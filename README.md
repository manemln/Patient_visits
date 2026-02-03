# Healthcare Data Management System

A high-performance healthcare data management system built with advanced data structures (AVL Trees and Graphs) to efficiently handle and analyze 1 million patient visit records.

This system manages large-scale healthcare data with efficient indexing, querying, and graph-based analysis capabilities. It handles patient visits, doctor referrals, treatment costs, and medical outcomes across multiple departments.

### Capabilities:
- **Fast Indexing**: O(log n) search operations using AVL trees
- **Graph Analysis**: Doctor referral networks and patient journey tracking
- **Real-time CRUD**: Add, modify, and delete records with automatic index updates
- **Range Queries**: Efficient cost range searches
- **Network Analysis**: BFS/DFS traversals for referral chain analysis

## System Architecture

┌─────────────────────────────────────────────────────────────┐
│                     Streamlit UI Layer                       │
│         (User Interface & Visualization)                     │
└────────────────────┬────────────────────────────────────────┘
                     │
┌────────────────────┴────────────────────────────────────────┐
│                  Query Engine Layer                          │
│    (Business Logic & Query Processing)                       │
└────┬────────────────────────────┬───────────────────────────┘
     │                            │
┌────┴────────────┐    ┌──────────┴──────────┐
│  Index Manager  │    │   Graph Manager     │
│  (AVL Trees)    │    │  (Directed Graph)   │
└────┬────────────┘    └──────────┬──────────┘
     │                            │
     └────────────┬───────────────┘
                  │
┌─────────────────┴────────────────────────────────────────────┐
│                   Data Storage Layer                          │
│              (In-Memory Dictionary)                           │
└───────────────────────────────────────────────────────────────┘


## Features

### 1. **Multi-Index System**
- **Patient Index**: Find all visits for a specific patient
- **Doctor Index**: Find all visits handled by a doctor
- **Cost Index**: Search by treatment cost with range queries
- **Visit Index**: Direct visit lookup

### 2. **Graph-Based Analysis**
- **Patient Journey**: Track complete patient visit history
- **Referral Networks**: Analyze doctor referral patterns with adjustable depth
- **Referral Chains**: Trace complete referral paths
- **Path Finding**: Find connections between visits

### 3. **Advanced Queries**
- Range-based cost queries
- Multi-attribute search
- Graph traversals (BFS/DFS)
- Strongly connected components

### 4. **Record Management**
- Add new records with duplicate detection
- Modify existing records with automatic re-indexing
- Delete records with cascade index updates
- Data validation and type checking

### 5. **Interactive Dashboard**
- Real-time statistics and metrics
- Department distribution visualization
- Cost analysis by department
- Recent records display

## Technology Stack

### Core
- **Python 3.x**: Primary programming language
- **Streamlit**: Web-based UI framework
- **Faker**: Synthetic data generation
- **CSV**: Data persistence

### Data Structures
- **AVL Trees**: Self-balancing BST for O(log n) operations
- **Directed Graphs**: Referral network representation
- **Hash Tables**: In-memory record storage

## Installation

### Prerequisites
```bash
Python 3.7 or higher
pip (Python package manager)
```

### Step 1: Clone or Download the Project
```bash
cd PROJECT_DSA
```

### Step 2: Installations
```bash
pip install streamlit faker
```

### Step 3: Generate Dataset
If you need to regenerate the dataset:
```bash
python data/generator.py
```
creates a CSV file with 1,000,000 synthetic patient visit records

### Step 4: Run the Application
```bash
cd UI
streamlit run app.py
```

The application will open in your default browser at `http://localhost:8501`



### Running the Application

```bash
# Navigate to UI directory
cd PROJECT_DSA/UI

streamlit run app.py
```

## Data Structure Design

### 1. AVL Tree Implementation

**Purpose**: Maintain sorted indices with guaranteed O(log n) operations

**Operations**:
- **Insert**: O(log n) - Add record with automatic balancing
- **Search**: O(log n) - Find records by key
- **Delete**: O(log n) - Remove record with rebalancing
- **Range Query**: O(log n + k) - Find all records in range

**Balancing Strategy**:
```
Balance Factor = Height(Left) - Height(Right)
If |Balance Factor| > 1, perform rotations:
  - Left-Left: Right rotation
  - Right-Right: Left rotation
  - Left-Right: Left rotation then right rotation
  - Right-Left: Right rotation then left rotation
```

