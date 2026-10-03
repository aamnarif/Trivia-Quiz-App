import random
import streamlit as st

# ──────────────────────────────────────────────────────────────────────────
# DATA: 10 questions per module (5 easy, 3 medium, 2 hard = 50/30/20)
# ──────────────────────────────────────────────────────────────────────────
DATA = {
    "algorithms": {
        "name": "Algorithms", "icon": "📈", "color": "#a78bf0", "level": "Level 3",
        "qs": [
            {"topic": "Complexity", "diff": "easy", "q": "What does Big-O notation describe about an algorithm?", "a": ["Its exact runtime in seconds", "The upper bound on its growth rate", "How much memory it uses on disk", "The number of lines of code"], "c": 1},
            {"topic": "Complexity", "diff": "easy", "q": "What is the worst-case time complexity of binary search on a sorted array?", "a": ["O(log n)", "O(n)", "O(n log n)", "O(1)"], "c": 0},
            {"topic": "Graphs", "diff": "easy", "q": "Which traversal finds the shortest path in an unweighted graph?", "a": ["Depth-first search", "Breadth-first search", "Topological sort", "Union-find"], "c": 1},
            {"topic": "Sorting", "diff": "easy", "q": "Which comparison sort is stable and O(n log n) in the worst case?", "a": ["Quicksort", "Merge sort", "Heapsort", "Selection sort"], "c": 1},
            {"topic": "Graphs", "diff": "medium", "q": "Dijkstra's algorithm gives incorrect results when a graph contains what?", "a": ["Cycles", "Negative edge weights", "Disconnected nodes", "Self-loops"], "c": 1},
            {"topic": "Paradigms", "diff": "medium", "q": "Which technique solves problems with overlapping subproblems by reusing stored results?", "a": ["Divide and conquer", "Backtracking", "Dynamic programming", "Greedy selection"], "c": 2},
            {"topic": "Sorting", "diff": "easy", "q": "What is quicksort's average-case time complexity?", "a": ["O(n²)", "O(n log n)", "O(n)", "O(log n)"], "c": 1},
            {"topic": "Sorting", "diff": "medium", "q": "What is quicksort's worst-case time complexity?", "a": ["O(n log n)", "O(log n)", "O(n²)", "O(n)"], "c": 2},
            {"topic": "Recurrences", "diff": "hard", "q": "The Master Theorem is used to directly solve which kind of recurrence?", "a": ["Linear recurrences", "Divide-and-conquer recurrences", "Recursive backtracking", "Amortized sequences"], "c": 1},
            {"topic": "Sorting", "diff": "hard", "q": "Which sorting algorithm is non-comparison-based and can sort integers in O(n) time?", "a": ["Merge sort", "Heapsort", "Radix sort", "Insertion sort"], "c": 2},
        ],
    },
    "ds": {
        "name": "Data Structures", "icon": "🗂️", "color": "#5aa9f5", "level": "Level 4",
        "qs": [
            {"topic": "Linear", "diff": "easy", "q": "Which structure removes elements in last-in, first-out order?", "a": ["Queue", "Stack", "Deque", "Priority queue"], "c": 1},
            {"topic": "Linear", "diff": "easy", "q": "Which structure removes elements in first-in, first-out order?", "a": ["Stack", "Queue", "Binary tree", "Hash set"], "c": 1},
            {"topic": "Hashing", "diff": "easy", "q": "Which structure offers O(1) average-case lookup by key?", "a": ["Hash table", "Balanced BST", "Linked list", "Sorted array"], "c": 0},
            {"topic": "Trees", "diff": "medium", "q": "What is the height of a balanced binary search tree with n nodes?", "a": ["O(n)", "O(√n)", "O(log n)", "O(n log n)"], "c": 2},
            {"topic": "Heaps", "diff": "easy", "q": "In a min-heap, which element is guaranteed to sit at the root?", "a": ["The median", "The smallest", "The largest", "The most recently added"], "c": 1},
            {"topic": "Trees", "diff": "easy", "q": "Which traversal visits left subtree, root, then right subtree?", "a": ["Pre-order", "In-order", "Post-order", "Level-order"], "c": 1},
            {"topic": "Hashing", "diff": "medium", "q": "What is the average-case time complexity of inserting into a hash table?", "a": ["O(n)", "O(log n)", "O(1)", "O(n²)"], "c": 2},
            {"topic": "Linear", "diff": "medium", "q": "Which pair of structures is standard for an O(1) LRU cache?", "a": ["Array + binary search", "Hash map + doubly linked list", "Two stacks", "Heap + set"], "c": 1},
            {"topic": "Trees", "diff": "hard", "q": "Which self-balancing BST maintains balance using a color property on each node?", "a": ["AVL tree", "Red-Black tree", "Splay tree", "B-tree"], "c": 1},
            {"topic": "Trees", "diff": "hard", "q": "A trie is most naturally suited for which kind of lookup?", "a": ["Range queries on numbers", "Prefix-based string lookups", "Nearest-neighbour search", "Constant-time hashing"], "c": 1},
        ],
    },
    "db": {
        "name": "Databases", "icon": "🗄️", "color": "#4ec9a6", "level": "Level 2",
        "qs": [
            {"topic": "Transactions", "diff": "easy", "q": "In ACID, what does the \u201cI\u201d stand for?", "a": ["Integrity", "Indexing", "Isolation", "Immutability"], "c": 2},
            {"topic": "Indexing", "diff": "easy", "q": "Adding an index primarily improves which operation?", "a": ["Inserts", "Lookups", "Backups", "Replication"], "c": 1},
            {"topic": "Modelling", "diff": "easy", "q": "What does a PRIMARY KEY guarantee for a column?", "a": ["It is always numeric", "It is unique and not null", "It is indexed automatically for speed only", "It can be duplicated once"], "c": 1},
            {"topic": "Normalization", "diff": "medium", "q": "Which normal form eliminates transitive dependencies on the primary key?", "a": ["1NF", "2NF", "3NF", "BCNF"], "c": 2},
            {"topic": "SQL", "diff": "medium", "q": "Which clause filters rows after they have been grouped?", "a": ["WHERE", "HAVING", "FILTER", "QUALIFY"], "c": 1},
            {"topic": "Modelling", "diff": "easy", "q": "A foreign key constraint exists to enforce what?", "a": ["Referential integrity", "Uniqueness", "Encryption", "Row ordering"], "c": 0},
            {"topic": "SQL", "diff": "easy", "q": "Which join returns only rows that match in both tables?", "a": ["LEFT JOIN", "INNER JOIN", "FULL OUTER JOIN", "CROSS JOIN"], "c": 1},
            {"topic": "Distributed", "diff": "hard", "q": "Under CAP, a partition-tolerant system that stays available must relax what?", "a": ["Durability", "Consistency", "Latency", "Atomicity"], "c": 1},
            {"topic": "Distributed", "diff": "hard", "q": "What does \u201ceventual consistency\u201d mean for database replicas?", "a": ["Writes are rejected until synced", "Replicas converge to the same state over time", "Reads always block until synced", "Only the primary node can be read"], "c": 1},
            {"topic": "Transactions", "diff": "medium", "q": "What is a deadlock between two database transactions?", "a": ["One transaction runs out of memory", "Each is waiting on a lock the other holds", "A query returns no rows", "A transaction is rolled back automatically"], "c": 1},
        ],
    },
    "net": {
        "name": "Networks", "icon": "🌐", "color": "#ff9a5c", "level": "Level 1",
        "qs": [
            {"topic": "Transport", "diff": "easy", "q": "Which guarantee does TCP provide that UDP does not?", "a": ["Lower latency", "Ordered, reliable delivery", "Multicast", "Smaller headers"], "c": 1},
            {"topic": "Protocols", "diff": "easy", "q": "Which port does DNS use by default?", "a": ["25", "53", "80", "443"], "c": 1},
            {"topic": "HTTP", "diff": "easy", "q": "What does HTTP status 301 signal to a client?", "a": ["Moved permanently", "Temporarily unavailable", "Not modified", "Forbidden"], "c": 0},
            {"topic": "OSI", "diff": "medium", "q": "At which OSI layer does IP operate?", "a": ["Layer 2: data link", "Layer 3: network", "Layer 4: transport", "Layer 7: application"], "c": 1},
            {"topic": "Transport", "diff": "medium", "q": "Which sequence opens a TCP connection?", "a": ["ACK, SYN, FIN", "SYN, SYN-ACK, ACK", "GET, 200, CLOSE", "HELLO, ACK"], "c": 1},
            {"topic": "Protocols", "diff": "easy", "q": "What does NAT primarily do at the network edge?", "a": ["Encrypts traffic", "Maps private addresses to a public one", "Compresses packets", "Resolves hostnames"], "c": 1},
            {"topic": "HTTP", "diff": "easy", "q": "Which HTTP method is safe and idempotent, used only to retrieve data?", "a": ["POST", "GET", "PUT", "DELETE"], "c": 1},
            {"topic": "Transport", "diff": "hard", "q": "What does TCP's three-way handshake primarily protect against?", "a": ["Packet compression errors", "Stray segments from an old, previous connection", "DNS spoofing", "IP fragmentation"], "c": 1},
            {"topic": "Routing", "diff": "medium", "q": "Which routing protocol type builds a full map of network topology at each router?", "a": ["Distance-vector", "Link-state", "Path-vector", "Static routing"], "c": 1},
            {"topic": "Routing", "diff": "hard", "q": "What problem does BGP (Border Gateway Protocol) primarily solve?", "a": ["Resolving domain names", "Routing between autonomous systems on the internet", "Assigning local IP addresses", "Encrypting web traffic"], "c": 1},
        ],
    },
    "os": {
        "name": "Operating Systems", "icon": "⚙️", "color": "#f2586f", "level": "Level 2",
        "qs": [
            {"topic": "Memory", "diff": "easy", "q": "Thrashing is caused by what?", "a": ["Excessive paging", "Too many threads", "Fragmented disks", "Cache coherence"], "c": 0},
            {"topic": "Scheduling", "diff": "easy", "q": "Round-robin scheduling is best described as what?", "a": ["Preemptive", "Non-preemptive", "Real-time only", "Cooperative"], "c": 0},
            {"topic": "Memory", "diff": "easy", "q": "Which memory region holds local variables and call frames?", "a": ["The heap", "The stack", "The data segment", "The page table"], "c": 1},
            {"topic": "Processes", "diff": "easy", "q": "What is the smallest unit the CPU scheduler dispatches?", "a": ["Process", "Thread", "Page", "Segment"], "c": 1},
            {"topic": "Concurrency", "diff": "medium", "q": "Deadlock needs mutual exclusion, hold-and-wait, no preemption, and what else?", "a": ["Starvation", "Circular wait", "Priority inversion", "Race condition"], "c": 1},
            {"topic": "Processes", "diff": "easy", "q": "A context switch saves and restores which state?", "a": ["The page cache", "The register set and process control block", "Open sockets only", "The file system journal"], "c": 1},
            {"topic": "Scheduling", "diff": "medium", "q": "Which scheduling algorithm can starve long jobs by always favoring the shortest one?", "a": ["Round-robin", "Shortest Job First", "First-Come First-Served", "Multilevel feedback queue"], "c": 1},
            {"topic": "Concurrency", "diff": "hard", "q": "What is a race condition?", "a": ["A CPU running above its rated clock speed", "An outcome that depends on the timing of uncontrolled concurrent access", "A process that never terminates", "A page fault under high load"], "c": 1},
            {"topic": "Memory", "diff": "hard", "q": "Which technique divides physical memory into fixed-size blocks to eliminate external fragmentation?", "a": ["Segmentation", "Paging", "Compaction", "Swapping"], "c": 1},
            {"topic": "Memory", "diff": "medium", "q": "What does virtual memory allow a process to do?", "a": ["Skip the operating system scheduler", "Use more memory than is physically installed, via disk", "Run without an MMU", "Bypass context switching"], "c": 1},
        ],
    },
    "ai": {
        "name": "AI & ML", "icon": "🧠", "color": "#e0ae13", "level": "Level 3",
        "qs": [
            {"topic": "Training", "diff": "easy", "q": "A model with low training error and high test error is showing what?", "a": ["Underfitting", "Overfitting", "Data leakage", "Vanishing gradients"], "c": 1},
            {"topic": "Optimization", "diff": "easy", "q": "Gradient descent iteratively minimizes which quantity?", "a": ["The loss function", "The learning rate", "The batch size", "The parameter count"], "c": 0},
            {"topic": "Fundamentals", "diff": "easy", "q": "Which type of learning trains a model on labeled input-output pairs?", "a": ["Unsupervised learning", "Reinforcement learning", "Supervised learning", "Self-supervised learning"], "c": 2},
            {"topic": "Neural nets", "diff": "easy", "q": "A softmax layer outputs what?", "a": ["A single logit", "A probability distribution", "A binary mask", "A normalized gradient"], "c": 1},
            {"topic": "Regularization", "diff": "medium", "q": "Which method fights overfitting by randomly deactivating units during training?", "a": ["Batch norm", "Dropout", "Early pooling", "Weight tying"], "c": 1},
            {"topic": "Classic ML", "diff": "easy", "q": "In k-nearest neighbours, what does k control?", "a": ["Feature count", "Neighbours that vote", "Tree depth", "Cluster radius"], "c": 1},
            {"topic": "Evaluation", "diff": "medium", "q": "Precision is defined as which ratio?", "a": ["TP / (TP + FP)", "TP / (TP + FN)", "(TP + TN) / all", "FP / (FP + TN)"], "c": 0},
            {"topic": "Evaluation", "diff": "medium", "q": "What is the purpose of a validation set, kept separate from train and test sets?", "a": ["To measure final, unbiased performance", "To tune hyperparameters during development", "To augment the training data", "To label unlabeled data"], "c": 1},
            {"topic": "Neural nets", "diff": "hard", "q": "In a convolutional neural network, what does a pooling layer primarily do?", "a": ["Add non-linearity", "Downsample feature maps to reduce spatial size", "Normalize the input", "Compute the loss"], "c": 1},
            {"topic": "Fundamentals", "diff": "hard", "q": "What does the bias-variance tradeoff describe?", "a": ["Balancing training speed against accuracy", "Balancing underfitting against overfitting", "Balancing GPU memory against batch size", "Balancing precision against recall only"], "c": 1},
        ],
    },
    "qub": {
        "name": "Queen's & Belfast", "icon": "🎓", "color": "#4263eb", "level": "Local",
        "qs": [
            {"topic": "Campus", "diff": "easy", "q": "In which city is Queen's University Belfast located?", "a": ["Dublin", "Belfast", "Derry", "Cork"], "c": 1},
            {"topic": "Campus", "diff": "easy", "q": "What is the name of Queen's University Belfast's iconic main building, designed by Sir Charles Lanyon?", "a": ["Whitla Hall", "Lanyon Building", "Riddel Hall", "McClay Library"], "c": 1},
            {"topic": "QUB CS", "diff": "easy", "q": "Which school at Queen's teaches Computer Science alongside Electronics and Electrical Engineering?", "a": ["School of Mathematics and Physics", "School of Electronics, Electrical Engineering and Computer Science", "School of Computing Science", "School of Informatics"], "c": 1},
            {"topic": "History", "diff": "medium", "q": "In what year was Queen's University Belfast founded by Royal Charter?", "a": ["1810", "1845", "1908", "1920"], "c": 1},
            {"topic": "Belfast", "diff": "easy", "q": "Which famous ocean liner was built at Belfast's Harland and Wolff shipyard?", "a": ["Queen Mary", "Titanic", "Lusitania", "Britannia"], "c": 1},
            {"topic": "QUB CS", "diff": "medium", "q": "What does CSIT, the major cyber security research centre based at Queen's, stand for?", "a": ["Centre for Software and IT", "Centre for Secure Information Technologies", "Cyber Security Innovation Team", "Computer Science and IT"], "c": 1},
            {"topic": "History", "diff": "easy", "q": "Queen's University Belfast is a member of which group of UK research-intensive universities?", "a": ["Ivy League", "Russell Group", "Sutton Trust", "1994 Group"], "c": 1},
            {"topic": "QUB CS", "diff": "hard", "q": "Which Queen's University Belfast computer science professor won the 1980 ACM Turing Award for his work on programming languages?", "a": ["Alan Turing", "Tony Hoare", "Edsger Dijkstra", "John McCarthy"], "c": 1},
            {"topic": "QUB CS", "diff": "hard", "q": "Which widely taught sorting algorithm was invented by Queen's Turing Award winning professor Tony Hoare?", "a": ["Merge sort", "Quicksort", "Heapsort", "Radix sort"], "c": 1},
            {"topic": "History", "diff": "medium", "q": "The Irish Universities Act 1908 split the Queen's University of Ireland into Queen's University Belfast and which other institution?", "a": ["Trinity College Dublin", "National University of Ireland", "University College Cork", "Ulster University"], "c": 1},
        ],
    },
}

