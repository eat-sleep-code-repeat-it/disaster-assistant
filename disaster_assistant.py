import csv
import os
import pickle
from dotenv import load_dotenv
import faiss
import numpy as np
import openai
load_dotenv(override=True)

openai_api_key = os.getenv('OPENAI_API_KEY')
if openai_api_key:
    print(f"OpenAI API Key exists and begins {openai_api_key[:8]}")
else:
    print("OpenAI API Key not set - please head to the troubleshooting guide in the setup folder")

from typing import List, Optional, Tuple
from pydantic import BaseModel, Field, ValidationError, field_validator
from datetime import date
class DisasterDeclaration(BaseModel):
    """
    Use this model when working with individual disaster declaration.
    """
    disasterNumber: int = Field(description="Sequentially assigned number used to designate an event or incident declared as a disaster")
    declarationTitle: str =  Field(description="Title for the disaster	")
    state: str = Field(description="The name or phrase describing the U.S. state, district, or territory")
    designatedArea: str = Field(description="The name or phrase describing the geographic area that was included in the declaration")
    declarationType: str = Field(description="Two character code that defines if this is a major disaster, fire management, or emergency declaration")
    declarationDate: date = Field(description="Date the disaster was declared")
    incidentBeginDate: date = Field(description="Date the incident itself began")
    incidentEndDate: Optional[date] = Field(default=None, description="Date the incident itself ended")
    fipsStateCode: str = Field(description="FIPS two-digit numeric code used to identify the United States, the District of Columbia, US territories, outlying areas of the US and freely associated states")
    fipsCountyCode: str = Field(description="FIPS three-digit numeric code used to identify counties and county equivalents in the United States, the District of Columbia, US territories, outlying areas of the US and freely associated states")
    ihProgramDeclared: bool = Field(description="Denotes whether the Individuals and Households program was declared for this disaster")
    iaProgramDeclared: bool = Field(description="Denotes whether the Individual Assistance program was declared for this disaster")
    paProgramDeclared: bool = Field(description="Denotes whether the Public Assistance program was declared for this disaster")
    incidentType:str = Field(description="The primary or official type of incident such as fire or flood. Secondary incident types may have been designated. See the designatedIncidentTypes field")
    
    @field_validator('incidentEndDate', mode='before')
    @classmethod
    def parse_incident_end_date(cls, v):
        if v in (None, ''):
            return None
        return v

#######################################################
def read_disaster_declarations_from_csv(file_path: str) -> List[DisasterDeclaration]:
    """
    load declarations as structured date model from csv
    """
    declarations = []
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            try:
                # Convert disasterNumber to int explicitly
                if 'disasterNumber' in row and row['disasterNumber']:
                    row['disasterNumber'] = int(row['disasterNumber'])
                decl = DisasterDeclaration(**row)
                declarations.append(decl)
            except ValidationError as e:
                print(f"Skipping invalid row: {e}")
    print(f"Loaded {len(declarations)} disaster declarations from CSV")
    return declarations

#######################################################
def build_faiss_index(declarations: List[DisasterDeclaration]) -> Tuple[faiss.IndexFlatL2, List[DisasterDeclaration]]:    
    """
    Creates and populates a FAISS vector index from disaster embeddings.
    """
    print("Creating embeddings and building FAISS index...")
    embeddings = []
    for decl in declarations:
        print(f"create_text_for_embedding {decl.disasterNumber}...")
        text = create_text_for_embedding(decl)
        emb = get_embedding(text)
        embeddings.append(emb)
    dimension = len(embeddings[0])
    index = faiss.IndexFlatL2(dimension)
    embeddings_np = np.array(embeddings).astype('float32')
    index.add(embeddings_np)
    print(f"FAISS index built with {index.ntotal} vectors")
    return index, declarations

#######################################################
def create_text_for_embedding(declaration: DisasterDeclaration, score: Optional[float] = None) -> str:
    parts = [
        f"DisasterNumber: {declaration.disasterNumber}",
        f"State: {declaration.state}",
        f"County: {declaration.designatedArea or 'N/A'}",
        f"DeclarationType: {declaration.declarationType or 'N/A'}",
        f"DeclarationDate: {declaration.declarationDate or 'N/A'}",
        f"declarationTitle: {declaration.declarationTitle or 'N/A'}",
        f"IncidentType: {declaration.incidentType or 'N/A'}",
        f"IncidentBeginDate: {declaration.incidentBeginDate or 'N/A'}",
        f"IncidentEndDate: {declaration.incidentEndDate or 'N/A'}"
    ]
    if score is not None:
        parts.append(f"FAISS Score: {round(score, 3)}")
    return ". ".join(parts)

#######################################################
def get_embedding(text: str) -> List[float]:
    """
    Embeds the structured disaster description using OpenAI Embeddings API.
    """
    response = openai.embeddings.create(
        model="text-embedding-3-small", #model="text-embedding-ada-002",
        input=text
    )
    return response.data[0].embedding

#######################################################
def save_index_and_metadata(index, metadata, index_path, metadata_path):
    """
    Storing FAISS index and embeddings to disk 
    FAISS stores only the vectors
    Need to keep track of the original data (e.g., disaster declarations) corresponding to each vector.
    and reloading them later to avoid recomputing embeddings and rebuilding the index every time you run the script.
    This saves a ton of time and API usage.
    """
    faiss.write_index(index, index_path)
    with open(metadata_path, "wb") as f:
        pickle.dump(metadata, f)

#######################################################
def load_index_and_metadata(index_path, metadata_path):
    """
    Reload  FAISS index and embeddings to avoid recomputing embeddings and rebuilding the index every time you run the script.
    This saves a ton of time and API usage.
    """    
    index = faiss.read_index(index_path)
    with open(metadata_path, "rb") as f:
        metadata = pickle.load(f)
    return index, metadata

#######################################################
def test_setup(question: str):
    question = "What is 2+2?"
    from openai import OpenAI
    openai = OpenAI()  
    messages = [{"role": "user", "content": question}]
    response = openai.chat.completions.create(
        model="gpt-4.1-mini",
        messages=messages
    )
    print(response.choices[0].message.content) 
#######################################################
def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    csv_file = os.path.join(script_dir, "data", "disaster_declarations.csv")
    disaster_declarations = read_disaster_declarations_from_csv(csv_file) 

    index_file = os.path.join(script_dir, "saved_index","disaster_faiss.index")
    index_metadata_file = os.path.join(script_dir, "saved_index", "disaster_metadata.pkl")
    if os.path.exists(index_file) and os.path.exists(index_metadata_file):
        index, indexed_declarations = load_index_and_metadata(index_file, index_metadata_file)
    else:
        index, indexed_declarations = build_faiss_index(disaster_declarations)
        save_index_and_metadata(index, indexed_declarations, index_file, index_metadata_file)
    
    question = "What is 2+2?"
    test_setup(question)

#######################################################
#
if __name__ == "__main__":
    main()