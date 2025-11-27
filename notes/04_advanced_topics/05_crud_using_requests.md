# Day 21: Web APIs & HTTP Requests for Bioinformatics

## 🌐 Access Biological Databases Programmatically

Master **HTTP requests** and **REST APIs** to access vast biological databases like NCBI, Ensembl, UniProt, and PDB. Learn to fetch sequences, retrieve annotations, search databases, and integrate external data into your bioinformatics pipelines programmatically.

### Why Web APIs for Bioinformatics?

- **Database Access**: Query NCBI, Ensembl, UniProt without manual downloads
- **Real-Time Data**: Get latest genomic annotations and sequences
- **Automation**: Build pipelines that fetch data automatically
- **Integration**: Combine multiple databases in analyses
- **Reproducibility**: Document exact data sources and versions

---

## 🎯 Learning Objectives

By the end of this guide, you will:

✓ Understand REST APIs and HTTP methods  
✓ Use requests library for API calls  
✓ Access NCBI E-utilities programmatically  
✓ Fetch sequences from Ensembl REST API  
✓ Query UniProt for protein information  
✓ Handle API rate limits and errors  
✓ Parse JSON and XML responses  

---

## 🧩 Part 1: HTTP Basics

### Understanding HTTP Methods

```python
# GET - Retrieve data (read)
# POST - Create new data
# PUT - Update existing data
# DELETE - Remove data
# PATCH - Partial update

# In bioinformatics, we mostly use GET
```

### Status Codes

```python
# 200 - OK (success)
# 400 - Bad Request (invalid parameters)
# 404 - Not Found (resource doesn't exist)
# 429 - Too Many Requests (rate limit exceeded)
# 500 - Internal Server Error (server problem)
```

### Installing requests

```bash
pip install requests
```

---

## 🧩 Part 2: Basic Requests

### Simple GET Request

```python
import requests

# Make GET request
response = requests.get('https://api.example.com/data')

# Check status
print(f"Status code: {response.status_code}")

# Get content
if response.status_code == 200:
    data = response.json()  # Parse JSON
    print(data)
else:
    print(f"Error: {response.status_code}")
```

### Request with Parameters

```python
import requests

url = 'https://api.example.com/search'

# Parameters as dictionary
params = {
    'query': 'BRCA1',
    'organism': 'human',
    'limit': 10
}

response = requests.get(url, params=params)

# URL will be: https://api.example.com/search?query=BRCA1&organism=human&limit=10

print(f"URL: {response.url}")
print(f"Data: {response.json()}")
```

### Headers

```python
import requests

url = 'https://api.example.com/data'

# Custom headers
headers = {
    'User-Agent': 'BioinformaticsScript/1.0',
    'Accept': 'application/json'
}

response = requests.get(url, headers=headers)
```

### Handling Errors

```python
import requests

try:
    response = requests.get('https://api.example.com/data', timeout=10)
    response.raise_for_status()  # Raises exception for 4xx/5xx codes
    
    data = response.json()
    print(data)
    
except requests.exceptions.Timeout:
    print("Request timed out")
    
except requests.exceptions.ConnectionError:
    print("Connection error")
    
except requests.exceptions.HTTPError as e:
    print(f"HTTP error: {e}")
    
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
```

---

## 🧩 Part 3: NCBI E-utilities

### Understanding E-utilities

NCBI provides **E-utilities** - web services for searching and retrieving data from databases like GenBank, PubMed, Gene, etc.

**Base URL**: `https://eutils.ncbi.nlm.nih.gov/entrez/eutils/`

**Main utilities**:
- `esearch.fcgi` - Search database
- `efetch.fcgi` - Fetch records
- `esummary.fcgi` - Get summaries
- `elink.fcgi` - Find related records

### Searching GenBank