PROFILE_COLORS = ["#a78bf0", "#5aa9f5", "#4ec9a6", "#ff9a5c", "#f2586f", "#e0ae13"]
MAX_PROFILES = 4

BRAND = "#4f33a8"
BRAND_2 = "#6f4fd1"
BRAND_DEEP = "#2f1c6b"
SOFT = "#ece7fb"
POP = "#ffd23f"
POP_DEEP = "#e0ae13"
INK = "#33212a"
INK_2 = "#7a6670"
INK_3 = "#a6939c"
CARD = "#fffdfd"
LINE = "#f3e3e7"
DIFF_COLOR = {"easy": "#4ec9a6", "medium": "#e0ae13", "hard": "#f2586f"}

st.set_page_config(page_title="Quiz World", page_icon="⚡", layout="wide")

# ──────────────────────────────────────────────────────────────────────────
# GLOBAL STYLE
# ──────────────────────────────────────────────────────────────────────────
st.html(f"""
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>
html, body, [class*="css"] {{ font-family: 'Inter', sans-serif; }}
.stApp {{ background: linear-gradient(170deg, {BRAND_2} 0%, {BRAND} 46%, {BRAND_DEEP} 100%); }}
.block-container {{ padding-top: 1.6rem; padding-bottom: 3rem; max-width: 1080px; }}
h1, h2, h3, h4, h5 {{ font-weight: 800 !important; letter-spacing: -0.015em; color: {INK}; }}
div[data-testid="stButton"] > button[kind="primary"] {{ background: {POP} !important; color: {INK} !important; border: none !important; border-radius: 999px !important; font-weight: 700 !important; font-size: 14.5px !important; padding: 0.65rem 1.4rem !important; box-shadow: 0 4px 0 {POP_DEEP} !important; transition: transform 0.1s ease !important; }}
div[data-testid="stButton"] > button[kind="primary"]:hover {{ transform: translateY(-2px); }}
div[data-testid="stButton"] > button[kind="primary"]:active {{ transform: translateY(2px) !important; box-shadow: 0 1px 0 {POP_DEEP} !important; }}
div[data-testid="stButton"] > button[kind="secondary"] {{ background: transparent !important; color: {INK_2} !important; border: 2px solid {LINE} !important; border-radius: 999px !important; font-weight: 700 !important; font-size: 13.5px !important; padding: 0.55rem 1.2rem !important; }}
div[data-testid="stButton"] > button[kind="secondary"]:hover {{ border-color: {BRAND} !important; color: {BRAND_DEEP} !important; }}
[class*="st-key-catcard_"] {{ background: {CARD} !important; border-radius: 24px !important; box-shadow: 0 2px 0 rgba(51,33,42,.05), 0 10px 26px rgba(47,28,107,.18) !important; padding: 18px !important; margin-bottom: 16px !important; }}
[class*="st-key-catcard_"] div[data-testid="stButton"] > button[kind="secondary"] {{ width: 100% !important; margin-top: 10px !important; background: {SOFT} !important; border-color: transparent !important; color: {BRAND_DEEP} !important; }}
[class*="st-key-catcard_"] div[data-testid="stButton"] > button[kind="secondary"]:hover {{ background: {POP} !important; color: {INK} !important; }}
[class*="st-key-profcard_"] {{ background: {CARD} !important; border-radius: 26px !important; box-shadow: 0 2px 0 rgba(51,33,42,.05), 0 10px 26px rgba(47,28,107,.18) !important; padding: 22px 16px 14px !important; text-align: center !important; margin-bottom: 16px !important; }}
[class*="st-key-profcard_"] div[data-testid="stButton"] > button[kind="secondary"] {{ width: 100% !important; margin-top: 12px !important; }}
[class*="st-key-modecard_"] {{ background: {CARD} !important; border-radius: 26px !important; box-shadow: 0 2px 0 rgba(51,33,42,.05), 0 10px 26px rgba(47,28,107,.18) !important; padding: 24px !important; margin-bottom: 16px !important; }}
[class*="st-key-modecard_"] div[data-testid="stButton"] > button[kind="secondary"] {{ width: 100% !important; margin-top: 14px !important; background: {SOFT} !important; border-color: transparent !important; color: {BRAND_DEEP} !important; }}
[class*="st-key-qcard"] {{ background: {CARD} !important; border-radius: 28px !important; box-shadow: 0 2px 0 rgba(51,33,42,.05), 0 10px 26px rgba(47,28,107,.18) !important; padding: 26px !important; }}
[class*="st-key-qcard"] div[data-testid="stButton"] > button[kind="secondary"] {{ width: 100% !important; text-align: left !important; justify-content: flex-start !important; background: {CARD} !important; border: 2px solid {LINE} !important; border-radius: 18px !important; padding: 0.85rem 1.1rem !important; font-weight: 600 !important; font-size: 14.5px !important; color: {INK} !important; margin-bottom: 6px !important; }}
[class*="st-key-qcard"] div[data-testid="stButton"] > button[kind="secondary"]:hover {{ border-color: {BRAND} !important; background: {SOFT} !important; color: {INK} !important; }}
[class*="st-key-resultcard"] {{ background: {CARD} !important; border-radius: 28px !important; box-shadow: 0 2px 0 rgba(51,33,42,.05), 0 10px 26px rgba(47,28,107,.18) !important; padding: 26px !important; text-align: center !important; }}
[class*="st-key-formcard"] {{ background: {CARD} !important; border-radius: 26px !important; box-shadow: 0 2px 0 rgba(51,33,42,.05), 0 10px 26px rgba(47,28,107,.18) !important; padding: 26px !important; max-width: 480px !important; }}
[class*="st-key-splashcard"] {{ text-align: center; padding: 60px 20px; }}
[class*="st-key-splashcard"] div[data-testid="stButton"] {{ display: flex; justify-content: center; }}
[class*="st-key-splashcard"] div[data-testid="stButton"] > button[kind="primary"] {{ margin-top: 22px !important; }}
[class*="st-key-avatarwrap"] div[data-testid="stButton"] > button {{ width: 36px !important; height: 36px !important; border-radius: 13px !important; padding: 0 !important; background: {BRAND} !important; color: white !important; border: none !important; font-weight: 700 !important; font-size: 12.5px !important; }}
[class*="st-key-navwrap_"] div[data-testid="stButton"] > button {{ border: none !important; background: transparent !important; color: {INK_2} !important; font-size: 13.5px !important; padding: 8px 14px !important; }}
[class*="st-key-navwrap_"] div[data-testid="stButton"] > button:hover {{ background: {SOFT} !important; color: {BRAND_DEEP} !important; }}
.qw-card {{ background: {CARD}; border-radius: 26px; box-shadow: 0 2px 0 rgba(51,33,42,.05), 0 10px 26px rgba(47,28,107,.18); padding: 22px 24px; }}
.qw-pill {{ display: inline-flex; align-items: center; gap: 6px; font-size: 12.5px; font-weight: 700; padding: 6px 13px; border-radius: 999px; }}
.qw-logo {{ display: flex; align-items: center; gap: 9px; font-weight: 800; font-size: 18px; color: white; }}
.qw-logo .mark {{ width: 30px; height: 30px; border-radius: 11px; background: {CARD}; display: grid; place-items: center; color: {BRAND}; font-size: 15px; }}
.qw-logo-dark {{ display: flex; align-items: center; gap: 9px; font-weight: 800; font-size: 18px; color: {INK}; }}
.qw-logo-dark .mark {{ width: 30px; height: 30px; border-radius: 11px; background: {BRAND}; display: grid; place-items: center; color: white; font-size: 15px; }}
[class*="st-key-header_row"] {{ background: {CARD} !important; border-radius: 22px !important; box-shadow: 0 2px 0 rgba(51,33,42,.05), 0 10px 26px rgba(47,28,107,.18) !important; padding: 10px 18px !important; margin-bottom: 20px !important; }}
[class*="st-key-header_row"], [class*="st-key-navgroup"], [class*="st-key-header_right"] {{ flex-wrap: nowrap !important; }}
[class*="st-key-header_right"] {{ margin-left: auto !important; }}
[class*="st-key-rankpreview"] {{ background: {CARD} !important; border-radius: 26px !important; box-shadow: 0 2px 0 rgba(51,33,42,.05), 0 10px 26px rgba(47,28,107,.18) !important; padding: 20px 22px !important; }}
[class*="st-key-rankpreview"] div[data-testid="stButton"] > button {{ border: none !important; background: transparent !important; color: {BRAND_DEEP} !important; font-size: 13px !important; padding: 4px 0 !important; }}
[class*="st-key-rankpreview"] div[data-testid="stButton"] > button:hover {{ text-decoration: underline !important; }}
[class*="st-key-onpurple"] div[data-testid="stButton"] > button[kind="secondary"] {{ color: white !important; border-color: rgba(255,255,255,.6) !important; }}
[class*="st-key-onpurple"] div[data-testid="stButton"] > button[kind="secondary"]:hover {{ background: rgba(255,255,255,.16) !important; border-color: white !important; color: white !important; }}
.qw-coin {{ display: inline-flex; align-items: center; gap: 6px; padding: 7px 13px; border-radius: 999px; background: {POP}; font-size: 13px; font-weight: 700; box-shadow: 0 3px 0 {POP_DEEP}; color: {INK}; }}
.cat-icon {{ width: 46px; height: 46px; border-radius: 16px; display: grid; place-items: center; font-size: 22px; }}
.cat-level {{ font-size: 11.5px; font-weight: 700; padding: 4px 10px; border-radius: 999px; background: {SOFT}; color: {BRAND_DEEP}; }}
.cat-name {{ font-weight: 800; font-size: 17.5px; margin: 10px 0 2px; color: {INK}; }}
.cat-sub {{ font-size: 12.5px; color: {INK_2}; margin-bottom: 10px; }}
.diff-bar {{ display: flex; height: 7px; border-radius: 4px; overflow: hidden; }}
.qw-progress {{ height: 10px; border-radius: 6px; background: {LINE}; overflow: hidden; margin-bottom: 22px; }}
.qw-progress-fill {{ height: 100%; border-radius: 6px; background: linear-gradient(90deg, {BRAND_2}, {BRAND}); }}
.qw-opt-row {{ display: flex; align-items: center; gap: 12px; padding: 12px 16px; border-radius: 18px; margin-bottom: 6px; font-weight: 600; font-size: 14.5px; }}
.qw-opt-letter {{ width: 26px; height: 26px; border-radius: 9px; display: grid; place-items: center; font-size: 12.5px; font-weight: 800; flex-shrink: 0; }}
.qw-stat {{ background: {SOFT}; border-radius: 18px; padding: 13px 14px; }}
.qw-stat .v {{ font-weight: 800; font-size: 24px; color: {INK}; line-height: 1.05; }}
.qw-stat .l {{ font-size: 11.5px; color: {INK_2}; }}
.team-card {{ display: flex; align-items: center; gap: 12px; border-radius: 20px; padding: 14px 18px; margin-bottom: 4px; }}
.team-chip {{ width: 36px; height: 36px; border-radius: 13px; display: grid; place-items: center; font-size: 16px; flex-shrink: 0; }}
.rank-row {{ display: flex; align-items: center; gap: 12px; padding: 12px 0; border-bottom: 1px solid {LINE}; }}
[data-testid="stDialog"] {{ background: {CARD} !important; border-radius: 26px !important; color: {INK} !important; }}
[data-testid="stDialog"] svg {{ fill: {INK} !important; }}
div[data-testid="stTextInput"] input {{ background: {CARD} !important; color: {BRAND} !important; border: 2px solid {LINE} !important; border-radius: 12px !important; }}
div[data-testid="stTextInput"] input::placeholder {{ color: {INK_3} !important; opacity: 1 !important; }}
div[data-testid="stTextInput"] input:focus {{ border-color: {BRAND} !important; box-shadow: 0 0 0 1px {BRAND} !important; }}
div[data-testid="stWidgetLabel"] p {{ color: {INK_2} !important; }}
@keyframes pulse-ring {{ 0% {{ transform: scale(.85); opacity: .5; }} 100% {{ transform: scale(1.8); opacity: 0; }} }}
@keyframes bob {{ 0%, 100% {{ transform: translateY(0); }} 50% {{ transform: translateY(-7px); }} }}
.splash-mark {{ position: relative; width: 104px; height: 104px; margin: 0 auto 20px; display: grid; place-items: center; }}
.splash-ring {{ position: absolute; inset: 0; border-radius: 34px; border: 3px solid rgba(255,255,255,.55); animation: pulse-ring 1.9s ease-out infinite; }}
.splash-box {{ width: 104px; height: 104px; border-radius: 34px; background: {CARD}; display: grid; place-items: center; box-shadow: 0 14px 34px rgba(47,28,107,.35); animation: bob 2.6s ease-in-out infinite; font-size: 46px; }}
#MainMenu, header, footer {{ visibility: hidden; }}
</style>
""")

