# Design

As mentioned in the requirements section, this application is expected to analyze resumes for keywords, quantifications, grammar, and ATS compatibility. For an AI-powered application, Python is the optimal programming language due to its readable syntax and vast collection of AI/ML libraries.

### Libraries
The following libraries are expected to be used in the application. Each library serves a specific purpose. Other libraries may be used in their place depending on app performance and future optimization.

- **pdfminer.six:** Extract layout and text from resume PDF uploads
- **PyMuPDF:** Analyze font styles in PDF to optimize resumes for ATS 
- **NLTK (Natural Language ToolKit):** AI library that handles raw text through the follow processes: Tokenization, Lemmatization, POS-tagging. May switch to spaCy when scaling application as it is faster and more resourceful than NLTK
- **streamlit:** Develop web UI prototypes rapidly with more emphasis on AI-based development. May use NodeJS to enhance web UI

### Data Flow
The [data flow](../docs/AI_Resume_Analyzer_DFD.png) diagram represents how the resume analyzer will handle the analysis process. Resumes and job descriptions will be stored in memory. Future renditions of this app may store both in databases to provide more accurate suggestions using TF-IDF.