```python
import requests

def search_ncbi(query, database='nucleotide', retmax=10):
    """
    Search NCBI database
    
    Parameters:
        query: Search term
        database: NCBI database (nucleotide, protein, gene, etc.)
        retmax: Maximum results to return
    
    Returns:
        List of IDs
    """
    base_url = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi'
    
    params = {
        'db': database,
        'term': query,
        'retmax': retmax,
        'retmode': 'json'
    }
    
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        id_list = data['esearchresult']['idlist']
        return id_list
    else:
        print(f"Error: {response.status_code}")
        return []

# Example: Search for BRCA1 sequences
ids = search_ncbi('BRCA1[Gene] AND Homo sapiens[Organism]', retmax=5)
print(f"Found {len(ids)} records")
print(f"IDs: {ids}")
```

### Fetching Sequences

```python
import requests
import time

def fetch_ncbi_sequence(id_list, database='nucleotide', rettype='fasta'):
    """
    Fetch sequences from NCBI
    
    Parameters:
        id_list: List of NCBI IDs
        database: Database name
        rettype: Return type (fasta, gb, etc.)
    
    Returns:
        Sequence data as text
    """
    base_url = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi'
    
    # Convert list to comma-separated string
    ids = ','.join(str(i) for i in id_list)
    
    params = {
        'db': database,
        'id': ids,
        'rettype': rettype,
        'retmode': 'text'
    }
    
    # Be nice to NCBI - add delay
    time.sleep(0.34)  # Max 3 requests per second
    
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        return response.text
    else:
        print(f"Error: {response.status_code}")
        return None

# Example: Fetch sequences
ids = ['NM_007294', 'NM_000546']  # BRCA1 and TP53
sequences = fetch_ncbi_sequence(ids, rettype='fasta')

if sequences:
    print("Fetched sequences:")
    print(sequences[:500])  # Print first 500 characters
```

### Complete NCBI Search & Fetch

```python
import requests
import time

class NCBIFetcher:
    """Class for interacting with NCBI E-utilities"""
    
    BASE_URL = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/'
    
    def __init__(self, email=None, api_key=None):
        """
        Initialize NCBI fetcher
        
        Parameters:
            email: Your email (required by NCBI)
            api_key: API key for higher rate limits (optional)
        """
        self.email = email
        self.api_key = api_key
        self.delay = 0.1 if api_key else 0.34  # 10 vs 3 requests/sec
    
    def search(self, query, database='nucleotide', retmax=20):
        """Search NCBI database"""
        url = self.BASE_URL + 'esearch.fcgi'
        
        params = {
            'db': database,
            'term': query,
            'retmax': retmax,
            'retmode': 'json'
        }
        
        if self.email:
            params['email'] = self.email
        if self.api_key:
            params['api_key'] = self.api_key
        
        time.sleep(self.delay)
        
        response = requests.get(url, params=params)
        response.raise_for_status()
        
        data = response.json()
        return data['esearchresult']['idlist']
    
    def fetch(self, id_list, database='nucleotide', rettype='fasta'):
        """Fetch records by ID"""
        url = self.BASE_URL + 'efetch.fcgi'
        
        ids = ','.join(str(i) for i in id_list)
        
        params = {
            'db': database,
            'id': ids,
            'rettype': rettype,
            'retmode': 'text'
        }
        
        if self.email:
            params['email'] = self.email
        if self.api_key:
            params['api_key'] = self.api_key
        
        time.sleep(self.delay)
        
        response = requests.get(url, params=params)
        response.raise_for_status()
        
        return response.text
    
    def search_and_fetch(self, query, database='nucleotide', retmax=5):
        """Search and fetch in one call"""
        print(f"Searching for: {query}")
        ids = self.search(query, database, retmax)
        print(f"Found {len(ids)} records")
        
        if ids:
            print("Fetching sequences...")
            sequences = self.fetch(ids, database)
            return sequences
        
        return None

# Example usage
fetcher = NCBIFetcher(email='your.email@example.com')

# Search and fetch human insulin sequences
insulin = fetcher.search_and_fetch(
    query='insulin[Gene] AND Homo sapiens[Organism]',
    database='nucleotide',
    retmax=3
)

if insulin:
    print(insulin[:500])
```

---

## 🧩 Part 4: Ensembl REST API

### Understanding Ensembl API

Ensembl provides REST API for genomic data:
- **Base URL**: `https://rest.ensembl.org`
- **No API key required** (but rate limited)
- **Returns JSON** by default

### Fetching Sequence by ID