**Node Structure**:
```python
class AVLNode:
    - key: Search key (patient_id, doctor_id, cost, visit_id)
    - record_ids: List of visit IDs with this key
    - height: Node height for balancing
    - left, right: Child pointers
```

### 2. Graph Implementation

**Purpose**: Model referral relationships and patient journeys

**Structure**:
- **Vertices**: Represent individual patient visits
- **Edges**: Represent referrals between visits

**Components**:
```python
class Vertex:
    - visit_id: Unique identifier
    - element: Visit record data
    - color: For traversal algorithms (white/gray/black)
    - distance: BFS distance from source
    - predecessor: Parent in traversal tree
    - discovery_time: DFS discovery time
    - finish_time: DFS finish time

class Edge:
    - origin: Source vertex (referring visit)
    - destination: Target vertex (referred visit)
    - element: Referral metadata
```

**Traversal Algorithms**:

**BFS (Breadth-First Search)**:
- **Time Complexity**: O(V + E)
- **Use Case**: Finding shortest referral paths
- **Process**: Level-by-level exploration

**DFS (Depth-First Search)**:
- **Time Complexity**: O(V + E)
- **Use Case**: Detecting referral cycles, topological sorting
- **Process**: Explore as deep as possible before backtracking

### 3. Index Manager

**Purpose**: Coordinate multiple indices for efficient multi-attribute queries

**Indices Maintained**:
```python
- by_patient: AVL Tree (patient_id[visit_ids])
- by_doctor: AVL Tree (doctor_id[visit_ids])
- by_cost: AVL Tree (treatment_cost[visit_ids])
- by_visit: AVL Tree (visit_id[visit_id])
```

**Operations**:
- **Build**: O(n log n) - Construct all indices from dataset
- **Add Record**: O(log n) - Insert into all relevant indices
- **Delete Record**: O(log n) - Remove from all indices
- **Modify Record**: O(log n) - Update relevant indices
- **Range Query**: O(log n + k) - Find records in cost range

### 4. Storage Layer
**Structure**: Hash table (Python dictionary)
```python
storage = {
    visit_id: {
        'visit_id': int,
        'patient_id': int,
        'doctor_id': int,
        'department': str,
        'diagnosis': str,
        'treatment_cost': float,
        'number_of_visits': int,
        'risk_score': float,
        'referral_doctor': int or None,
        'outcome_score': float
    }
}
```

**Advantages**:
- O(1) average case lookup
- O(1) insertion and deletion
- Efficient memory usage for large datasets

## Performance Analysis

### Time Complexity

| Operation | Index Manager | Graph Manager |
|-----------|--------------|---------------|
| Search by ID | O(log n) | N/A |
| Range Query | O(log n + k) | N/A |
| Add Record | O(log n) | O(1) |
| Delete Record | O(log n) | O(E) |
| Modify Record | O(log n) | O(1) |
| BFS Traversal | N/A | O(V + E) |
| DFS Traversal | N/A | O(V + E) |
| Find Path | N/A | O(V + E) |

Where:
- n = number of records
- k = number of results in range
- V = number of vertices (visits)
- E = number of edges (referrals)

### Space Complexity

| Component | Space Usage |
|-----------|-------------|
| Storage | O(n) |
| Each AVL Index | O(n) |
| Total Indices | O(4n) = O(n) |
| Graph Vertices | O(n) |
| Graph Edges | O(r) where r = referrals |
| **Total** | **O(n + r)** |


### File Descriptions
#### `storage.py`
- **DataStorage**: CSV loading and record management
- **AVLNode**: Tree node with balancing metadata
- **AVLTree**: Self-balancing binary search tree
- **IndexManager**: Multi-index coordination

#### `graph.py`
- **Vertex**: Graph node representing visits
- **Edge**: Connection between visits (referrals)
- **Graph**: Directed graph with traversal algorithms
- **GraphManager**: High-level graph operations

#### `query_engine.py`
- Unified query interface
- Combines index and graph operations
- Simplified API for UI layer

#### `generator.py`
- Creates synthetic patient visit data
- Configurable record count
- Realistic medical departments and diagnoses

#### `app.py`
- Streamlit-based web interface
- 8 different views/pages
- Interactive visualizations and controls

### `main.py`
- Example usages