# ──────────────────────────────────────────────────────────────────────────
# STATE
# ──────────────────────────────────────────────────────────────────────────
ss = st.session_state
ss.setdefault("screen", "splash")
ss.setdefault("player_name", None)
ss.setdefault("player_initials", None)
ss.setdefault("player_color", BRAND)
ss.setdefault("mode", "solo")
ss.setdefault("cat", None)
ss.setdefault("questions", [])
ss.setdefault("qi", 0)
ss.setdefault("score", 0)
ss.setdefault("streak", 0)
ss.setdefault("best_streak", 0)
ss.setdefault("correct_count", 0)
ss.setdefault("answered", False)
ss.setdefault("picked", None)
ss.setdefault("topic_stats", {})
ss.setdefault("total_coins", 0)
ss.setdefault("games_played", 0)
ss.setdefault("profiles", [])
ss.setdefault("active_profile_idx", None)
ss.setdefault("teams", [{"name": "Team A", "score": 0, "correct": 0, "streak": 0},
                         {"name": "Team B", "score": 0, "correct": 0, "streak": 0}])
ss.setdefault("active_team", 0)
ss.setdefault("match_history", [])

IN_APP_SCREENS = {"home", "discover", "ranking", "play", "results", "winner"}

def goto(name):
    ss.screen = name