```python
import requests
import time

def get_ensembl_sequence(gene_id, species='human'):
    """
    Get sequence from Ensembl
    
    Parameters:
        gene_id: Ensembl gene ID (e.g., ENSG00000139618)
        species: Species name
    
    Returns:
        Sequence data as dictionary
    """
    url = f'https://rest.ensembl.org/sequence/id/{gene_id}'
    
    headers = {
        'Content-Type': 'application/json'
    }
    
    params = {
        'type': 'genomic'  # or 'cds', 'cdna', 'protein'
    }
    
    response = requests.get(url, headers=headers, params=params)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error {response.status_code}: {response.text}")
        return None

# Example: Get BRCA2 sequence
brca2_data = get_ensembl_sequence('ENSG00000139618')

if brca2_data:
    print(f"ID: {brca2_data['id']}")
    print(f"Length: {len(brca2_data['seq'])} bp")
    print(f"Sequence (first 100 bp): {brca2_data['seq'][:100]}")
```

### Looking Up Gene Information

```python
import requests

def lookup_gene(gene_symbol, species='human'):
    """
    Look up gene by symbol
    
    Parameters:
        gene_symbol: Gene symbol (e.g., 'BRCA1')
        species: Species name
    
    Returns:
        Gene information
    """
    url = f'https://rest.ensembl.org/lookup/symbol/{species}/{gene_symbol}'
    
    headers = {'Content-Type': 'application/json'}
    
    params = {'expand': 1}  # Include additional info
    
    response = requests.get(url, headers=headers, params=params)
    
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Example: Look up TP53
tp53_info = lookup_gene('TP53')

if tp53_info:
    print(f"Gene: {tp53_info['display_name']}")
    print(f"ID: {tp53_info['id']}")
    print(f"Chromosome: {tp53_info['seq_region_name']}")
    print(f"Location: {tp53_info['start']}-{tp53_info['end']}")
    print(f"Strand: {tp53_info['strand']}")
```

### Batch Requests

```python
import requests
import json

def batch_lookup_genes(gene_symbols, species='human'):
    """
    Look up multiple genes in one request
    
    Parameters:
        gene_symbols: List of gene symbols
        species: Species name
    
    Returns:
        Dictionary of gene information
    """
    url = 'https://rest.ensembl.org/lookup/symbol/homo_sapiens'
    
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    
    # POST request with JSON body
    data = {
        'symbols': gene_symbols
    }
    
    response = requests.post(url, headers=headers, data=json.dumps(data))
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None

# Example: Look up multiple cancer genes
genes = ['BRCA1', 'BRCA2', 'TP53', 'EGFR', 'KRAS']
results = batch_lookup_genes(genes)

if results:
    for gene_symbol, info in results.items():
        if info:
            print(f"{gene_symbol}: {info['id']} on chr{info['seq_region_name']}")
```

---

## 🧩 Part 5: UniProt API

### Searching UniProt

```python
import requests

def search_uniprot(query, format='json', limit=10):
    """
    Search UniProt database
    
    Parameters:
        query: Search query
        format: Return format (json, fasta, xml)
        limit: Maximum results
    
    Returns:
        Search results
    """
    url = 'https://rest.uniprot.org/uniprotkb/search'
    
    params = {
        'query': query,
        'format': format,
        'size': limit
    }
    
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        if format == 'json':
            return response.json()
        else:
            return response.text
    else:
        print(f"Error: {response.status_code}")
        return None

# Example: Search for human insulin
results = search_uniprot('gene:INS AND organism:9606', limit=5)

if results:
    print(f"Found {len(results['results'])} entries")
    for entry in results['results']:
        print(f"\nProtein: {entry['primaryAccession']}")
        print(f"Name: {entry['uniProtkbId']}")
        if 'proteinDescription' in entry:
            print(f"Description: {entry['proteinDescription']['recommendedName']['fullName']['value']}")
```

### Fetching Protein Sequence

