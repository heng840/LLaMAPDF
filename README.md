# LLaMAPDF

LLaMAPDF is a project designed to enable LLaMA2 and other large language models (LLMs) with limited input length to process longer texts, such as PDF documents.

## Problem Statement

Many LLMs, including LLaMA2, have a restricted input length, which makes it challenging to process lengthy documents like academic papers in PDF format. This limitation hinders the ability to perform comprehensive analysis or question-answering tasks on full documents.

## Solution

LLaMAPDF addresses this issue by implementing a method to enable LLaMA2 to read and process longer texts within its limited context window. This allows for more effective handling of PDF documents, such as ACL (Association for Computational Linguistics) papers.

## Features

- Extends LLaMA2's ability to process longer texts
- Supports PDF document input
- Optimized for academic papers and similar long-form content

## Installation

To install LLaMAPDF, follow these steps:

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/LLaMAPDF.git
   cd LLaMAPDF
   ```

2. Download and set up the LLaMA2 model (follow instructions on the official LLaMA2 repository).

## Usage

Here's a basic example of how to use LLaMAPDF:

```python
from llamapdf import PDFParser, LLaMAExtender

# Initialize the PDF parser
pdf_parser = PDFParser()

# Parse a PDF file
parsed_content = pdf_parser.parse("path/to/your/document.pdf")

# Initialize the LLaMA extender
llama_extender = LLaMAExtender()

# Process the parsed content
result = llama_extender.process(parsed_content)

# Now you can use the result with your LLaMA2 model
# ...
```

## How It Works

LLaMAPDF uses two main components to enable processing of longer texts:

1. PDF_parser: This component processes PDF files, extracting the text content and maintaining the structure of the document. It handles various PDF formats and ensures that the extracted text is clean and ready for processing.

2. Adaptive Hierarchical Sliding Window: This is the key technology in LLaMAPDF that extends the effective window length of the LLaMA2 model. Here's how it works:

   a. Adaptive Chunking:
      - The document is divided into chunks based on content structure (e.g., paragraphs, sections) rather than fixed sizes.
      - This ensures that contextual units remain intact.

   b. First-Level Processing:
      - Each chunk is processed individually by LLaMA2, but with overlap from adjacent chunks.
      - For example, if LLaMA2's max input is 2048 tokens, we might use chunks of ~1500 tokens with 500-token overlaps.

   c. Hierarchical Summarization:
      - The output from each first-level chunk is summarized.
      - These summaries are then combined into larger, second-level chunks.

   d. Second-Level Processing:
      - The second-level chunks (consisting of first-level summaries) are processed by LLaMA2.
      - This allows the model to capture long-range dependencies and global context.

   e. Intelligent Combination:
      - Results from overlapping regions are combined using a weighted average based on token position.
      - A small "combiner" model (e.g., a fine-tuned BERT model) is used to select the most coherent transitions between non-overlapping sections.
      - Details:

   f. Final Synthesis:
      - The second-level output is used to guide the combination of the detailed first-level outputs.
      - This produces a coherent final output that maintains both local details and global context.

This Adaptive Hierarchical Sliding Window approach allows LLaMAPDF to process documents that are much longer than LLaMA2's native maximum input length while maintaining context and coherence throughout the document. It balances the need for detailed local processing with the capture of long-range dependencies.

Key advantages of this approach:
1. Preserves important contextual units through adaptive chunking.
2. Captures both local details and global context through hierarchical processing.
3. Maintains coherence across the entire document length.
4. Adapts to different types of documents and content structures.


## Limitations

While LLaMAPDF significantly extends LLaMA2's ability to process longer texts, it does have some limitations:

1. Processing Time: Due to the chunking and recombining process, processing very long documents can be time-consuming.
2. Memory Usage: Depending on the document size, the process may require significant memory.
3. Context Boundaries: While the overlapping window approach mitigates this, there might still be some loss of context at the boundaries between chunks.
4. PDF Complexity: Highly complex PDFs with intricate layouts or embedded elements may not be parsed perfectly.
5. Model Limitations: The final output quality is still dependent on the underlying LLaMA2 model's capabilities.

We are continuously working on improving these aspects and welcome contributions from the community.