def enter_profiles():
    ss.screen = "profiles"

def select_profile(idx):
    p = ss.profiles[idx]
    ss.player_name = p["name"]
    ss.player_initials = p["initials"]
    ss.player_color = p["color"]
    ss.active_profile_idx = idx
    ss.screen = "mode"

def remove_profile(idx):
    if 0 <= idx < len(ss.profiles):
        ss.profiles.pop(idx)
        if ss.active_profile_idx == idx:
            ss.active_profile_idx = None
            ss.player_name = None
            ss.player_initials = None
        elif ss.active_profile_idx is not None and ss.active_profile_idx > idx:
            ss.active_profile_idx -= 1

def go_new_player_form():
    ss.screen = "new_player_form"

def make_initials(name):
    name = (name or "").strip()
    if not name:
        return "GU"
    parts = name.split()
    if len(parts) >= 2:
        return (parts[0][0] + parts[1][0]).upper()
    return name[:2].upper()

def active_profile_stats():
    if ss.active_profile_idx is not None and ss.active_profile_idx < len(ss.profiles):
        p = ss.profiles[ss.active_profile_idx]
        return p["coins"], p["games"]
    return 0, 0

def team_win_counts():
    wins = {}
    for m in ss.match_history:
        if m["type"] == "team" and m["winner"]:
            wins[m["winner"]] = wins.get(m["winner"], 0) + 1
    return sorted(wins.items(), key=lambda x: -x[1])