```python
import requests

def get_uniprot_sequence(accession):
    """
    Get protein sequence from UniProt
    
    Parameters:
        accession: UniProt accession (e.g., P04637)
    
    Returns:
        FASTA format sequence
    """
    url = f'https://rest.uniprot.org/uniprotkb/{accession}.fasta'
    
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.text
    else:
        print(f"Error: {response.status_code}")
        return None

# Example: Get p53 protein sequence
p53_sequence = get_uniprot_sequence('P04637')

if p53_sequence:
    print(p53_sequence)
```

---

## 🧩 Part 6: Practical Applications

### Complete Gene Information Fetcher

```python
import requests
import time
from typing import Dict, Optional

class BioDataFetcher:
    """Unified interface for biological databases"""
    
    def __init__(self):
        self.ncbi_delay = 0.34
        self.last_request_time = 0
    
    def _rate_limit(self):
        """Enforce rate limiting"""
        elapsed = time.time() - self.last_request_time
        if elapsed < self.ncbi_delay:
            time.sleep(self.ncbi_delay - elapsed)
        self.last_request_time = time.time()
    
    def get_gene_info_ensembl(self, gene_symbol: str, species: str = 'human') -> Optional[Dict]:
        """Get gene information from Ensembl"""
        url = f'https://rest.ensembl.org/lookup/symbol/{species}/{gene_symbol}'
        headers = {'Content-Type': 'application/json'}
        
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            return response.json()
        return None
    
    def get_sequence_ensembl(self, gene_id: str) -> Optional[str]:
        """Get genomic sequence from Ensembl"""
        url = f'https://rest.ensembl.org/sequence/id/{gene_id}'
        headers = {'Content-Type': 'application/json'}
        params = {'type': 'genomic'}
        
        response = requests.get(url, headers=headers, params=params)
        
        if response.status_code == 200:
            data = response.json()
            return data['seq']
        return None
    
    def search_ncbi(self, query: str, database: str = 'nucleotide', retmax: int = 10):
        """Search NCBI database"""
        self._rate_limit()
        
        url = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi'
        params = {
            'db': database,
            'term': query,
            'retmax': retmax,
            'retmode': 'json'
        }
        
        response = requests.get(url, params=params)
        
        if response.status_code == 200:
            data = response.json()
            return data['esearchresult']['idlist']
        return []
    
    def get_comprehensive_info(self, gene_symbol: str) -> Dict:
        """Get comprehensive information from multiple sources"""
        info = {
            'gene_symbol': gene_symbol,
            'ensembl': None,
            'sequence': None,
            'ncbi_ids': None
        }
        
        print(f"Fetching information for {gene_symbol}...")
        
        # Get Ensembl info
        ensembl_data = self.get_gene_info_ensembl(gene_symbol)
        if ensembl_data:
            info['ensembl'] = {
                'id': ensembl_data['id'],
                'chromosome': ensembl_data['seq_region_name'],
                'start': ensembl_data['start'],
                'end': ensembl_data['end'],
                'strand': ensembl_data['strand']
            }
            
            # Get sequence
            sequence = self.get_sequence_ensembl(ensembl_data['id'])
            if sequence:
                info['sequence'] = {
                    'length': len(sequence),
                    'preview': sequence[:100]
                }
        
        # Search NCBI
        ncbi_query = f"{gene_symbol}[Gene] AND Homo sapiens[Organism]"
        ncbi_ids = self.search_ncbi(ncbi_query, retmax=3)
        if ncbi_ids:
            info['ncbi_ids'] = ncbi_ids
        
        return info

# Example usage
fetcher = BioDataFetcher()

# Get comprehensive information about BRCA1
brca1_info = fetcher.get_comprehensive_info('BRCA1')

print("\n=== BRCA1 Information ===")
if brca1_info['ensembl']:
    print(f"Ensembl ID: {brca1_info['ensembl']['id']}")
    print(f"Location: chr{brca1_info['ensembl']['chromosome']}:"
          f"{brca1_info['ensembl']['start']}-{brca1_info['ensembl']['end']}")

if brca1_info['sequence']:
    print(f"Sequence length: {brca1_info['sequence']['length']} bp")
    print(f"Preview: {brca1_info['sequence']['preview']}...")

if brca1_info['ncbi_ids']:
    print(f"NCBI IDs: {', '.join(brca1_info['ncbi_ids'])}")
```

