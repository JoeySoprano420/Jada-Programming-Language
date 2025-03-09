from docx import Document

def extract_text(docx_file):
    """Extracts text from the given DOCX file."""
    doc = Document(docx_file)
    full_text = []
    for para in doc.paragraphs:
        full_text.append(para.text)
    return '\n'.join(full_text)

# Path to the document containing the dataset
dataset_path = "C:\\Users\\420up\\OneDrive\\Documents\\J_ADA_Programming_Language.docx"
dataset = extract_text(dataset_path)

from sklearn.cluster import KMeans
import numpy as np

def unsupervised_learning(data, num_clusters=5):
    """Performs unsupervised learning on the dataset using KMeans clustering."""
    # Tokenize and vectorize dataset (simplified)
    vectorized_data = np.array([len(line.split()) for line in data.splitlines()])  # Simple vectorization by word length
    kmeans = KMeans(n_clusters=num_clusters, random_state=42)
    kmeans.fit(vectorized_data.reshape(-1, 1))
    return kmeans

# Train unsupervised model on dataset
unsupervised_model = unsupervised_learning(dataset)

from _7FSEN import FSEN, ContextualNetwork

# Define a Virtual Machine class with integrated 7-FSEN
class LearningVirtualMachine:
    def __init__(self, language_data):
        self.language_data = language_data
        self.context = ContextualNetwork()
        self.fsen_system = FSEN()  # Feedback system for evolving reasoning
        self.execution_engine = CodeInterpreter(language_data)

    def query_and_learn(self, query):
        """Process a query and learn from the result."""
        result = self.process_query(query)
        self.fsen_system.process_feedback(result)  # Learn from the feedback
        return result

    def process_query(self, query):
        """Simulate processing of a query (interpretation step)."""
        response = self.execution_engine.execute(query)
        return response

class CodeInterpreter:
    def __init__(self, language_data):
        self.language_data = language_data
        self.context = {}

    def execute(self, code):
        """Execute code in J-Ada."""
        if "print" in code:
            return self._execute_print(code)
        elif "define" in code:
            return self._execute_define(code)
        else:
            return "Code execution logic for J-Ada goes here."

    def _execute_print(self, code):
        """Simulate print functionality."""
        return code.replace("print", "").strip()

    def _execute_define(self, code):
        """Simulate defining variables in J-Ada."""
        definition = code.replace("define", "").strip()
        variable, value = definition.split("=")
        self.context[variable.strip()] = value.strip()
        return f"Defined {variable.strip()} = {value.strip()}"

class VirtualMachineWithLearning:
    def __init__(self, language_data):
        self.language_data = language_data
        self.execution_engine = CodeInterpreter(language_data)
        self.fsen_system = FSEN()  # For feedback and learning

    def process_and_learn(self, code_input):
        """Execute the code input through the interpreter and learn from the execution result."""
        execution_result = self.execution_engine.execute(code_input)
        
        # Send the execution result to FSEN for further learning
        self.fsen_system.process_feedback(execution_result)
        
        return execution_result

# Create an instance of the VM with learning capabilities
vm = VirtualMachineWithLearning(dataset)

# Example of running and learning from code
code_input = "print Hello, World!"
execution_output = vm.process_and_learn(code_input)
print(execution_output)

# Example of defining a variable
define_input = "define x = 10"
execution_output = vm.process_and_learn(define_input)
print(execution_output)

# Example of dynamic input from user
user_input = input("Enter J-Ada code: ")
execution_output = vm.process_and_learn(user_input)
print(f"Execution Output: {execution_output}")

# Feedback System to improve reasoning over time
class FSEN:
    def __init__(self):
        self.memory = {}

    def process_feedback(self, feedback):
        """Process feedback to improve reasoning over time."""
        # Simulating by just storing the feedback
        self.memory["last_feedback"] = feedback
        print(f"Learning from feedback: {feedback}")

# Example of the feedback process
vm.fsen_system.process_feedback("Executed: print Hello, World!")