def solo_scores_sorted():
    return sorted([m for m in ss.match_history if m["type"] == "solo"], key=lambda x: -x["score"])

def render_win_rows(rows):
    if not rows:
        return f"<div style='color:{INK_2};font-size:13.5px;padding:8px 0'>No team matches played yet this session.</div>"
    return "".join(f"""
    <div class="rank-row">
      <span style="flex:1;font-weight:600;color:{INK}">{name}</span>
      <span style="font-weight:800;color:{BRAND_DEEP}">{count} win{'s' if count != 1 else ''}</span>
    </div>
    """ for name, count in rows)

def render_solo_rows(rows):
    if not rows:
        return f"<div style='color:{INK_2};font-size:13.5px;padding:8px 0'>No solo rounds played yet this session.</div>"
    return "".join(f"""
    <div class="rank-row">
      <span style="flex:1">
        <span style="display:block;font-weight:600;color:{INK}">{m['name']}</span>
        <span style="display:block;font-size:11.5px;color:{INK_3}">{m['cat']}</span>
      </span>
      <span style="font-weight:800;color:{BRAND_DEEP}">🪙 {m['score']}</span>
    </div>
    """ for m in rows)

@st.dialog("Winning players")
def show_leaderboard_dialog():
    st.html(f"""
    <div style="font-weight:800;font-size:14px;margin-bottom:4px;color:{INK}">Team wins (this session)</div>
    {render_win_rows(team_win_counts())}
    """)
    st.write("")
    st.html(f"""
    <div style="font-weight:800;font-size:14px;margin-bottom:4px;color:{INK}">Solo scores (this session)</div>
    {render_solo_rows(solo_scores_sorted())}
    """)
    st.write("")
    if st.button("Close", type="primary", use_container_width=True):
        st.rerun()

def confirm_new_player():
    typed = st.session_state.get("new_player_name_input", "").strip()
    name = typed if typed else f"Player {len(ss.profiles) + 1}"
    color = PROFILE_COLORS[len(ss.profiles) % len(PROFILE_COLORS)]
    profile = {"name": name, "initials": make_initials(name), "color": color, "coins": 0, "games": 0}
    ss.profiles.append(profile)
    idx = len(ss.profiles) - 1
    ss.player_name = profile["name"]
    ss.player_initials = profile["initials"]
    ss.player_color = profile["color"]
    ss.active_profile_idx = idx
    ss.screen = "mode"

@st.dialog("Player limit reached")
def show_limit_dialog():
    st.write(f"You can only have {MAX_PROFILES} players at a time. Remove one from the list first, then add a new one.")
    if st.button("Got it", type="primary", use_container_width=True):
        st.rerun()

def set_mode(m):
    ss.mode = m
    ss.screen = "team_setup" if m == "teams" else "home"

def confirm_team_names():
    a = st.session_state.get("team_a_name_input", "").strip()
    b = st.session_state.get("team_b_name_input", "").strip()
    ss.teams[0]["name"] = a if a else "Team A"
    ss.teams[1]["name"] = b if b else "Team B"
    ss.screen = "home"

def order_by_difficulty(qs):
    easy = [q for q in qs if q["diff"] == "easy"]; random.shuffle(easy)
    med = [q for q in qs if q["diff"] == "medium"]; random.shuffle(med)
    hard = [q for q in qs if q["diff"] == "hard"]; random.shuffle(hard)
    return easy + med + hard

def start_category(key):
    if key == "mixed":
        pool = [dict(q, cat=k) for k in DATA for q in DATA[k]["qs"]]
        easy_pool = [q for q in pool if q["diff"] == "easy"]
        med_pool = [q for q in pool if q["diff"] == "medium"]
        hard_pool = [q for q in pool if q["diff"] == "hard"]
        qs = random.sample(easy_pool, 10) + random.sample(med_pool, 6) + random.sample(hard_pool, 4)
    else:
        qs = order_by_difficulty(DATA[key]["qs"][:])
    ss.cat = key
    ss.questions = qs
    ss.qi = 0
    ss.score = 0
    ss.streak = 0
    ss.correct_count = 0
    ss.answered = False
    ss.picked = None
    ss.topic_stats = {}
    if ss.mode == "teams":
        ss.teams[0]["score"] = 0; ss.teams[0]["correct"] = 0; ss.teams[0]["streak"] = 0
        ss.teams[1]["score"] = 0; ss.teams[1]["correct"] = 0; ss.teams[1]["streak"] = 0
    ss.active_team = 0
    ss.screen = "play"

def pick(idx):
    if ss.answered:
        return
    ss.picked = idx
    ss.answered = True
    q = ss.questions[ss.qi]
    stats = ss.topic_stats.setdefault(q["topic"], [0, 0])
    stats[1] += 1
    correct = idx == q["c"]
    if ss.mode == "teams":
        t = ss.teams[ss.active_team]
        if correct:
            t["streak"] += 1; t["correct"] += 1; t["score"] += 20 + (t["streak"] - 1) * 5; stats[0] += 1
        else:
            t["streak"] = 0
    else:
        if correct:
            ss.streak += 1
            ss.best_streak = max(ss.best_streak, ss.streak)
            ss.correct_count += 1
            ss.score += 20 + (ss.streak - 1) * 5
            stats[0] += 1
        else:
            ss.streak = 0

def next_question():
    ss.qi += 1
    ss.answered = False
    ss.picked = None
    if ss.mode == "teams" and ss.qi == len(ss.questions) // 2:
        ss.active_team = 1
    if ss.qi >= len(ss.questions):
        if ss.mode == "teams":
            ss.games_played += 1
            t0, t1 = ss.teams
            earned = t0["score"] + t1["score"]
            ss.total_coins += earned
            if ss.active_profile_idx is not None:
                prof = ss.profiles[ss.active_profile_idx]
                prof["coins"] += earned
                prof["games"] += 1
            winner = None
            if t0["score"] != t1["score"]:
                winner = t0["name"] if t0["score"] > t1["score"] else t1["name"]
            ss.match_history.append({"type": "team", "team_a": t0["name"], "team_b": t1["name"],
                                      "score_a": t0["score"], "score_b": t1["score"], "winner": winner})
            ss.screen = "winner"
        else:
            ss.total_coins += ss.score
            if ss.active_profile_idx is not None:
                prof = ss.profiles[ss.active_profile_idx]
                prof["coins"] += ss.score
                prof["games"] += 1
            ss.games_played += 1
            cat_name = DATA.get(ss.cat, {}).get("name", "Mixed Round")
            ss.match_history.append({"type": "solo", "name": ss.player_name, "score": ss.score, "cat": cat_name})
            ss.screen = "results"