### Batch Sequence Downloader

```python
import requests
import time
from pathlib import Path

def download_sequences_batch(gene_symbols, output_dir='sequences'):
    """
    Download sequences for multiple genes
    
    Parameters:
        gene_symbols: List of gene symbols
        output_dir: Directory to save sequences
    """
    output_path = Path(output_dir)
    output_path.mkdir(exist_ok=True)
    
    print(f"Downloading sequences for {len(gene_symbols)} genes...")
    
    for gene in gene_symbols:
        print(f"\nProcessing {gene}...")
        
        # Look up gene
        url = f'https://rest.ensembl.org/lookup/symbol/human/{gene}'
        headers = {'Content-Type': 'application/json'}
        
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            gene_info = response.json()
            gene_id = gene_info['id']
            
            # Get sequence
            seq_url = f'https://rest.ensembl.org/sequence/id/{gene_id}'
            seq_response = requests.get(seq_url, headers=headers, 
                                       params={'type': 'genomic'})
            
            if seq_response.status_code == 200:
                seq_data = seq_response.json()
                
                # Save to file
                filename = output_path / f"{gene}.fasta"
                with open(filename, 'w') as f:
                    f.write(f">{gene}|{gene_id}\n")
                    # Write in 60-char lines
                    seq = seq_data['seq']
                    for i in range(0, len(seq), 60):
                        f.write(seq[i:i+60] + '\n')
                
                print(f"  Saved to {filename}")
            else:
                print(f"  Failed to fetch sequence")
        else:
            print(f"  Gene not found")
        
        time.sleep(0.1)  # Be nice to the server
    
    print(f"\nDone! Sequences saved to {output_dir}/")

# Example: Download sequences for cancer genes
cancer_genes = ['TP53', 'BRCA1', 'BRCA2', 'EGFR', 'KRAS']
# download_sequences_batch(cancer_genes)
```

---

## 📝 Practice Tasks (Day 21)

### Basic Exercises

1. **Simple GET**: Make a GET request to a public API and print the response.

2. **NCBI Search**: Search NCBI for a specific gene and print the IDs returned.

3. **Ensembl Lookup**: Look up a gene symbol in Ensembl and print its location.

4. **Error Handling**: Write code that handles HTTP errors gracefully.

5. **Rate Limiting**: Implement a function with rate limiting (max 3 requests/second).

### Intermediate Challenges

6. **Sequence Fetcher**: Create a function that searches NCBI and fetches sequences in one call.

7. **Batch Lookup**: Look up multiple genes from Ensembl in a single batch request.

8. **Format Converter**: Fetch sequence from NCBI in GenBank format and convert to FASTA.

9. **Data Integration**: Combine data from NCBI and Ensembl for the same gene.

10. **Cache Results**: Implement caching to avoid redundant API calls.

### Advanced Challenges

11. **API Client Class**: Build a complete API client class with methods for search, fetch, and batch operations.

12. **Parallel Downloads**: Download sequences for multiple genes using threading or async.

13. **Retry Logic**: Implement automatic retries with exponential backoff for failed requests.

14. **Database Builder**: Create a local SQLite database populated from API data.

15. **API Wrapper**: Create a unified interface that abstracts multiple APIs (NCBI, Ensembl, UniProt).

---

## 💡 Key Takeaways

✓ **REST APIs** enable programmatic database access  
✓ **requests library** simplifies HTTP operations  
✓ **GET requests** retrieve data, POST sends data  
✓ **Status codes** indicate success (200) or errors (4xx, 5xx)  
✓ **NCBI E-utilities** provide esearch and efetch  
✓ **Ensembl REST API** offers genomic data in JSON  
✓ **UniProt API** provides protein information  
✓ **Rate limiting** is crucial - respect server limits  
✓ **Error handling** prevents crashes on failed requests  
✓ **Time delays** (time.sleep) enforce rate limits  
✓ **Headers** specify content type and user agent  
✓ **Parameters** customize API queries  
✓ **JSON format** is standard for modern APIs  
✓ **Batch requests** reduce number of API calls  
✓ **Document data sources** for reproducibility  

**Next**: Jupyter Notebooks & Interactive Analysis
