import os

from .eutilities import download_pubmed_ids
from .esummary import (
    articles_to_dataframe,
    extract_articles_from_esummaries,
)


directory = os.path.dirname(os.path.abspath(__file__))

pubmed_ids = [
    '27094199',  # Circ Cardiovasc Genet
    '26158728',  # PLoS Comput Biol
    '25648772',  # PeerJ
    '21736753',  # BioData Min
    '25915600',  # Nature Genet
    '20081222',  # Bioinformatics
]

esummary_path = os.path.join(directory, 'data', 'esummary.xml')
efetch_path = os.path.join(directory, 'data', 'efetch.xml')
dates_path = os.path.join(directory, 'data', 'dates.tsv')


def test_esummary():
    """
    Run to recreate data/esummary.xml
    """
    with open(esummary_path, 'wt') as write_file:
        download_pubmed_ids(pubmed_ids, write_file, endpoint='esummary')


def test_efetch():
    """
    Run to recreate data/esummary.xml
    """
    with open(efetch_path, 'wt') as write_file:
        download_pubmed_ids(pubmed_ids, write_file, endpoint='efetch')


def test_extract_articles():
    n_articles = len(pubmed_ids)
    articles = extract_articles_from_esummaries(esummary_path, n_articles)
    assert len(articles) == n_articles
    article_df = articles_to_dataframe(articles)
    article_df.to_csv(dates_path, index=False, sep='\t')