def go_home():
    ss.screen = "home"

# ──────────────────────────────────────────────────────────────────────────
# HEADER
# ──────────────────────────────────────────────────────────────────────────
if ss.screen in IN_APP_SCREENS:
    with st.container(key="header_row", horizontal=True, horizontal_alignment="distribute",
                       vertical_alignment="center"):
        st.html('<div class="qw-logo-dark"><span class="mark">⚡</span>Quiz World</div>')
        with st.container(key="navgroup", horizontal=True, gap="small"):
            with st.container(key="navwrap_home"):
                st.button("Home", key="nav_home", on_click=goto, args=("home",), use_container_width=True)
            with st.container(key="navwrap_discover"):
                st.button("Discover", key="nav_discover", on_click=goto, args=("discover",), use_container_width=True)
            with st.container(key="navwrap_ranking"):
                st.button("Ranking", key="nav_ranking", on_click=goto, args=("ranking",), use_container_width=True)
        with st.container(key="header_right", horizontal=True, vertical_alignment="center", gap="small"):
            _hdr_coins, _hdr_games = active_profile_stats()
            st.html(f"<span class='qw-coin'>🪙 {_hdr_coins}</span>")
            with st.container(key="avatarwrap"):
                st.html(f"<style>[class*='st-key-avatarwrap'] div[data-testid='stButton'] > button {{ background:{ss.player_color} !important; }}</style>")
                st.button(ss.player_initials or "?", key="avatar_btn", on_click=enter_profiles)
    st.write("")
elif ss.screen != "splash":
    st.html('<div class="qw-logo"><span class="mark">⚡</span>Quiz World</div>')
    st.write("")

# ──────────────────────────────────────────────────────────────────────────
# SPLASH
# ──────────────────────────────────────────────────────────────────────────
if ss.screen == "splash":
    st.write("")
    st.write("")
    with st.container(key="splashcard"):
        st.html("""
        <div class="splash-mark">
          <div class="splash-ring"></div>
          <div class="splash-box">⚡</div>
        </div>
        <div style="font-weight:800;font-size:54px;line-height:1;color:white">Quiz World</div>
        <div style="font-size:15px;color:rgba(255,255,255,.88);margin-top:14px">Smart, fast, champion</div>
        """)
        c1, c2, c3 = st.columns([1, 1, 1])
        with c2:
            st.button("Tap to continue →", key="splash_go", type="primary",
                       on_click=enter_profiles, use_container_width=True)

# ──────────────────────────────────────────────────────────────────────────
# PROFILES
# ──────────────────────────────────────────────────────────────────────────
elif ss.screen == "profiles":
    st.html("""
    <h2 style="margin:0 0 6px;font-size:34px;color:white">Who's playing?</h2>
    <p style="margin:0 0 22px;font-size:15px;color:rgba(255,255,255,.85)">Pick a player to load their streak, coins and topic history.</p>
    """)
    n_slots = len(ss.profiles) + 1  # existing players + one "create" slot
    cols = st.columns(n_slots, gap="medium")

    for i, p in enumerate(ss.profiles):
        with cols[i]:
            with st.container(key=f"profcard_{i}"):
                meta = f"{p['games']} rounds · {p['coins']} coins" if p["games"] else "No rounds played yet"
                st.html(f"""
                <div style="width:64px;height:64px;margin:0 auto;border-radius:22px;display:grid;place-items:center;font-weight:800;font-size:22px;color:white;background:{p['color']}">{p['initials']}</div>
                <div style="font-weight:800;font-size:16px;margin-top:10px;color:{INK}">{p['name']}</div>
                <div style="font-size:11.5px;color:{INK_2}">{meta}</div>
                """)
                sb1, sb2 = st.columns(2)
                with sb1:
                    st.button("Select", key=f"pick_{i}", type="secondary",
                              on_click=select_profile, args=(i,), use_container_width=True)
                with sb2:
                    st.button("Remove", key=f"remove_{i}", type="secondary",
                              on_click=remove_profile, args=(i,), use_container_width=True)

    with cols[-1]:
        with st.container(key="profcard_new"):
            st.html(f"""
            <div style="width:64px;height:64px;margin:0 auto;border-radius:22px;display:grid;place-items:center;font-size:26px;border:2px dashed {LINE};color:{BRAND}">+</div>
            <div style="font-weight:800;font-size:16px;margin-top:10px;color:{INK}">New player</div>
            <div style="font-size:11.5px;color:{INK_2}">Start from zero</div>
            """)
            if len(ss.profiles) >= MAX_PROFILES:
                if st.button("Create", key="pick_new_full", type="secondary", use_container_width=True):
                    show_limit_dialog()
            else:
                st.button("Create", key="pick_new", type="secondary",
                          on_click=go_new_player_form, use_container_width=True)

    preview_rows = render_solo_rows(solo_scores_sorted()[:3])
    with st.container(key="rankpreview"):
        rc1, rc2 = st.columns([4, 1])
        with rc1:
            st.html("<h5 style='margin:0'>Quiz board ranking</h5>")
        with rc2:
            if st.button("See all", key="see_all_ranking", use_container_width=True):
                show_leaderboard_dialog()
        st.html(preview_rows)

# ──────────────────────────────────────────────────────────────────────────
# NEW PLAYER FORM
# ──────────────────────────────────────────────────────────────────────────
elif ss.screen == "new_player_form":
    with st.container(key="formcard"):
        st.html(f"""
        <div style="font-weight:800;font-size:22px;color:{INK};margin-bottom:4px">What's your name?</div>
        <div style="font-size:13.5px;color:{INK_2};margin-bottom:16px">This is shown on the leaderboard and in-game header.</div>
        """)
        st.text_input("Your name", key="new_player_name_input", label_visibility="collapsed", placeholder="e.g. Sam Carter")
        st.button("Continue →", key="new_player_continue", type="primary",
                  on_click=confirm_new_player, use_container_width=True)

# ──────────────────────────────────────────────────────────────────────────
# MODE SELECT
# ──────────────────────────────────────────────────────────────────────────
elif ss.screen == "mode":
    st.html(f"""
    <h2 style="margin:0 0 6px;font-size:34px;color:white">How do you want to play?</h2>
    <p style="margin:0 0 26px;font-size:15px;color:rgba(255,255,255,.85)">
      Hi {ss.player_name}. Solo tracks your own score and streak. Two teams splits the round evenly and crowns a winner at the end.
    </p>
    """)
    m1, m2 = st.columns(2, gap="medium")
    with m1:
        with st.container(key="modecard_solo"):
            st.html(f"""
            <div style="width:52px;height:52px;border-radius:18px;background:{SOFT};display:grid;place-items:center;font-size:24px">🙂</div>
            <div style="font-weight:800;font-size:20px;margin-top:12px;color:{INK}">Single player</div>
            <div style="font-size:13.5px;color:{INK_2};margin-top:4px">One player, one score. Streak bonuses, coins and a topic breakdown at the end.</div>
            """)
            st.button("Choose →", key="mode_solo", type="secondary", on_click=set_mode, args=("solo",), use_container_width=True)
    with m2:
        with st.container(key="modecard_teams"):
            st.html(f"""
            <div style="width:52px;height:52px;border-radius:18px;background:{SOFT};display:grid;place-items:center;font-size:24px">👥</div>
            <div style="font-weight:800;font-size:20px;margin-top:12px;color:{INK}">Two teams</div>
            <div style="font-size:13.5px;color:{INK_2};margin-top:4px">Questions split down the middle. Team A first, then Team B, then a winner page.</div>
            """)
            st.button("Choose →", key="mode_teams", type="secondary", on_click=set_mode, args=("teams",), use_container_width=True)

# ──────────────────────────────────────────────────────────────────────────
# TEAM SETUP
# ──────────────────────────────────────────────────────────────────────────
elif ss.screen == "team_setup":
    with st.container(key="formcard"):
        st.html(f"""
        <div style="font-weight:800;font-size:22px;color:{INK};margin-bottom:4px">Name your teams</div>
        <div style="font-size:13.5px;color:{INK_2};margin-bottom:16px">These names are used on the scoreboard and the ranking page.</div>
        """)
        st.text_input("Team A", key="team_a_name_input", placeholder="Team A")
        st.text_input("Team B", key="team_b_name_input", placeholder="Team B")
        st.button("Continue →", key="team_setup_continue", type="primary",
                  on_click=confirm_team_names, use_container_width=True)

# ──────────────────────────────────────────────────────────────────────────
# HOME
# ──────────────────────────────────────────────────────────────────────────
elif ss.screen == "home":
    left, right = st.columns([1.3, 1], gap="medium")
    with left:
        st.html(f"""
        <div class="qw-card" style="height:100%">
          <span class="qw-pill" style="background:{SOFT};color:{BRAND_DEEP}">🔥 9-day streak</span>
          <h2 style="margin:12px 0 8px;font-size:32px">Welcome back,<br>{ss.player_name}!</h2>
          <p style="margin:0 0 18px;font-size:14.5px;color:{INK_2};max-width:42ch">
            Playing as {ss.mode}. Jump into a topic, or browse everything on Discover.
          </p>
        </div>
        """)
        qp1, qp2 = st.columns(2)
        with qp1:
            st.button("▶ Quick play", key="quick_play", type="primary",
                      on_click=start_category, args=(random.choice(list(DATA.keys())),), use_container_width=True)
        with qp2:
            with st.container(key="onpurple_browse"):
                st.button("Browse all topics", key="to_discover", type="secondary",
                          on_click=goto, args=("discover",), use_container_width=True)
    with right:
        st.html(f"""
        <div class="qw-card" style="height:100%;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;gap:6px">
          <div style="font-size:46px">🏆</div>
          <div style="font-weight:800;font-size:15px;color:{INK}">{active_profile_stats()[1]} rounds played</div>
          <div style="font-size:12.5px;color:{INK_2}">{active_profile_stats()[0]} coins earned so far</div>
        </div>
        """)

# ──────────────────────────────────────────────────────────────────────────
# DISCOVER
# ──────────────────────────────────────────────────────────────────────────
elif ss.screen == "discover":
    st.html("""
    <h4 style="color:white;margin:0 0 4px">Discover topics</h4>
    <div style="color:rgba(255,255,255,.85);font-size:13px;margin-bottom:14px">7 modules · 10 questions each, 5 easy · 3 medium · 2 hard · plus a 20-question mixed round</div>
    """)
    cols = st.columns(3, gap="medium")
    for i, key in enumerate(DATA):
        cat = DATA[key]
        with cols[i % 3]:
            with st.container(key=f"catcard_{key}"):
                st.html(f"""
                <div style="display:flex;align-items:center;justify-content:space-between">
                  <div class="cat-icon" style="background:{cat['color']}">{cat['icon']}</div>
                  <span class="cat-level">{cat['level']}</span>
                </div>
                <div class="cat-name">{cat['name']}</div>
                <div class="cat-sub">10 questions · 5 easy · 3 medium · 2 hard</div>
                <div class="diff-bar">
                  <div style="width:50%;background:{DIFF_COLOR['easy']}"></div>
                  <div style="width:30%;background:{DIFF_COLOR['medium']}"></div>
                  <div style="width:20%;background:{DIFF_COLOR['hard']}"></div>
                </div>
                """)
                st.button(f"Start {cat['name']} →", key=f"start_{key}", type="secondary",
                          on_click=start_category, args=(key,), use_container_width=True)

    with st.container(key="catcard_mixed"):
        st.html(f"""
        <div class="cat-icon" style="background:{BRAND}">🔀</div>
        <div class="cat-name">Mixed Round</div>
        <div class="cat-sub">20 questions · every topic{' · split into 2 teams' if ss.mode == 'teams' else ''}</div>
        <div class="diff-bar">
          <div style="width:50%;background:{DIFF_COLOR['easy']}"></div>
          <div style="width:30%;background:{DIFF_COLOR['medium']}"></div>
          <div style="width:20%;background:{DIFF_COLOR['hard']}"></div>
        </div>
        """)
        st.button("Start Mixed Round →", key="start_mixed", type="secondary",
                  on_click=start_category, args=("mixed",), use_container_width=True)

# ──────────────────────────────────────────────────────────────────────────
# RANKING
# ──────────────────────────────────────────────────────────────────────────
elif ss.screen == "ranking":
    st.html("""
    <h4 style="color:white;margin:0 0 4px">Ranking</h4>
    <div style="color:rgba(255,255,255,.85);font-size:13px;margin-bottom:14px">Team wins and solo scores from this session.</div>
    """)

    win_html = render_win_rows(team_win_counts())
    solo_html = render_solo_rows(solo_scores_sorted())

    r1, r2 = st.columns(2, gap="medium")
    with r1:
        st.html(f"""
        <div class="qw-card">
          <h5 style="margin:0 0 8px;font-size:17px">Team wins (this session)</h5>
          {win_html}
        </div>
        """)
    with r2:
        st.html(f"""
        <div class="qw-card">
          <h5 style="margin:0 0 8px;font-size:17px">Solo scores (this session)</h5>
          {solo_html}
        </div>
        """)

# ──────────────────────────────────────────────────────────────────────────
# PLAY
# ──────────────────────────────────────────────────────────────────────────
elif ss.screen == "play":
    q = ss.questions[ss.qi]
    cat_key = q.get("cat", ss.cat)
    cat = DATA[cat_key]
    cat_label = "Mixed Round" if ss.cat == "mixed" else cat["name"]

    b1, b2, b3, b4 = st.columns([1, 1.4, 1, 1])
    with b1:
        with st.container(key="onpurple_exit"):
            st.button("← Exit", key="exit_btn", type="secondary", on_click=go_home)
    with b2:
        icon = "🔀" if ss.cat == "mixed" else cat["icon"]
        st.html(f"<span class='qw-pill' style='background:{CARD};color:{INK}'>{icon} {cat_label}</span>")
    with b3:
        live_score = ss.teams[ss.active_team]["score"] if ss.mode == "teams" else ss.score
        st.html(f"<span class='qw-coin'>🪙 {live_score}</span>")
    with b4:
        live_streak = ss.teams[ss.active_team]["streak"] if ss.mode == "teams" else ss.streak
        st.html(f"<span class='qw-pill' style='background:{CARD};color:{BRAND_DEEP}'>🔥 {live_streak}</span>")

    st.write("")

    if ss.mode == "teams":
        cards = ""
        for i, t in enumerate(ss.teams):
            active = i == ss.active_team
            bg = SOFT if active else LINE
            border = f"2px solid {BRAND}" if active else "2px solid transparent"
            status = "Now playing" if active else "Waiting"
            cards += f"""
            <div style="flex:1">
              <div class="team-card" style="background:{bg};border:{border}">
                <span class="team-chip" style="background:{BRAND if active else INK_3};color:white">👥</span>
                <span style="flex:1">
                  <span style="display:block;font-weight:700;font-size:14.5px;color:{INK}">{t['name']}</span>
                  <span style="display:block;font-size:11.5px;color:{INK_3}">{status} · {t['correct']} correct</span>
                </span>
                <span style="font-weight:800;font-size:20px;color:{INK}">{t['score']}</span>
              </div>
            </div>
            """
        st.html(f"<div style='display:flex;gap:12px;margin-bottom:14px'>{cards}</div>")

    progress_pct = int((ss.qi / len(ss.questions)) * 100)
    letters = ["A", "B", "C", "D"]

    with st.container(key="qcard"):
        turn_tag = f" · {ss.teams[ss.active_team]['name']}'s turn" if ss.mode == "teams" else ""
        st.html(f"""
        <div style="display:flex;align-items:center;justify-content:space-between;font-size:12.5px;font-weight:600;color:{INK_2};margin-bottom:8px">
          <span>Question {ss.qi + 1} of {len(ss.questions)}</span>
          <span style="color:{BRAND_DEEP}">{q['topic']} · {q['diff']}{turn_tag}</span>
        </div>
        <div class="qw-progress"><div class="qw-progress-fill" style="width:{progress_pct}%"></div></div>
        <h3 style="font-size:25px;margin:0 0 20px">{q['q']}</h3>
        """)

        if not ss.answered:
            for i, opt in enumerate(q["a"]):
                st.button(f"{letters[i]}   {opt}", key=f"opt_{ss.qi}_{i}", type="secondary",
                          on_click=pick, args=(i,), use_container_width=True)
        else:
            rows = ""
            for i, opt in enumerate(q["a"]):
                is_correct = i == q["c"]
                is_picked = i == ss.picked
                if is_correct:
                    bg, letter_bg, mark = "rgba(78,201,166,0.15)", "#4ec9a6", "✓"
                elif is_picked:
                    bg, letter_bg, mark = "rgba(242,88,111,0.12)", "#f2586f", "✗"
                else:
                    bg, letter_bg, mark = LINE, INK_3, ""
                rows += f"""
                <div class="qw-opt-row" style="background:{bg}">
                  <span class="qw-opt-letter" style="background:{letter_bg};color:white">{letters[i]}</span>
                  <span style="flex:1">{opt}</span>
                  <span style="font-weight:800">{mark}</span>
                </div>
                """
            st.html(rows)

            was_correct = ss.picked == q["c"]
            fb_color = "#4ec9a6" if was_correct else "#f2586f"
            gained = (ss.teams[ss.active_team]["streak"] if ss.mode == "teams" else ss.streak)
            fb_text = "Correct! +{} coins".format(20 + (gained - 1) * 5) if was_correct else "Not quite, check the highlighted answer"
            st.write("")
            f1, f2 = st.columns([2, 1])
            with f1:
                st.html(f"<div style='font-weight:700;color:{fb_color};padding-top:8px'>{fb_text}</div>")
            with f2:
                label = "Next question →" if ss.qi + 1 < len(ss.questions) else "See results →"
                st.button(label, key=f"next_{ss.qi}", type="primary", on_click=next_question, use_container_width=True)

# ──────────────────────────────────────────────────────────────────────────
# RESULTS (solo)
# ──────────────────────────────────────────────────────────────────────────
elif ss.screen == "results":
    total = len(ss.questions)
    acc = round((ss.correct_count / total) * 100) if total else 0
    verdict = "flawless run" if acc >= 85 else "solid round" if acc >= 60 else "room to grow"

    r1, r2 = st.columns([1.3, 1], gap="medium")
    with r1:
        with st.container(key="resultcard"):
            st.html(f"""
            <div style="width:74px;height:74px;margin:0 auto 12px;border-radius:26px;background:{SOFT};display:grid;place-items:center;font-size:34px">🏆</div>
            <div style="font-size:11.5px;font-weight:700;letter-spacing:.06em;text-transform:uppercase;color:{BRAND_DEEP}">Round complete</div>
            <div style="font-weight:800;font-size:60px;line-height:1;margin:6px 0 4px;color:{INK}">{ss.score}</div>
            <div style="font-size:13.5px;color:{INK_2};margin-bottom:18px">coins · {DATA.get(ss.cat, {}).get('name', 'Mixed Round')} · {verdict}</div>
            """)
            p1, p2 = st.columns(2)
            with p1:
                st.button("↻ Play again", key="again", type="primary",
                          on_click=start_category, args=(ss.cat,), use_container_width=True)
            with p2:
                st.button("Back to home", key="home", type="secondary", on_click=go_home, use_container_width=True)

    with r2:
        stats = [("Correct", f"{ss.correct_count}/{total}"), ("Accuracy", f"{acc}%"),
                 ("Best streak", str(ss.best_streak)), ("Coins", str(ss.score))]
        sc = st.columns(2)
        for i, (label, value) in enumerate(stats):
            with sc[i % 2]:
                st.html(f"""
                <div class="qw-stat" style="margin-bottom:12px">
                  <div class="v">{value}</div><div class="l">{label}</div>
                </div>
                """)

    st.write("")
    rows = "".join(f"""
    <div style="display:flex;align-items:center;gap:14px;padding:12px 0;border-bottom:1px solid {LINE}">
      <span style="flex:1;font-weight:600;font-size:14.5px">{topic}</span>
      <span style="width:34%;max-width:200px;height:8px;border-radius:5px;background:{LINE};overflow:hidden">
        <span style="display:block;height:100%;border-radius:5px;width:{int(100*c/t)}%;background:{BRAND}"></span>
      </span>
      <span style="width:52px;text-align:right;font-weight:700;font-size:13.5px;color:{INK_2}">{c}/{t}</span>
    </div>
    """ for topic, (c, t) in ss.topic_stats.items())
    st.html(f"""
    <div class="qw-card">
      <div style="display:flex;justify-content:space-between;margin-bottom:8px">
        <h5 style="margin:0;font-size:18px">Topic breakdown</h5>
        <span style="font-size:12.5px;color:{INK_3}">{ss.correct_count} of {total} correct</span>
      </div>
      {rows}
    </div>
    """)

# ──────────────────────────────────────────────────────────────────────────
# WINNER (teams)
# ──────────────────────────────────────────────────────────────────────────
elif ss.screen == "winner":
    t0, t1 = ss.teams
    if t0["score"] == t1["score"]:
        winner_title, winner_line, winner_sub = "It's a tie!", f"{t0['score']} to {t1['score']}", "Dead level. Run a tiebreak round."
        win_idx = None
    else:
        win_idx = 0 if t0["score"] > t1["score"] else 1
        lose_idx = 1 - win_idx
        winner_title = f"{ss.teams[win_idx]['name']} wins!"
        winner_line = f"{ss.teams[win_idx]['score']} to {ss.teams[lose_idx]['score']}"
        winner_sub = f"Won by {abs(t0['score'] - t1['score'])} coins over {len(ss.questions)} questions."

    with st.container(key="resultcard"):
        st.html(f"""
        <div style="width:84px;height:84px;margin:0 auto 14px;border-radius:30px;background:{SOFT};display:grid;place-items:center;font-size:40px">👑</div>
        <div style="font-size:11.5px;font-weight:700;letter-spacing:.06em;text-transform:uppercase;color:{BRAND_DEEP}">Match over</div>
        <h2 style="margin:6px 0 4px;font-size:38px">{winner_title}</h2>
        <div style="font-weight:800;font-size:48px;line-height:1.05;color:{INK}">{winner_line}</div>
        <p style="margin:8px auto 20px;font-size:14px;color:{INK_2};max-width:46ch">{winner_sub}</p>
        """)
        p1, p2 = st.columns(2)
        with p1:
            st.button("↻ Rematch", key="rematch", type="primary",
                      on_click=start_category, args=(ss.cat,), use_container_width=True)
        with p2:
            st.button("Back to home", key="home_w", type="secondary", on_click=go_home, use_container_width=True)

    st.write("")
    cols = st.columns(2, gap="medium")
    for i, t in enumerate(ss.teams):
        is_winner = win_idx == i
        crown = "👑" if is_winner else "🎗️"
        with cols[i]:
            st.html(f"""
            <div class="qw-card" style="text-align:center">
              <div style="font-size:24px">{crown}</div>
              <div style="font-weight:800;font-size:19px;margin-top:4px">{t['name']}</div>
              <div style="font-weight:800;font-size:32px;line-height:1;margin-top:2px">{t['score']}</div>
              <div style="font-size:12.5px;color:{INK_2}">{t['correct']} correct</div>
            </div>
            """)
