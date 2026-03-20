QUESTIONS = [
    {
        "question": "What does NLP stand for?",
        "options": [
            "Neural Learning Process",
            "Natural Language Processing",
            "Normalized Linear Projection",
            "Network Layer Protocol"
        ],
        "answer": "Natural Language Processing",
        "category": "AI & NLP",
        "difficulty": "Easy",
        "explanation": "NLP (Natural Language Processing) is a field of AI focused on enabling computers to understand, interpret, and generate human language — powering applications like chatbots, translation, and sentiment analysis."
    },
    {
        "question": "What is a Large Language Model (LLM)?",
        "options": [
            "A database of linguistic rules",
            "A model trained on massive text data to understand and generate language",
            "A model that only classifies text into categories",
            "A search engine with language capabilities"
        ],
        "answer": "A model trained on massive text data to understand and generate language",
        "category": "AI & NLP",
        "difficulty": "Easy",
        "explanation": "LLMs (like GPT-4, Claude, Gemini) are Transformer-based models trained on billions of text tokens via next-token prediction. They develop emergent abilities in reasoning, summarization, coding, and conversation."
    },
    {
        "question": "What does 'tokenization' mean in NLP?",
        "options": [
            "Converting numerical data to text",
            "Splitting text into smaller units (tokens) for processing",
            "Encrypting text for secure transmission",
            "Translating text between languages"
        ],
        "answer": "Splitting text into smaller units (tokens) for processing",
        "category": "AI & NLP",
        "difficulty": "Easy",
        "explanation": "Tokenization breaks text into tokens — words, subwords, or characters — that a model can process numerically. Modern LLMs use subword tokenization (BPE, SentencePiece) to balance vocabulary size and coverage."
    },
    {
        "question": "What is the difference between semantic search and keyword search?",
        "options": [
            "Keyword search is faster; semantic search only works on images",
            "Semantic search understands meaning and context; keyword search matches exact terms",
            "Semantic search only works for short queries; keyword search handles long documents",
            "They are the same but keyword search is older"
        ],
        "answer": "Semantic search understands meaning and context; keyword search matches exact terms",
        "category": "AI & NLP",
        "difficulty": "Medium",
        "explanation": "Keyword search (BM25, TF-IDF) matches literal terms. Semantic search uses embeddings to find conceptually similar content even without exact word matches — e.g., finding 'car' when querying 'automobile'."
    },
    {
        "question": "What is prompt engineering?",
        "options": [
            "Writing code to fine-tune language models",
            "Designing inputs to LLMs to guide their outputs effectively",
            "Converting prompts from one language to another",
            "Compressing long prompts to save tokens"
        ],
        "answer": "Designing inputs to LLMs to guide their outputs effectively",
        "category": "AI & NLP",
        "difficulty": "Medium",
        "explanation": "Prompt engineering involves crafting, structuring, and iterating on inputs to LLMs (using techniques like chain-of-thought, few-shot examples, role specification) to elicit more accurate, relevant, and well-formatted responses."
    },
    {
        "question": "What is RAG (Retrieval-Augmented Generation)?",
        "options": [
            "A method to compress LLM weights",
            "Generating data for model training using retrieval systems",
            "Combining retrieval from a knowledge base with LLM generation",
            "A fine-tuning technique for domain adaptation"
        ],
        "answer": "Combining retrieval from a knowledge base with LLM generation",
        "category": "AI & NLP",
        "difficulty": "Medium",
        "explanation": "RAG retrieves relevant documents from an external knowledge base at query time and injects them into the LLM's context, allowing the model to answer questions grounded in up-to-date or domain-specific information without retraining."
    },
    {
        "question": "In the attention mechanism, what do Q, K, and V represent?",
        "options": [
            "Quantization, Kernel, and Value layers",
            "Query, Key, and Value projections of the input",
            "Queue, Knowledge, and Vocabulary matrices",
            "Quality, Kernel, and Vector embeddings"
        ],
        "answer": "Query, Key, and Value projections of the input",
        "category": "AI & NLP",
        "difficulty": "Hard",
        "explanation": "In self-attention, the input is projected into Queries (what we're looking for), Keys (what each position offers), and Values (what to return). Attention scores are computed as softmax(QK^T / sqrt(d_k)) x V, allowing dynamic focus on relevant positions."
    },
    {
        "question": "What is RLHF (Reinforcement Learning from Human Feedback) used for in LLMs?",
        "options": [
            "To pre-train models on large text corpora",
            "To align model outputs with human preferences and safety guidelines",
            "To compress model weights for faster inference",
            "To translate models between different languages"
        ],
        "answer": "To align model outputs with human preferences and safety guidelines",
        "category": "AI & NLP",
        "difficulty": "Hard",
        "explanation": "RLHF trains a reward model from human preference comparisons, then uses RL (typically PPO) to fine-tune the LLM to maximize this reward. It's used to make models more helpful, harmless, and honest — as used in InstructGPT and Claude."
    },
    {
        "question": "What is a word embedding?",
        "options": [
            "A technique to remove stop words from text",
            "A dense numerical vector representing a word in a continuous space",
            "A dictionary mapping words to their definitions",
            "A method for counting word frequencies in a corpus"
        ],
        "answer": "A dense numerical vector representing a word in a continuous space",
        "category": "AI & NLP",
        "difficulty": "Easy",
        "explanation": "Word embeddings (Word2Vec, GloVe, FastText) map words to dense vectors where semantically similar words are close in vector space. They capture meaning and analogies (king - man + woman = queen) and are foundational input representations for NLP models."
    },
    {
        "question": "What does the term 'context window' mean in LLMs?",
        "options": [
            "The size of the GPU memory available",
            "The maximum number of tokens the model can consider at once",
            "The number of layers in the transformer",
            "The amount of data used for fine-tuning"
        ],
        "answer": "The maximum number of tokens the model can consider at once",
        "category": "AI & NLP",
        "difficulty": "Easy",
        "explanation": "The context window defines how many tokens (input + output) the model can process in a single forward pass. Longer context windows allow handling long documents and multi-turn conversations but require more memory and compute."
    },
    {
        "question": "What is sentiment analysis?",
        "options": [
            "Identifying the language a text is written in",
            "Determining the emotional tone (positive, negative, neutral) of text",
            "Extracting named entities such as persons and locations",
            "Generating a summary of a long document"
        ],
        "answer": "Determining the emotional tone (positive, negative, neutral) of text",
        "category": "AI & NLP",
        "difficulty": "Easy",
        "explanation": "Sentiment analysis classifies text by its expressed emotion — commonly positive, negative, or neutral. It powers product review analysis, social media monitoring, and customer feedback tools, and can be fine-grained (star ratings) or binary."
    },
    {
        "question": "What is the difference between BERT and GPT architectures?",
        "options": [
            "BERT is larger than GPT in parameter count",
            "BERT uses a bidirectional (encoder-only) Transformer; GPT uses a left-to-right (decoder-only) Transformer",
            "GPT was trained on images; BERT on text",
            "They are architecturally identical but trained on different datasets"
        ],
        "answer": "BERT uses a bidirectional (encoder-only) Transformer; GPT uses a left-to-right (decoder-only) Transformer",
        "category": "AI & NLP",
        "difficulty": "Medium",
        "explanation": "BERT (encoder-only) sees all tokens simultaneously using masked language modeling, making it excellent for understanding tasks (classification, NER, QA). GPT (decoder-only) is autoregressive — predicting the next token left-to-right — making it optimal for generation tasks."
    },
    {
        "question": "What is named entity recognition (NER)?",
        "options": [
            "Classifying the sentiment of each sentence in a document",
            "Identifying and categorizing real-world entities (persons, organizations, locations) in text",
            "Parsing sentence structure into a syntactic tree",
            "Resolving coreferences between pronouns and nouns"
        ],
        "answer": "Identifying and categorizing real-world entities (persons, organizations, locations) in text",
        "category": "AI & NLP",
        "difficulty": "Medium",
        "explanation": "NER is a sequence labeling task that tags spans of text with entity types such as PERSON, ORG, GPE, DATE, and MONEY. It is a core building block for information extraction, knowledge graph construction, and question answering."
    },
    {
        "question": "What is the purpose of positional encoding in Transformers?",
        "options": [
            "To encode the semantic meaning of each word",
            "To inject information about token positions since self-attention is order-agnostic",
            "To normalize the attention scores across heads",
            "To project the input tokens into a higher-dimensional space"
        ],
        "answer": "To inject information about token positions since self-attention is order-agnostic",
        "category": "AI & NLP",
        "difficulty": "Medium",
        "explanation": "Self-attention treats all positions identically. Positional encodings (sinusoidal or learned) are added to token embeddings to give the model information about token order, enabling it to distinguish 'dog bites man' from 'man bites dog'."
    },
    {
        "question": "What is TF-IDF used for?",
        "options": [
            "Training a language model on unlabeled text",
            "Weighting words by their importance in a document relative to a corpus",
            "Splitting text into sentences for processing",
            "Generating embeddings for downstream tasks"
        ],
        "answer": "Weighting words by their importance in a document relative to a corpus",
        "category": "AI & NLP",
        "difficulty": "Medium",
        "explanation": "TF-IDF (Term Frequency-Inverse Document Frequency) scores words highly if they appear often in a document (TF) but rarely across the corpus (IDF), capturing uniqueness. It is a strong baseline for information retrieval and text classification."
    },
    {
        "question": "What is the purpose of multi-head attention in Transformers?",
        "options": [
            "To run multiple Transformer models in parallel",
            "To allow the model to jointly attend to information from different representation subspaces at different positions",
            "To increase the depth of the Transformer encoder",
            "To separately encode syntax and semantics in different attention layers"
        ],
        "answer": "To allow the model to jointly attend to information from different representation subspaces at different positions",
        "category": "AI & NLP",
        "difficulty": "Hard",
        "explanation": "Multi-head attention runs h parallel attention operations with different learned projections, then concatenates and projects the results. Each head can specialize in different aspects (syntactic roles, coreference, local/global dependencies), enriching the representation beyond a single attention function."
    },
    {
        "question": "What is byte-pair encoding (BPE) tokenization?",
        "options": [
            "Encoding each character as a single byte for efficiency",
            "An iterative algorithm that merges the most frequent character pairs to build a subword vocabulary",
            "A method that tokenizes text by whitespace only",
            "A lossless compression applied to model weights"
        ],
        "answer": "An iterative algorithm that merges the most frequent character pairs to build a subword vocabulary",
        "category": "AI & NLP",
        "difficulty": "Hard",
        "explanation": "BPE starts with a character vocabulary and repeatedly merges the most frequent adjacent token pairs until the desired vocabulary size is reached. This produces subword tokens that balance vocabulary size with the ability to handle rare or unknown words — used in GPT-2, RoBERTa, and many modern LLMs."
    },
    {
        "question": "What does 'temperature' control in LLM text generation?",
        "options": [
            "The maximum length of the generated response",
            "The randomness of the probability distribution when sampling next tokens",
            "The speed at which tokens are generated",
            "The number of transformer layers activated during inference"
        ],
        "answer": "The randomness of the probability distribution when sampling next tokens",
        "category": "AI & NLP",
        "difficulty": "Hard",
        "explanation": "Temperature T divides logits before softmax. T < 1 sharpens the distribution (more deterministic), T > 1 flattens it (more random and diverse). Temperature 0 is greedy decoding. Higher temperature increases creativity at the cost of coherence."
    },
    {
        "question": "What is machine translation in NLP?",
        "options": [
            "Converting speech to text automatically",
            "Automatically translating text from one human language to another",
            "Translating programming code from one language to another",
            "Parsing a sentence into its grammatical components"
        ],
        "answer": "Automatically translating text from one human language to another",
        "category": "AI & NLP",
        "difficulty": "Easy",
        "explanation": "Machine translation (MT) uses AI models to automatically convert text between languages. Modern neural MT systems (like Google Translate, DeepL) are based on sequence-to-sequence Transformer architectures and have significantly outperformed earlier statistical methods."
    },
    {
        "question": "What is a chatbot?",
        "options": [
            "A robot that physically interacts with customers",
            "A software application designed to simulate conversation with humans",
            "A tool that only answers predefined FAQ questions from a database",
            "A browser plugin that autocompletes text fields"
        ],
        "answer": "A software application designed to simulate conversation with humans",
        "category": "AI & NLP",
        "difficulty": "Easy",
        "explanation": "Chatbots use NLP (and increasingly LLMs) to understand user inputs and generate responses. They range from simple rule-based systems to advanced AI assistants capable of multi-turn dialogue, reasoning, and task completion."
    },
    {
        "question": "What is text summarization?",
        "options": [
            "Converting text into numerical vectors",
            "Automatically producing a shorter version of a document that preserves key information",
            "Classifying a document into predefined categories",
            "Detecting the language of an input text"
        ],
        "answer": "Automatically producing a shorter version of a document that preserves key information",
        "category": "AI & NLP",
        "difficulty": "Easy",
        "explanation": "Text summarization can be extractive (selecting key sentences) or abstractive (generating new text). Modern LLMs excel at abstractive summarization, condensing long articles, reports, or conversations into concise, readable summaries."
    },
    {
        "question": "What does 'zero-shot learning' mean in the context of LLMs?",
        "options": [
            "Training a model with zero labeled examples",
            "The model performing a task it was never explicitly trained on, guided only by a natural language description",
            "Running inference without using GPU acceleration",
            "Generating outputs with temperature set to zero"
        ],
        "answer": "The model performing a task it was never explicitly trained on, guided only by a natural language description",
        "category": "AI & NLP",
        "difficulty": "Medium",
        "explanation": "Zero-shot prompting instructs the LLM to perform a task using only a description, with no examples. Large pretrained models generalize well zero-shot because they develop broad task understanding during pretraining — e.g., 'Translate this sentence to French: ...'."
    },
    {
        "question": "What is fine-tuning in the context of NLP models?",
        "options": [
            "Training a model from scratch on a new dataset",
            "Adjusting a pretrained model's weights on a task-specific dataset to improve performance",
            "Reducing the number of parameters in a model",
            "Changing the tokenizer vocabulary of a model"
        ],
        "answer": "Adjusting a pretrained model's weights on a task-specific dataset to improve performance",
        "category": "AI & NLP",
        "difficulty": "Medium",
        "explanation": "Fine-tuning starts with a pretrained model (e.g., BERT, GPT) and continues training on labeled domain-specific data. It adapts the model to tasks like sentiment analysis, legal document classification, or medical QA with far less data than training from scratch."
    },
    {
        "question": "What is the Transformer architecture primarily based on?",
        "options": [
            "Recurrent neural networks with gating mechanisms",
            "Convolutional neural networks applied to text sequences",
            "Self-attention mechanisms without recurrence or convolution",
            "Markov chain models with neural network scoring"
        ],
        "answer": "Self-attention mechanisms without recurrence or convolution",
        "category": "AI & NLP",
        "difficulty": "Medium",
        "explanation": "Introduced in 'Attention Is All You Need' (2017), the Transformer replaces RNNs and CNNs with stacked self-attention and feed-forward layers. This allows massive parallelization during training and enables models to capture long-range dependencies efficiently."
    },
    {
        "question": "What is coreference resolution in NLP?",
        "options": [
            "Identifying synonyms in a sentence",
            "Determining which words or phrases refer to the same real-world entity in a text",
            "Linking named entities to entries in a knowledge base",
            "Detecting repeated sentences across a document"
        ],
        "answer": "Determining which words or phrases refer to the same real-world entity in a text",
        "category": "AI & NLP",
        "difficulty": "Medium",
        "explanation": "Coreference resolution clusters mentions (e.g., 'Alice', 'she', 'the engineer') that refer to the same entity. It is essential for document understanding, information extraction, and reading comprehension tasks where tracking entity identity across sentences is required."
    },
    {
        "question": "What is the purpose of layer normalization in Transformer models?",
        "options": [
            "To reduce the number of parameters in each layer",
            "To stabilize training by normalizing activations across the feature dimension",
            "To enforce sparsity in the attention weights",
            "To scale the output of each attention head independently"
        ],
        "answer": "To stabilize training by normalizing activations across the feature dimension",
        "category": "AI & NLP",
        "difficulty": "Hard",
        "explanation": "Layer normalization (LayerNorm) normalizes each token's representation across its feature dimensions, centering and scaling activations. This combats vanishing/exploding gradients and allows stable training of very deep Transformers, and is typically applied before (pre-norm) or after (post-norm) each sub-layer."
    },
    {
        "question": "What is the 'hallucination' problem in LLMs?",
        "options": [
            "The model generating text with very high confidence at all times",
            "The model producing plausible-sounding but factually incorrect or fabricated information",
            "The model repeating the same sentence in a loop",
            "The model refusing to answer certain types of questions"
        ],
        "answer": "The model producing plausible-sounding but factually incorrect or fabricated information",
        "category": "AI & NLP",
        "difficulty": "Medium",
        "explanation": "LLMs hallucinate because they are trained to produce fluent, coherent text rather than verified facts. They may confidently state wrong dates, fabricate citations, or invent entities. Mitigation strategies include RAG, grounding, and improved RLHF alignment."
    },
    {
        "question": "What is a language model perplexity score?",
        "options": [
            "A measure of how confused users are by the model's output",
            "A metric measuring how well a probability model predicts a sample, based on entropy",
            "The ratio of correct answers to total questions in a benchmark",
            "The average number of tokens generated per second"
        ],
        "answer": "A metric measuring how well a probability model predicts a sample, based on entropy",
        "category": "AI & NLP",
        "difficulty": "Hard",
        "explanation": "Perplexity = 2^H where H is the cross-entropy of the model on a test corpus. Lower perplexity means the model assigns higher probability to the actual text, indicating better language modeling. It is the standard intrinsic evaluation metric for language models."
    },
    {
        "question": "What is dependency parsing in NLP?",
        "options": [
            "Determining the language a sentence is written in",
            "Analyzing grammatical structure by identifying relationships between words in a sentence",
            "Splitting a document into individual sentences",
            "Grouping semantically similar sentences together"
        ],
        "answer": "Analyzing grammatical structure by identifying relationships between words in a sentence",
        "category": "AI & NLP",
        "difficulty": "Medium",
        "explanation": "Dependency parsing produces a tree where each word is connected to its syntactic head via a labeled arc (e.g., subject, object, modifier). It captures grammatical relations and is used in information extraction, question answering, and semantic role labeling."
    },
    {
        "question": "What is the role of the feed-forward network (FFN) layer in a Transformer block?",
        "options": [
            "It computes attention scores between all token pairs",
            "It applies a position-wise nonlinear transformation to each token's representation independently",
            "It projects the output of all attention heads into a single vector",
            "It encodes positional information into the token embeddings"
        ],
        "answer": "It applies a position-wise nonlinear transformation to each token's representation independently",
        "category": "AI & NLP",
        "difficulty": "Hard",
        "explanation": "Each Transformer block contains an FFN applied identically and independently to each token position. Typically two linear layers with a nonlinearity (ReLU or GELU) in between, the FFN expands the dimension (often 4x) then projects back. It acts as a key-value memory and accounts for roughly two-thirds of total parameters in large models."
    },
    {
        "question": "What is few-shot prompting?",
        "options": [
            "Training a model on a very small labeled dataset",
            "Providing a small number of input-output examples in the prompt to guide model behavior",
            "Running inference with a reduced model size",
            "A technique that limits the model to generating short responses"
        ],
        "answer": "Providing a small number of input-output examples in the prompt to guide model behavior",
        "category": "AI & NLP",
        "difficulty": "Easy",
        "explanation": "Few-shot prompting includes several demonstrations (e.g., 2-5 examples) directly in the context before the actual query. This in-context learning technique significantly improves performance on classification, translation, and reasoning tasks without updating model weights."
    },
    {
        "question": "What is chain-of-thought (CoT) prompting?",
        "options": [
            "Linking multiple LLM API calls sequentially in a pipeline",
            "Prompting the model to reason step-by-step before producing a final answer",
            "Feeding the output of one model as input to another model",
            "A retrieval technique that chains multiple documents together"
        ],
        "answer": "Prompting the model to reason step-by-step before producing a final answer",
        "category": "AI & NLP",
        "difficulty": "Medium",
        "explanation": "Chain-of-thought prompting elicits intermediate reasoning steps by including examples with explicit reasoning traces or by adding 'Let's think step by step.' This dramatically improves performance on arithmetic, commonsense, and symbolic reasoning tasks in large models."
    },
    {
        "question": "What is instruction tuning in LLMs?",
        "options": [
            "Training a model using only programming instructions as data",
            "Fine-tuning a pretrained LLM on diverse task instructions to follow human directions",
            "A hardware optimization technique for faster inference",
            "Reducing model size by removing instruction-following layers"
        ],
        "answer": "Fine-tuning a pretrained LLM on diverse task instructions to follow human directions",
        "category": "AI & NLP",
        "difficulty": "Medium",
        "explanation": "Instruction tuning (used in FLAN, InstructGPT, and others) fine-tunes LLMs on datasets of (instruction, response) pairs across many task types. It significantly improves the model's ability to follow natural language instructions zero-shot, making models more useful as general-purpose assistants."
    },
    {
        "question": "What is the primary training objective of BERT?",
        "options": [
            "Next token prediction on a large text corpus",
            "Masked language modeling and next sentence prediction",
            "Minimizing perplexity on a held-out validation set",
            "Contrastive learning between positive and negative sentence pairs"
        ],
        "answer": "Masked language modeling and next sentence prediction",
        "category": "AI & NLP",
        "difficulty": "Medium",
        "explanation": "BERT is pretrained using Masked Language Modeling (MLM), where 15% of tokens are randomly masked and the model predicts them using bidirectional context, and Next Sentence Prediction (NSP), which teaches the model sentence relationships. MLM is the more impactful objective."
    },
    {
        "question": "What does 'grounding' mean in the context of LLMs?",
        "options": [
            "Reducing the model's vocabulary to a core set of common words",
            "Connecting model outputs to verifiable external facts or sources",
            "Preventing the model from generating unsafe content",
            "Quantizing model weights to reduce memory usage"
        ],
        "answer": "Connecting model outputs to verifiable external facts or sources",
        "category": "AI & NLP",
        "difficulty": "Medium",
        "explanation": "Grounding ensures that LLM responses are anchored to external, verifiable sources (documents, databases, search results) rather than relying solely on parametric memory. It reduces hallucination and is a core motivation behind RAG and tool-augmented language models."
    },
    {
        "question": "What is model quantization in the context of LLMs?",
        "options": [
            "Converting a model's training data into numerical format",
            "Reducing the bit precision of model weights to decrease memory and increase speed",
            "Splitting a large model across multiple GPUs",
            "Measuring a model's performance on quantitative benchmarks"
        ],
        "answer": "Reducing the bit precision of model weights to decrease memory and increase speed",
        "category": "AI & NLP",
        "difficulty": "Hard",
        "explanation": "Quantization reduces weight precision from FP32/FP16 to INT8 or INT4, drastically reducing model size and inference latency. Techniques like GPTQ and AWQ enable high-quality quantization of LLMs with minimal accuracy loss, making large models deployable on consumer hardware."
    },
    {
        "question": "What is the purpose of the softmax function in the attention mechanism?",
        "options": [
            "To normalize input embeddings to unit length",
            "To convert raw attention scores into a probability distribution that sums to one",
            "To apply nonlinearity between transformer layers",
            "To initialize model weights before training"
        ],
        "answer": "To convert raw attention scores into a probability distribution that sums to one",
        "category": "AI & NLP",
        "difficulty": "Hard",
        "explanation": "In attention, softmax is applied to the dot-product scores QK^T / sqrt(d_k) to produce attention weights that are non-negative and sum to 1. This lets the model weight how much to 'attend' to each position when computing the output as a weighted sum of Values."
    },
    {
        "question": "What is an AI agent in the context of LLMs?",
        "options": [
            "A human operator who monitors an LLM's outputs",
            "An LLM-powered system that can plan, use tools, and take actions to accomplish goals",
            "A specialized neural network for image recognition",
            "A rule-based chatbot with predefined decision trees"
        ],
        "answer": "An LLM-powered system that can plan, use tools, and take actions to accomplish goals",
        "category": "AI & NLP",
        "difficulty": "Medium",
        "explanation": "LLM agents extend language models with reasoning loops (ReAct, Plan-and-Execute), tool use (web search, code execution, APIs), and memory. They autonomously decompose complex goals into sub-tasks, execute steps, and adapt based on environment feedback."
    },
    {
        "question": "What is LoRA (Low-Rank Adaptation)?",
        "options": [
            "A technique for lossless compression of model weights",
            "A parameter-efficient fine-tuning method that adds small trainable rank-decomposition matrices",
            "A new attention mechanism that reduces quadratic complexity",
            "A regularization technique to prevent overfitting during fine-tuning"
        ],
        "answer": "A parameter-efficient fine-tuning method that adds small trainable rank-decomposition matrices",
        "category": "AI & NLP",
        "difficulty": "Hard",
        "explanation": "LoRA freezes the pretrained model weights and injects trainable low-rank matrices (A and B) into specific layers (typically attention projections), so the update delta_W = BA. This reduces trainable parameters by orders of magnitude while matching full fine-tuning performance — critical for adapting billion-parameter LLMs efficiently."
    },
    {
        "question": "What is the BLEU score used for in NLP?",
        "options": [
            "Evaluating the fluency of generated speech audio",
            "Measuring the similarity between machine-generated text and human reference translations",
            "Scoring how well a model understands sentiment",
            "Tracking training loss during language model pretraining"
        ],
        "answer": "Measuring the similarity between machine-generated text and human reference translations",
        "category": "AI & NLP",
        "difficulty": "Medium",
        "explanation": "BLEU (Bilingual Evaluation Understudy) computes n-gram precision between a model output and one or more reference texts, with a brevity penalty. It is the most widely used automatic metric in machine translation and has been adapted for other text generation tasks, though it has known limitations in capturing semantic quality."
    },
    {
        "question": "What is a recurrent neural network (RNN) limitation that Transformers were designed to address?",
        "options": [
            "RNNs cannot process text data of any kind",
            "RNNs process tokens sequentially, making parallelization difficult and struggling with long-range dependencies",
            "RNNs require labeled data while Transformers use unsupervised learning",
            "RNNs cannot be trained using backpropagation"
        ],
        "answer": "RNNs process tokens sequentially, making parallelization difficult and struggling with long-range dependencies",
        "category": "AI & NLP",
        "difficulty": "Medium",
        "explanation": "RNNs process sequences one token at a time, creating a bottleneck for parallelism and causing vanishing gradients that impede learning long-range dependencies. Transformers overcome this with self-attention, which connects all positions in O(1) steps and processes the full sequence in parallel."
    },
    {
        "question": "What is text classification in NLP?",
        "options": [
            "Generating labels for unlabeled images using text descriptions",
            "Assigning predefined categories or labels to text documents",
            "Translating text from formal to informal register",
            "Extracting the main topic sentence from each paragraph"
        ],
        "answer": "Assigning predefined categories or labels to text documents",
        "category": "AI & NLP",
        "difficulty": "Easy",
        "explanation": "Text classification assigns input text to one or more predefined categories — examples include spam detection, topic labeling, intent classification, and sentiment analysis. It is one of the most common NLP tasks, solvable with traditional ML (SVM, Naive Bayes) or modern fine-tuned Transformers."
    },
    {
        "question": "What is the difference between extractive and abstractive summarization?",
        "options": [
            "Extractive summarization only works for short texts; abstractive for long texts",
            "Extractive selects and copies existing sentences; abstractive generates new text paraphrasing the content",
            "Extractive uses neural networks; abstractive uses rule-based systems",
            "They produce identical summaries but via different computational paths"
        ],
        "answer": "Extractive selects and copies existing sentences; abstractive generates new text paraphrasing the content",
        "category": "AI & NLP",
        "difficulty": "Medium",
        "explanation": "Extractive summarization ranks and selects the most important sentences from the source. Abstractive summarization (used by modern LLMs) generates novel text that may not appear verbatim in the source, producing more fluent and concise summaries but requiring deeper language understanding."
    },
    {
        "question": "What is a vector database and why is it used with LLMs?",
        "options": [
            "A database optimized for storing and querying high-dimensional embedding vectors for similarity search",
            "A relational database that stores model weights as vectors",
            "A graph database that maps entity relationships in knowledge bases",
            "A distributed file system for storing large training corpora"
        ],
        "answer": "A database optimized for storing and querying high-dimensional embedding vectors for similarity search",
        "category": "AI & NLP",
        "difficulty": "Medium",
        "explanation": "Vector databases (Pinecone, Weaviate, Chroma, Qdrant) store embedding vectors and support fast approximate nearest-neighbor (ANN) search. In LLM pipelines — particularly RAG — documents are embedded and stored in a vector DB, then retrieved at query time by comparing query embeddings to stored ones."
    },
    {
        "question": "What does 'top-p' (nucleus) sampling control in LLM generation?",
        "options": [
            "The maximum number of tokens in the output",
            "The cumulative probability threshold for the set of tokens considered during sampling",
            "The penalty applied to repeated tokens in the output",
            "The number of candidate responses generated before selection"
        ],
        "answer": "The cumulative probability threshold for the set of tokens considered during sampling",
        "category": "AI & NLP",
        "difficulty": "Hard",
        "explanation": "Top-p (nucleus) sampling considers only the smallest set of tokens whose cumulative probability exceeds p. For example, p=0.9 means sampling from tokens covering the top 90% of the probability mass. It adapts the candidate pool dynamically per step, avoiding both truncation of valid options and sampling from very unlikely tokens."
    },
    {
        "question": "What is semantic role labeling (SRL)?",
        "options": [
            "Assigning sentiment polarity to each token in a sentence",
            "Identifying the predicate-argument structure of a sentence — who did what to whom",
            "Linking words to their corresponding entries in a thesaurus",
            "Detecting the topic or domain of a text document"
        ],
        "answer": "Identifying the predicate-argument structure of a sentence — who did what to whom",
        "category": "AI & NLP",
        "difficulty": "Hard",
        "explanation": "SRL labels semantic roles such as Agent (who performs the action), Patient (what is affected), Instrument, and Location relative to a predicate. For example, in 'Alice broke the window with a hammer,' Alice is Agent, the window is Patient, and the hammer is Instrument. SRL is useful for information extraction and QA."
    },
    {
        "question": "What is Constitutional AI (CAI)?",
        "options": [
            "A legal framework governing the deployment of AI systems",
            "A technique where AI models are trained to critique and revise their own outputs using a set of principles",
            "A hardware architecture designed to enforce AI safety constraints",
            "A dataset of human-written guidelines used in model pretraining"
        ],
        "answer": "A technique where AI models are trained to critique and revise their own outputs using a set of principles",
        "category": "AI & NLP",
        "difficulty": "Hard",
        "explanation": "Constitutional AI (Anthropic, 2022) trains models using a written set of principles (the 'constitution'). The model is prompted to evaluate and revise its own responses for harmlessness, then trained via RLHF on AI-generated preference data. It reduces reliance on human labelers for harmlessness feedback while improving alignment."
    },
    {
        "question": "What is speech recognition in AI?",
        "options": [
            "Generating synthetic speech from text input",
            "Automatically converting spoken audio into written text",
            "Identifying the speaker's emotional state from audio",
            "Translating spoken words between two languages in real time"
        ],
        "answer": "Automatically converting spoken audio into written text",
        "category": "AI & NLP",
        "difficulty": "Easy",
        "explanation": "Speech recognition (ASR — Automatic Speech Recognition) converts spoken language into text. Modern systems like Whisper, Google Speech-to-Text, and AWS Transcribe use deep learning (typically Transformer-based) to achieve near-human accuracy across languages and accents."
    },
    {
        "question": "What is the encoder-decoder architecture used for in NLP?",
        "options": [
            "Compressing model weights during deployment",
            "Mapping an input sequence to an output sequence, typically of different length",
            "Encoding images alongside text for multimodal tasks",
            "Splitting a large model into two independent halves for distributed inference"
        ],
        "answer": "Mapping an input sequence to an output sequence, typically of different length",
        "category": "AI & NLP",
        "difficulty": "Medium",
        "explanation": "Encoder-decoder (seq2seq) models encode an input sequence into a representation and then decode it into an output sequence. They are the backbone of machine translation, summarization, and question answering (e.g., T5, BART). The encoder builds context; the decoder generates the output token by token using cross-attention over encoder outputs."
    },
    {
        "question": "What is knowledge distillation in the context of NLP models?",
        "options": [
            "Extracting structured facts from unstructured text documents",
            "Training a smaller student model to mimic the behavior of a larger teacher model",
            "Storing domain-specific knowledge in a vector database for retrieval",
            "Compressing a model's vocabulary to reduce inference costs"
        ],
        "answer": "Training a smaller student model to mimic the behavior of a larger teacher model",
        "category": "AI & NLP",
        "difficulty": "Hard",
        "explanation": "Knowledge distillation transfers the 'dark knowledge' of a large teacher model (soft probability distributions, intermediate representations) to a compact student model. DistilBERT, for example, retains ~97% of BERT's performance at 60% of its size. It is widely used to deploy efficient models in production without significant accuracy loss."
    },
    {
        "question": "What does GPU stand for and why is it used for deep learning?",
        "options": [
            "General Processing Unit; it has a larger cache than CPUs",
            "Graphics Processing Unit; its thousands of small cores efficiently parallelize the matrix operations in neural networks",
            "Generative Processing Unit; it is specifically designed for AI workloads",
            "Graphics Processing Unit; it uses less power than CPUs during training"
        ],
        "answer": "Graphics Processing Unit; its thousands of small cores efficiently parallelize the matrix operations in neural networks",
        "category": "Cloud & Infrastructure",
        "difficulty": "Easy",
        "explanation": "GPUs were designed for parallel graphics rendering and contain thousands of small, efficient cores ideal for matrix multiplications — the dominant operation in deep learning. A modern GPU can be 10-100x faster than a CPU for neural network training."
    },
    {
        "question": "What is object storage (e.g., Amazon S3)?",
        "options": [
            "A file system mounted on a virtual machine",
            "A relational database optimized for storing objects",
            "A highly scalable service that stores data as objects (files) with unique keys, accessible via HTTP",
            "An in-memory cache for frequently accessed data"
        ],
        "answer": "A highly scalable service that stores data as objects (files) with unique keys, accessible via HTTP",
        "category": "Cloud & Infrastructure",
        "difficulty": "Easy",
        "explanation": "Object storage (S3, GCS, Azure Blob) stores arbitrary files as immutable objects with a unique key. It is infinitely scalable, cheap for large volumes, and the standard for storing raw data, model artifacts, training datasets, and ML outputs in cloud pipelines."
    },
    {
        "question": "What is infrastructure-as-code (IaC)?",
        "options": [
            "Writing Python scripts to interact with cloud APIs",
            "Managing and provisioning infrastructure through declarative configuration files rather than manual setup",
            "Containerizing applications with Docker",
            "Monitoring cloud resource usage with dashboards"
        ],
        "answer": "Managing and provisioning infrastructure through declarative configuration files rather than manual setup",
        "category": "Cloud & Infrastructure",
        "difficulty": "Medium",
        "explanation": "IaC (Terraform, CloudFormation, Pulumi) defines infrastructure in code, enabling version control, repeatability, and automation. Instead of clicking through a console, you declare desired state and the IaC tool provisions or modifies resources to match — critical for reproducible ML infrastructure."
    },
    {
        "question": "What is Kubernetes used for in ML system deployments?",
        "options": [
            "Training neural networks on distributed GPU clusters",
            "Orchestrating containerized applications, managing scaling, self-healing, and rolling updates",
            "Storing and versioning machine learning datasets",
            "Providing a managed feature store for real-time inference"
        ],
        "answer": "Orchestrating containerized applications, managing scaling, self-healing, and rolling updates",
        "category": "Cloud & Infrastructure",
        "difficulty": "Medium",
        "explanation": "Kubernetes (K8s) automates deployment, scaling, and management of containerized workloads. In MLOps, it is used to serve ML models (with auto-scaling on traffic), run batch training jobs, and manage microservices — providing resilience and portability across cloud providers."
    },
    {
        "question": "What is the difference between horizontal and vertical scaling for ML serving?",
        "options": [
            "Horizontal scaling increases compute power of a single machine; vertical scaling adds more machines",
            "Horizontal scaling adds more machine instances; vertical scaling upgrades a single machine with more CPU/RAM/GPU",
            "They are identical for GPU-based workloads",
            "Horizontal scaling applies to training; vertical scaling applies to inference"
        ],
        "answer": "Horizontal scaling adds more machine instances; vertical scaling upgrades a single machine with more CPU/RAM/GPU",
        "category": "Cloud & Infrastructure",
        "difficulty": "Hard",
        "explanation": "Vertical scaling (scale up) increases resources on a single node — limited by hardware maximums and causes downtime. Horizontal scaling (scale out) adds more nodes — preferred for ML serving since it enables zero-downtime scaling and fault tolerance. Auto-scaling groups in cloud providers manage this dynamically based on traffic."
    },
    {
        "question": "What is a Docker container?",
        "options": [
            "A virtual machine running a full operating system",
            "A lightweight, portable, self-contained unit that packages an application and its dependencies",
            "A cloud storage bucket for model artifacts",
            "A type of GPU instance on AWS"
        ],
        "answer": "A lightweight, portable, self-contained unit that packages an application and its dependencies",
        "category": "Cloud & Infrastructure",
        "difficulty": "Easy",
        "explanation": "Docker containers encapsulate an application with all its dependencies (libraries, runtime, config) into a single image. This ensures 'it works on my machine' becomes 'it works everywhere,' making ML model deployment reproducible across dev, staging, and production environments."
    },
    {
        "question": "What is a content delivery network (CDN)?",
        "options": [
            "A distributed network of servers that caches content closer to end users to reduce latency",
            "A private fiber network connecting data centers",
            "A load balancer that routes traffic between cloud regions",
            "A DNS service for resolving domain names"
        ],
        "answer": "A distributed network of servers that caches content closer to end users to reduce latency",
        "category": "Cloud & Infrastructure",
        "difficulty": "Easy",
        "explanation": "CDNs (CloudFront, Fastly, Cloudflare) cache static assets at edge locations worldwide. For ML applications, CDNs can serve static model outputs, reduce API response latency for geographically distributed users, and offload traffic from origin servers."
    },
    {
        "question": "What is the purpose of a message queue (e.g., Apache Kafka, AWS SQS) in ML pipelines?",
        "options": [
            "To store training datasets in a structured format",
            "To decouple producers and consumers of data, enabling asynchronous processing and buffering",
            "To provide real-time feature lookups for inference",
            "To schedule periodic model retraining jobs"
        ],
        "answer": "To decouple producers and consumers of data, enabling asynchronous processing and buffering",
        "category": "Cloud & Infrastructure",
        "difficulty": "Medium",
        "explanation": "Message queues act as buffers between services. In ML pipelines, they decouple data ingestion from processing — if an inference service is slow, requests queue up instead of being dropped. Kafka also enables event streaming for real-time feature engineering and model monitoring."
    },
    {
        "question": "What is a spot instance (or preemptible VM) in cloud computing?",
        "options": [
            "A reserved instance with a 1-year commitment for guaranteed availability",
            "A spare compute capacity offered at steep discounts that can be reclaimed by the cloud provider with short notice",
            "A dedicated physical server not shared with other customers",
            "A burstable instance that can temporarily exceed its baseline CPU"
        ],
        "answer": "A spare compute capacity offered at steep discounts that can be reclaimed by the cloud provider with short notice",
        "category": "Cloud & Infrastructure",
        "difficulty": "Medium",
        "explanation": "Spot/preemptible instances use excess cloud capacity at 60-90% discounts but can be interrupted with 2-minute notice. They are ideal for fault-tolerant ML training jobs with checkpointing. If interrupted, training resumes from the last checkpoint — saving significant cost."
    },
    {
        "question": "What is a virtual private cloud (VPC)?",
        "options": [
            "A dedicated physical data center rented from a cloud provider",
            "An isolated, logically defined network within a public cloud where you control IP ranges, subnets, and routing",
            "A containerized environment for running ML workloads",
            "A private CDN for serving model predictions"
        ],
        "answer": "An isolated, logically defined network within a public cloud where you control IP ranges, subnets, and routing",
        "category": "Cloud & Infrastructure",
        "difficulty": "Medium",
        "explanation": "A VPC provides network isolation in the cloud. You define subnets (public for internet-facing services, private for databases and training clusters), security groups (firewall rules), and routing. ML workloads often run in private subnets, accessing the internet only through NAT gateways."
    },
    {
        "question": "What does 'serverless' mean in cloud computing?",
        "options": [
            "Running workloads without any underlying servers",
            "A model where the cloud provider automatically manages server provisioning, scaling, and maintenance while you pay per execution",
            "Deploying containers that auto-scale to zero",
            "Running inference on client devices instead of servers"
        ],
        "answer": "A model where the cloud provider automatically manages server provisioning, scaling, and maintenance while you pay per execution",
        "category": "Cloud & Infrastructure",
        "difficulty": "Easy",
        "explanation": "Serverless (AWS Lambda, GCP Cloud Functions) abstracts away infrastructure management. Code runs in response to events and you pay only for compute time used. For ML, it is useful for lightweight preprocessing, post-inference hooks, or serving small models — but cold starts and memory limits can be a constraint."
    },
    {
        "question": "What is the role of a load balancer in an ML serving system?",
        "options": [
            "To compress model weights before deployment",
            "To distribute incoming inference requests across multiple model server instances",
            "To cache frequent model predictions",
            "To encrypt data in transit between services"
        ],
        "answer": "To distribute incoming inference requests across multiple model server instances",
        "category": "Cloud & Infrastructure",
        "difficulty": "Easy",
        "explanation": "A load balancer sits in front of multiple model serving instances and routes each request to an available backend, preventing any single instance from being overwhelmed. It also performs health checks and removes unhealthy instances from rotation, improving availability and throughput."
    },
    {
        "question": "What is the difference between block storage and object storage?",
        "options": [
            "Block storage is cloud-based; object storage is on-premises",
            "Block storage provides low-latency disk volumes attachable to a VM; object storage stores files as objects accessible via APIs over HTTP",
            "Block storage is for structured data; object storage is for unstructured data",
            "They are identical but differ in pricing models"
        ],
        "answer": "Block storage provides low-latency disk volumes attachable to a VM; object storage stores files as objects accessible via APIs over HTTP",
        "category": "Cloud & Infrastructure",
        "difficulty": "Medium",
        "explanation": "Block storage (AWS EBS, GCP Persistent Disk) behaves like a hard drive — low latency, mountable as a filesystem, ideal for databases and OS disks. Object storage (S3, GCS) is accessed via HTTP, infinitely scalable, but higher latency. ML training data is typically stored in object storage and streamed during training."
    },
    {
        "question": "What is TPU and how does it differ from a GPU for ML workloads?",
        "options": [
            "TPU stands for Tensor Processing Unit; it is an ASIC custom-designed by Google specifically for tensor operations in neural networks, often faster and more efficient than GPUs for large-scale training",
            "TPU stands for Training Processing Unit; it is a faster version of a GPU",
            "TPU is a type of CPU optimized for floating-point operations",
            "TPU and GPU are identical in architecture but TPUs are only available on-premises"
        ],
        "answer": "TPU stands for Tensor Processing Unit; it is an ASIC custom-designed by Google specifically for tensor operations in neural networks, often faster and more efficient than GPUs for large-scale training",
        "category": "Cloud & Infrastructure",
        "difficulty": "Medium",
        "explanation": "TPUs are custom ASICs built by Google specifically for matrix multiply operations in TensorFlow/JAX. They feature high-bandwidth memory and systolic array architectures that outperform GPUs for certain workloads (large transformers, CNNs). TPU Pods can scale to thousands of chips interconnected with high-speed links."
    },
    {
        "question": "What is a Kubernetes Pod?",
        "options": [
            "A physical server in a Kubernetes cluster",
            "The smallest deployable unit in Kubernetes, consisting of one or more containers sharing the same network namespace and storage",
            "A namespace for isolating Kubernetes workloads",
            "A persistent volume claim for storing model artifacts"
        ],
        "answer": "The smallest deployable unit in Kubernetes, consisting of one or more containers sharing the same network namespace and storage",
        "category": "Cloud & Infrastructure",
        "difficulty": "Medium",
        "explanation": "A Pod wraps one or more containers that must run together on the same node. Containers in a Pod share an IP address and can communicate via localhost. In ML serving, a Pod might contain the model server container plus a sidecar for logging or metric collection."
    },
    {
        "question": "What is auto-scaling in cloud infrastructure?",
        "options": [
            "Manually increasing server capacity during peak traffic",
            "Automatically adjusting the number of compute instances based on load metrics such as CPU utilization or request rate",
            "Upgrading instance types when memory usage exceeds a threshold",
            "A billing feature that scales cost linearly with usage"
        ],
        "answer": "Automatically adjusting the number of compute instances based on load metrics such as CPU utilization or request rate",
        "category": "Cloud & Infrastructure",
        "difficulty": "Easy",
        "explanation": "Auto-scaling groups monitor metrics (CPU, memory, custom metrics like requests-per-second) and add or remove instances automatically. For ML serving, this ensures sufficient capacity during traffic spikes and cost efficiency during low-traffic periods — scaling down to near-zero when idle."
    },
    {
        "question": "What is a container registry?",
        "options": [
            "A database that tracks running containers in a Kubernetes cluster",
            "A service that stores, versions, and distributes Docker container images",
            "A Kubernetes component that schedules containers onto nodes",
            "An audit log of container resource usage"
        ],
        "answer": "A service that stores, versions, and distributes Docker container images",
        "category": "Cloud & Infrastructure",
        "difficulty": "Easy",
        "explanation": "Container registries (DockerHub, AWS ECR, GCP Artifact Registry) store versioned Docker images. In MLOps CI/CD pipelines, a new image is built and pushed to the registry on each commit, then Kubernetes pulls the new image during deployment — enabling immutable, versioned deployments."
    },
    {
        "question": "What is the purpose of a service mesh (e.g., Istio, Linkerd) in microservice architectures?",
        "options": [
            "To provide distributed training capabilities for deep learning",
            "To manage service-to-service communication with traffic management, observability, and mutual TLS encryption",
            "To store shared configuration across microservices",
            "To run scheduled batch inference jobs"
        ],
        "answer": "To manage service-to-service communication with traffic management, observability, and mutual TLS encryption",
        "category": "Cloud & Infrastructure",
        "difficulty": "Hard",
        "explanation": "A service mesh adds a sidecar proxy to each service that intercepts all network traffic. This enables retries, circuit breaking, load balancing, distributed tracing, and mTLS without changing application code. In large ML serving stacks with many microservices, it greatly simplifies observability and security."
    },
    {
        "question": "What is multi-region deployment and why does it matter for ML systems?",
        "options": [
            "Running the same model in multiple cloud providers simultaneously",
            "Deploying infrastructure across geographically distributed data centers to reduce latency, improve availability, and meet data residency requirements",
            "Splitting a large model across multiple machines in the same data center",
            "Using multiple availability zones within a single cloud region"
        ],
        "answer": "Deploying infrastructure across geographically distributed data centers to reduce latency, improve availability, and meet data residency requirements",
        "category": "Cloud & Infrastructure",
        "difficulty": "Hard",
        "explanation": "Multi-region deployment places services closer to users (reducing latency), provides disaster recovery (if one region fails another serves traffic), and satisfies regulations requiring data to remain in certain geographies (GDPR). Complexity increases as data synchronization, failover, and latency must be carefully managed."
    },
    {
        "question": "What is a managed ML service (e.g., AWS SageMaker, GCP Vertex AI)?",
        "options": [
            "An open-source framework for building neural networks",
            "A fully managed platform that handles infrastructure provisioning for ML training, deployment, and monitoring",
            "A cloud database optimized for storing feature vectors",
            "A version control system for machine learning models"
        ],
        "answer": "A fully managed platform that handles infrastructure provisioning for ML training, deployment, and monitoring",
        "category": "Cloud & Infrastructure",
        "difficulty": "Easy",
        "explanation": "Managed ML platforms abstract away infrastructure management. SageMaker, Vertex AI, and Azure ML provide built-in notebook environments, distributed training, model registries, endpoint deployment, and monitoring — allowing data scientists to focus on modeling rather than DevOps."
    },
    {
        "question": "What is network latency and why is it critical for real-time ML inference?",
        "options": [
            "The time required to load a model into GPU memory",
            "The delay in data transmission between two points in a network, which directly adds to the end-to-end response time of inference requests",
            "The time it takes to preprocess input features before inference",
            "The bandwidth available between training nodes"
        ],
        "answer": "The delay in data transmission between two points in a network, which directly adds to the end-to-end response time of inference requests",
        "category": "Cloud & Infrastructure",
        "difficulty": "Medium",
        "explanation": "For real-time inference (fraud detection, recommendation, NLP APIs), total latency includes network round-trip time plus model compute time. Reducing network latency through edge deployment, CDN, or co-locating services in the same region/VPC is essential for sub-100ms SLA requirements."
    },
    {
        "question": "What is a CI/CD pipeline in the context of ML systems?",
        "options": [
            "A data preprocessing pipeline that cleans and transforms features continuously",
            "An automated workflow that builds, tests, and deploys code and model artifacts to production upon each change",
            "A distributed training pipeline that runs on multiple GPUs",
            "A monitoring pipeline that detects data drift in production"
        ],
        "answer": "An automated workflow that builds, tests, and deploys code and model artifacts to production upon each change",
        "category": "Cloud & Infrastructure",
        "difficulty": "Medium",
        "explanation": "CI/CD (Continuous Integration/Continuous Deployment) automates the path from code commit to production. For ML, this includes running unit tests, building Docker images, validating model performance on a holdout set, and deploying only if quality gates pass — enabling safe, frequent releases."
    },
    {
        "question": "What is the purpose of health checks in Kubernetes?",
        "options": [
            "To monitor GPU temperature and prevent overheating",
            "To periodically probe containers and automatically restart or remove those that are unhealthy or not yet ready to receive traffic",
            "To check model accuracy against a validation set",
            "To bill cloud usage based on resource consumption"
        ],
        "answer": "To periodically probe containers and automatically restart or remove those that are unhealthy or not yet ready to receive traffic",
        "category": "Cloud & Infrastructure",
        "difficulty": "Medium",
        "explanation": "Kubernetes liveness probes detect if a container is stuck and restart it. Readiness probes ensure traffic is only routed to containers that have finished loading (e.g., model weights loaded into memory). This prevents requests from hitting a model server that is still initializing."
    },
    {
        "question": "What is data replication in distributed storage systems?",
        "options": [
            "Compressing data to reduce storage costs",
            "Storing multiple copies of data across different nodes or regions to ensure durability and availability",
            "Indexing data for faster query performance",
            "Encrypting data at rest using AES-256"
        ],
        "answer": "Storing multiple copies of data across different nodes or regions to ensure durability and availability",
        "category": "Cloud & Infrastructure",
        "difficulty": "Medium",
        "explanation": "Replication (e.g., S3's 99.999999999% durability stores data across multiple AZs) protects against hardware failure. In ML, losing a training dataset or model checkpoint can be catastrophic — replication ensures that even if a disk or availability zone fails, data remains accessible."
    },
    {
        "question": "What is a feature store in ML infrastructure?",
        "options": [
            "A Git repository for storing ML model code",
            "A centralized repository that stores, manages, and serves precomputed features for both model training and real-time inference",
            "An object storage bucket for raw training data",
            "A cloud marketplace for pre-trained model weights"
        ],
        "answer": "A centralized repository that stores, manages, and serves precomputed features for both model training and real-time inference",
        "category": "Cloud & Infrastructure",
        "difficulty": "Hard",
        "explanation": "Feature stores (Feast, Tecton, Hopsworks) solve training-serving skew and feature reuse. They compute features once, store them, and serve the same values during training and inference. This prevents inconsistencies where a feature is computed differently at training vs. serving time."
    },
    {
        "question": "What is egress cost in cloud computing?",
        "options": [
            "The cost of storing data in object storage",
            "The cost charged by cloud providers for data transferred out of their network to the internet or other regions",
            "The cost of running GPU instances for training",
            "The cost of provisioning load balancers"
        ],
        "answer": "The cost charged by cloud providers for data transferred out of their network to the internet or other regions",
        "category": "Cloud & Infrastructure",
        "difficulty": "Medium",
        "explanation": "Cloud providers charge for data leaving their network (egress) but not for ingress (data coming in). For ML systems with large model outputs, predictions served to external clients, or data replicated across regions, egress fees can become significant — often the largest line item in a cloud bill."
    },
    {
        "question": "What is blue-green deployment?",
        "options": [
            "A deployment strategy where two identical production environments are maintained; traffic is switched from the old (blue) to the new (green) version atomically",
            "A rolling update strategy that gradually replaces old instances with new ones",
            "A canary release that routes 5% of traffic to a new model version",
            "A multi-cloud strategy that runs workloads on AWS and GCP simultaneously"
        ],
        "answer": "A deployment strategy where two identical production environments are maintained; traffic is switched from the old (blue) to the new (green) version atomically",
        "category": "Cloud & Infrastructure",
        "difficulty": "Hard",
        "explanation": "Blue-green deployment runs two identical environments. After validating the new version (green) in isolation, a load balancer instantly switches all traffic from blue to green. Rollback is instantaneous by switching traffic back to blue. This eliminates deployment downtime and reduces risk for ML model updates."
    },
    {
        "question": "What is a Kubernetes namespace?",
        "options": [
            "A DNS name used to access Kubernetes services externally",
            "A virtual cluster within a Kubernetes cluster used to isolate resources between teams or environments",
            "A type of Kubernetes storage volume",
            "The directory structure inside a Docker container"
        ],
        "answer": "A virtual cluster within a Kubernetes cluster used to isolate resources between teams or environments",
        "category": "Cloud & Infrastructure",
        "difficulty": "Medium",
        "explanation": "Namespaces provide a scope for Kubernetes resource names and can have separate resource quotas, RBAC policies, and network policies. In ML platforms, separate namespaces for dev, staging, and production (or per team) prevent resource conflicts and enable fine-grained access control."
    },
    {
        "question": "What is a canary deployment in ML model serving?",
        "options": [
            "Deploying a model on a single GPU to test performance before scaling",
            "Routing a small percentage of production traffic to a new model version while the rest continues using the old version, enabling safe validation",
            "Running shadow inference in parallel without returning results to users",
            "A deployment strategy that gradually replaces all instances over 24 hours"
        ],
        "answer": "Routing a small percentage of production traffic to a new model version while the rest continues using the old version, enabling safe validation",
        "category": "Cloud & Infrastructure",
        "difficulty": "Hard",
        "explanation": "Canary releases (5% of traffic to v2, 95% to v1) let you validate a new model in production with real users before full rollout. If metrics degrade (latency, error rate, business KPIs), traffic is shifted back to v1. This limits blast radius when deploying risky model updates."
    },
    {
        "question": "What is the purpose of environment variables in containerized ML deployments?",
        "options": [
            "To store model weights inside the container image",
            "To pass configuration values (API keys, model paths, hyperparameters) to a container at runtime without hardcoding them in the image",
            "To set the number of CPU threads available to the container",
            "To define the Docker base image version"
        ],
        "answer": "To pass configuration values (API keys, model paths, hyperparameters) to a container at runtime without hardcoding them in the image",
        "category": "Cloud & Infrastructure",
        "difficulty": "Easy",
        "explanation": "Environment variables decouple configuration from code. The same Docker image can be used across dev/staging/prod by injecting different environment variables (model endpoint URLs, database credentials, feature flag values). In Kubernetes, these are managed via ConfigMaps and Secrets."
    },
    {
        "question": "What is an availability zone (AZ) in cloud infrastructure?",
        "options": [
            "A geographic region where a cloud provider operates",
            "An isolated data center within a cloud region, with independent power, cooling, and networking, used to achieve high availability",
            "A virtual network segment within a VPC",
            "A service-level agreement tier offered by cloud providers"
        ],
        "answer": "An isolated data center within a cloud region, with independent power, cooling, and networking, used to achieve high availability",
        "category": "Cloud & Infrastructure",
        "difficulty": "Easy",
        "explanation": "Each cloud region contains multiple AZs (typically 3+). Deploying resources across AZs means a power outage or hardware failure in one AZ does not take down the service. ML serving systems typically deploy model replicas across multiple AZs behind a load balancer for fault tolerance."
    },
    {
        "question": "What is the function of a Kubernetes Deployment resource?",
        "options": [
            "To expose a group of Pods as a network service",
            "To declare the desired state of a Pod replica set, managing rolling updates, rollbacks, and self-healing",
            "To schedule one-time batch training jobs on GPU nodes",
            "To define persistent storage volumes for model artifacts"
        ],
        "answer": "To declare the desired state of a Pod replica set, managing rolling updates, rollbacks, and self-healing",
        "category": "Cloud & Infrastructure",
        "difficulty": "Medium",
        "explanation": "A Kubernetes Deployment declares 'I want 5 replicas of this model server running at all times.' Kubernetes continuously reconciles actual state with desired state — restarting crashed Pods, rolling out new image versions gradually, and enabling instant rollback. It is the standard way to deploy stateless ML serving workloads."
    },
    {
        "question": "What is data partitioning (sharding) in distributed ML systems?",
        "options": [
            "Encrypting portions of a dataset for security",
            "Splitting a large dataset into smaller, non-overlapping subsets distributed across multiple workers or storage nodes to enable parallel processing",
            "Compressing training data to reduce storage footprint",
            "Replicating data across multiple cloud regions"
        ],
        "answer": "Splitting a large dataset into smaller, non-overlapping subsets distributed across multiple workers or storage nodes to enable parallel processing",
        "category": "Cloud & Infrastructure",
        "difficulty": "Hard",
        "explanation": "Data sharding enables distributed training: each GPU worker receives a different shard and processes it in parallel. In databases, sharding splits records across nodes to scale write throughput. The challenge is maintaining balanced shard sizes and minimizing cross-shard operations, which add communication overhead."
    },
    {
        "question": "What is observability in cloud infrastructure?",
        "options": [
            "The ability to visually inspect container logs via a web dashboard",
            "The practice of instrumenting systems to collect metrics, logs, and traces to understand internal state from external outputs",
            "A compliance framework for auditing cloud resource usage",
            "The process of monitoring model accuracy in production"
        ],
        "answer": "The practice of instrumenting systems to collect metrics, logs, and traces to understand internal state from external outputs",
        "category": "Cloud & Infrastructure",
        "difficulty": "Medium",
        "explanation": "Observability (metrics, logs, distributed traces) enables understanding why a system behaves unexpectedly, not just whether it is up. For ML systems, observability includes infrastructure metrics (GPU utilization, memory), application metrics (latency, throughput), and ML metrics (prediction distributions, drift)."
    },
    {
        "question": "What is a cold start problem in serverless ML inference?",
        "options": [
            "Loading a model onto a GPU that was previously idle",
            "The latency spike that occurs when a serverless function is invoked for the first time or after inactivity, requiring the runtime and model to be initialized",
            "A network timeout when the inference endpoint is in a different region from the client",
            "A memory error caused by loading a model that exceeds available RAM"
        ],
        "answer": "The latency spike that occurs when a serverless function is invoked for the first time or after inactivity, requiring the runtime and model to be initialized",
        "category": "Cloud & Infrastructure",
        "difficulty": "Hard",
        "explanation": "Serverless runtimes are shut down after inactivity. When a request arrives to a cold instance, the container must be started, dependencies loaded, and the model initialized — adding seconds of latency. Mitigations include provisioned concurrency (keeping instances warm), lightweight models, or using dedicated serving infrastructure for latency-sensitive ML APIs."
    },
    {
        "question": "What is the difference between synchronous and asynchronous inference?",
        "options": [
            "Synchronous inference runs on CPUs; asynchronous inference runs on GPUs",
            "Synchronous inference waits for the model response before returning to the caller; asynchronous inference accepts the request, processes it in the background, and notifies the caller when complete",
            "Synchronous inference supports batch inputs; asynchronous inference only supports single inputs",
            "They are the same but differ in HTTP method (GET vs POST)"
        ],
        "answer": "Synchronous inference waits for the model response before returning to the caller; asynchronous inference accepts the request, processes it in the background, and notifies the caller when complete",
        "category": "Cloud & Infrastructure",
        "difficulty": "Medium",
        "explanation": "Synchronous inference suits low-latency real-time use cases (chatbots, recommendation APIs). Asynchronous inference suits high-latency or bursty workloads (video analysis, document processing) — requests are queued, processed in the background, and results are retrieved via polling or callbacks, improving throughput and decoupling clients from model servers."
    },
    {
        "question": "What is a persistent volume in Kubernetes?",
        "options": [
            "A temporary directory that exists only while a Pod is running",
            "A storage resource provisioned independently of Pod lifecycle, allowing data to persist across container restarts and Pod rescheduling",
            "A Kubernetes object for storing configuration data as key-value pairs",
            "A network-attached GPU device mapped into a container"
        ],
        "answer": "A storage resource provisioned independently of Pod lifecycle, allowing data to persist across container restarts and Pod rescheduling",
        "category": "Cloud & Infrastructure",
        "difficulty": "Medium",
        "explanation": "Containers are ephemeral — data written to the container filesystem is lost on restart. Persistent Volumes (PVs) attach external storage (cloud block disks, NFS) to Pods. In ML, PVs are used to persist training checkpoints, datasets mounted locally for fast access, and model weights."
    },
    {
        "question": "What does 'idempotency' mean in the context of cloud infrastructure operations?",
        "options": [
            "The ability to scale infrastructure to any size without code changes",
            "The property that performing the same operation multiple times produces the same result as performing it once",
            "Encrypting API calls to ensure secure transmission",
            "Automatically retrying failed requests with exponential backoff"
        ],
        "answer": "The property that performing the same operation multiple times produces the same result as performing it once",
        "category": "Cloud & Infrastructure",
        "difficulty": "Hard",
        "explanation": "Idempotency is fundamental to reliable distributed systems. In IaC, applying the same Terraform configuration multiple times should not create duplicate resources. In ML pipelines, idempotent processing ensures re-running a failed step doesn't corrupt data or create duplicate model versions."
    },
    {
        "question": "What is GPU memory bandwidth and why does it matter for LLM inference?",
        "options": [
            "The speed at which data can be transferred between GPU and CPU via PCIe",
            "The rate at which the GPU can read and write data from its on-chip memory, which is the primary bottleneck for memory-bound operations like LLM token generation",
            "The amount of VRAM available for storing model weights",
            "The clock speed of the GPU's processing cores"
        ],
        "answer": "The rate at which the GPU can read and write data from its on-chip memory, which is the primary bottleneck for memory-bound operations like LLM token generation",
        "category": "Cloud & Infrastructure",
        "difficulty": "Hard",
        "explanation": "LLM autoregressive decoding is memory-bandwidth-bound: each token generation requires loading all model weights from HBM memory. A GPU with higher bandwidth (e.g., H100: 3.35 TB/s vs A100: 2 TB/s) generates tokens faster. This is why bandwidth-optimized architectures (HBM3, HBM3e) are critical for LLM serving."
    },
    {
        "question": "What is a Helm chart in Kubernetes?",
        "options": [
            "A visual dashboard for monitoring Kubernetes cluster metrics",
            "A package manager for Kubernetes that bundles related resources into reusable, configurable templates",
            "A network policy definition for pod-to-pod communication",
            "A Kubernetes resource for running GPU-accelerated workloads"
        ],
        "answer": "A package manager for Kubernetes that bundles related resources into reusable, configurable templates",
        "category": "Cloud & Infrastructure",
        "difficulty": "Medium",
        "explanation": "Helm charts package all the Kubernetes YAML manifests (Deployments, Services, ConfigMaps) needed to deploy an application into a single versioned artifact with configurable values. ML teams use Helm to standardize model serving deployments across environments, overriding values like replica count, resource limits, and model URIs per environment."
    },
    {
        "question": "What is model parallelism in distributed ML training?",
        "options": [
            "Training multiple independent models on separate GPUs simultaneously",
            "Splitting model layers or parameters across multiple devices so that no single device needs to hold the entire model in memory",
            "Using data parallelism to process multiple mini-batches in parallel",
            "Distributing hyperparameter search across a cluster"
        ],
        "answer": "Splitting model layers or parameters across multiple devices so that no single device needs to hold the entire model in memory",
        "category": "Cloud & Infrastructure",
        "difficulty": "Hard",
        "explanation": "Large models (LLMs, GPT-4 scale) don't fit on a single GPU. Model parallelism (tensor parallelism, pipeline parallelism) splits the model across devices. Tensor parallelism splits individual weight matrices; pipeline parallelism assigns different layers to different GPUs. Both require careful communication design to minimize overhead."
    },
    {
        "question": "What is the purpose of resource quotas in Kubernetes?",
        "options": [
            "To set GPU clock speeds for containerized workloads",
            "To limit the total amount of compute resources (CPU, memory, GPU) that can be consumed within a namespace, preventing any single team from exhausting cluster resources",
            "To prioritize certain Pods for scheduling during resource contention",
            "To define maximum Pod startup time before Kubernetes considers it failed"
        ],
        "answer": "To limit the total amount of compute resources (CPU, memory, GPU) that can be consumed within a namespace, preventing any single team from exhausting cluster resources",
        "category": "Cloud & Infrastructure",
        "difficulty": "Medium",
        "explanation": "Resource quotas enforce fair usage in shared ML clusters. Without quotas, a single training job could consume all cluster GPUs, blocking other teams. Quotas set limits on total CPU/memory/GPU requests and limits per namespace, ensuring predictable resource allocation in multi-tenant ML platforms."
    },
    {
        "question": "What is data pipeline orchestration and which tools are commonly used?",
        "options": [
            "The process of encrypting data as it flows between services; tools include HashiCorp Vault",
            "The process of scheduling, monitoring, and managing dependencies between tasks in a data workflow; tools include Apache Airflow, Prefect, and Dagster",
            "The process of distributing data across multiple storage systems; tools include Apache Kafka",
            "The process of compressing data for storage efficiency; tools include Parquet and ORC"
        ],
        "answer": "The process of scheduling, monitoring, and managing dependencies between tasks in a data workflow; tools include Apache Airflow, Prefect, and Dagster",
        "category": "Cloud & Infrastructure",
        "difficulty": "Medium",
        "explanation": "Orchestration tools define DAGs (Directed Acyclic Graphs) of dependent tasks. Airflow, Prefect, and Dagster handle scheduling (run this pipeline at 2am), retries, dependency management (task B only runs after task A succeeds), and monitoring — essential for reliable ML data pipelines and model retraining workflows."
    },
    {
        "question": "What is the difference between a public subnet and a private subnet in a VPC?",
        "options": [
            "Public subnets use IPv4; private subnets use IPv6",
            "Public subnets have a route to an internet gateway and can receive inbound internet traffic; private subnets route outbound traffic through a NAT gateway but are not directly reachable from the internet",
            "Public subnets are for production; private subnets are for development",
            "Public subnets have higher bandwidth; private subnets have lower latency"
        ],
        "answer": "Public subnets have a route to an internet gateway and can receive inbound internet traffic; private subnets route outbound traffic through a NAT gateway but are not directly reachable from the internet",
        "category": "Cloud & Infrastructure",
        "difficulty": "Hard",
        "explanation": "In ML architectures, inference endpoints often sit in public subnets (to receive client requests) while training clusters, databases, and feature stores are in private subnets (no direct internet exposure). A NAT gateway allows private subnet resources to pull packages or data from the internet without being publicly accessible."
    },
    {
        "question": "What is distributed data-parallel (DDP) training?",
        "options": [
            "Distributing layers of a model across different GPUs",
            "Replicating the full model on each GPU, splitting the training data across GPUs, and aggregating gradients across all workers after each step",
            "Training a model on both CPU and GPU simultaneously",
            "A method for asynchronous gradient updates in parameter server architectures"
        ],
        "answer": "Replicating the full model on each GPU, splitting the training data across GPUs, and aggregating gradients across all workers after each step",
        "category": "Cloud & Infrastructure",
        "difficulty": "Hard",
        "explanation": "DDP (PyTorch's preferred distributed training method) places a full model copy on each GPU. Each worker processes a different data shard, computes gradients, and participates in an all-reduce operation to average gradients across all workers before the optimizer step. This scales training linearly with the number of GPUs while keeping all replicas in sync."
    },
    {
        "question": "What is a secret management service (e.g., AWS Secrets Manager, HashiCorp Vault) used for in ML systems?",
        "options": [
            "Storing model weights securely",
            "Securely storing and dynamically injecting sensitive credentials (API keys, database passwords, tokens) into applications without hardcoding them",
            "Encrypting training data at rest in object storage",
            "Managing SSH keys for EC2 instances"
        ],
        "answer": "Securely storing and dynamically injecting sensitive credentials (API keys, database passwords, tokens) into applications without hardcoding them",
        "category": "Cloud & Infrastructure",
        "difficulty": "Medium",
        "explanation": "Hardcoding credentials in code or Docker images is a major security risk. Secret managers encrypt and centrally store secrets, provide audit logs of access, support automatic rotation, and inject secrets at runtime. In ML pipelines, they secure database credentials, third-party API keys, and cloud service account tokens."
    },
    {
        "question": "What is a GPU node pool in a Kubernetes cluster?",
        "options": [
            "A shared memory pool accessible by all GPUs within a single node",
            "A group of Kubernetes nodes equipped with GPUs, labeled to accept only GPU workloads and isolated from CPU-only nodes",
            "A Kubernetes resource for pooling GPU memory across Pods",
            "A container image layer cache shared between GPU nodes"
        ],
        "answer": "A group of Kubernetes nodes equipped with GPUs, labeled to accept only GPU workloads and isolated from CPU-only nodes",
        "category": "Cloud & Infrastructure",
        "difficulty": "Medium",
        "explanation": "ML clusters separate CPU and GPU node pools to optimize cost. GPU instances are expensive — only training and inference Pods should run on them. Node pools use labels and taints/tolerations to ensure only GPU-requesting Pods are scheduled on GPU nodes, while cheap CPU nodes handle preprocessing and orchestration workloads."
    },
    {
        "question": "What is the CAP theorem and how does it apply to ML data infrastructure?",
        "options": [
            "A theorem stating that distributed ML models cannot be both accurate and efficient simultaneously",
            "A principle stating that a distributed system can only guarantee two of the three properties: Consistency, Availability, and Partition tolerance",
            "A cloud cost optimization framework balancing Compute, Access, and Performance",
            "A theorem defining trade-offs between model complexity, training data size, and generalization"
        ],
        "answer": "A principle stating that a distributed system can only guarantee two of the three properties: Consistency, Availability, and Partition tolerance",
        "category": "Cloud & Infrastructure",
        "difficulty": "Hard",
        "explanation": "CAP theorem (Brewer's theorem) means distributed data stores must trade off between strong consistency (all nodes see the same data) and high availability (every request gets a response) during network partitions. Feature stores and ML databases must choose their trade-off: financial ML might require CP (consistency over availability), while recommendation systems might prefer AP (availability over consistency)."
    },
    {
        "question": "What is the purpose of max pooling in a CNN?",
        "options": [
            "To add non-linearity to the network",
            "To reduce spatial dimensions while retaining dominant features",
            "To normalize feature map values",
            "To increase the depth of feature maps"
        ],
        "answer": "To reduce spatial dimensions while retaining dominant features",
        "category": "Computer Vision",
        "difficulty": "Medium",
        "explanation": "Max pooling takes the maximum value in each pooling window, reducing spatial resolution (width × height) while keeping the most prominent activations. This reduces computational cost, adds translation invariance, and controls overfitting."
    },
    {
        "question": "What is the difference between object detection and image classification?",
        "options": [
            "Classification is harder and requires more data",
            "Classification assigns one label to the whole image; detection locates and classifies multiple objects",
            "Detection only works on videos; classification works on static images",
            "They are the same task with different names"
        ],
        "answer": "Classification assigns one label to the whole image; detection locates and classifies multiple objects",
        "category": "Computer Vision",
        "difficulty": "Medium",
        "explanation": "Image classification outputs a single label for the entire image. Object detection (YOLO, Faster R-CNN) outputs bounding boxes and class labels for each object present in the image, handling multiple instances simultaneously."
    },
    {
        "question": "What is a convolutional filter (kernel) in a CNN?",
        "options": [
            "A fully connected layer applied to each pixel",
            "A small learnable matrix that slides over the image to detect local patterns",
            "A pooling operation that reduces image resolution",
            "A normalization layer applied after each activation"
        ],
        "answer": "A small learnable matrix that slides over the image to detect local patterns",
        "category": "Computer Vision",
        "difficulty": "Easy",
        "explanation": "A convolutional filter (e.g., 3x3 or 5x5) slides across the image computing dot products with each local patch, producing a feature map that highlights detected patterns such as edges and textures. Filters are learned during training via backpropagation."
    },
    {
        "question": "What is image augmentation used for in training CNNs?",
        "options": [
            "Increasing image resolution before inference",
            "Artificially expanding the training set with transformed versions of images to improve generalization",
            "Removing noise from images before passing them to the model",
            "Compressing images to reduce training time"
        ],
        "answer": "Artificially expanding the training set with transformed versions of images to improve generalization",
        "category": "Computer Vision",
        "difficulty": "Easy",
        "explanation": "Augmentation applies random transformations (flips, rotations, crops, color jitter, noise) to training images. This increases effective dataset size, teaches the model invariance to these transformations, and reduces overfitting — especially important with small datasets."
    },
    {
        "question": "What is the role of the encoder in a U-Net architecture?",
        "options": [
            "To generate the final segmentation mask directly",
            "To progressively downsample the input, extracting hierarchical feature representations",
            "To upsample low-resolution features back to full resolution",
            "To classify the entire image into a single category"
        ],
        "answer": "To progressively downsample the input, extracting hierarchical feature representations",
        "category": "Computer Vision",
        "difficulty": "Medium",
        "explanation": "U-Net's encoder (contracting path) uses convolution and pooling to downsample spatially while increasing channel depth, capturing context. Skip connections pass encoder features to the decoder (expanding path), which upsamples back to original resolution for dense pixel-level prediction."
    },
    {
        "question": "What distinguishes YOLO from two-stage detectors like Faster R-CNN?",
        "options": [
            "YOLO uses more anchor boxes than Faster R-CNN",
            "YOLO predicts bounding boxes and classes in a single pass; Faster R-CNN uses a separate region proposal stage",
            "Faster R-CNN is a one-stage detector; YOLO is two-stage",
            "They are architecturally identical but YOLO is trained differently"
        ],
        "answer": "YOLO predicts bounding boxes and classes in a single pass; Faster R-CNN uses a separate region proposal stage",
        "category": "Computer Vision",
        "difficulty": "Medium",
        "explanation": "YOLO (You Only Look Once) is a one-stage detector that divides the image into a grid and predicts boxes and classes in a single forward pass — extremely fast. Faster R-CNN first generates region proposals via an RPN, then classifies each region — more accurate but slower."
    },
    {
        "question": "What is the Vision Transformer (ViT) and how does it differ from CNNs?",
        "options": [
            "ViT uses recurrent layers to process image rows sequentially",
            "ViT splits images into patches, embeds them as tokens, and processes them with a Transformer encoder",
            "ViT uses depthwise separable convolutions instead of standard convolutions",
            "ViT is a GAN variant for high-resolution image generation"
        ],
        "answer": "ViT splits images into patches, embeds them as tokens, and processes them with a Transformer encoder",
        "category": "Computer Vision",
        "difficulty": "Hard",
        "explanation": "ViT treats images as sequences of fixed-size patches (e.g., 16x16), linearly embeds each patch, prepends a [CLS] token, and processes with a standard Transformer encoder. Unlike CNNs, it lacks inductive biases (locality, translation equivariance) but excels with large-scale pretraining data."
    },
    {
        "question": "What does Intersection over Union (IoU) measure in object detection?",
        "options": [
            "The ratio of true positives to false positives in detection results",
            "The overlap between a predicted bounding box and the ground truth bounding box",
            "The number of objects detected per image",
            "The confidence score assigned to each detected object"
        ],
        "answer": "The overlap between a predicted bounding box and the ground truth bounding box",
        "category": "Computer Vision",
        "difficulty": "Medium",
        "explanation": "IoU is computed as the area of the intersection of two bounding boxes divided by the area of their union. It ranges from 0 (no overlap) to 1 (perfect overlap). A predicted box is typically considered correct if IoU exceeds a threshold (commonly 0.5)."
    },
    {
        "question": "What is the purpose of batch normalization in a CNN?",
        "options": [
            "To reduce the number of trainable parameters",
            "To normalize activations within a mini-batch, stabilizing and accelerating training",
            "To pool features across spatial dimensions",
            "To apply dropout to convolutional layers"
        ],
        "answer": "To normalize activations within a mini-batch, stabilizing and accelerating training",
        "category": "Computer Vision",
        "difficulty": "Medium",
        "explanation": "Batch normalization normalizes the mean and variance of activations across a mini-batch, reducing internal covariate shift. This allows higher learning rates, reduces sensitivity to weight initialization, and acts as a mild regularizer, greatly speeding up convergence."
    },
    {
        "question": "What is semantic segmentation?",
        "options": [
            "Classifying each pixel in an image into a category without distinguishing individual instances",
            "Drawing bounding boxes around objects and labeling them",
            "Separating foreground objects from the background",
            "Predicting depth values for each pixel in an image"
        ],
        "answer": "Classifying each pixel in an image into a category without distinguishing individual instances",
        "category": "Computer Vision",
        "difficulty": "Medium",
        "explanation": "Semantic segmentation assigns a class label to every pixel (e.g., road, sky, pedestrian). Unlike instance segmentation, it does not differentiate between separate instances of the same class — all pixels belonging to 'car' share the same label regardless of which car they belong to."
    },
    {
        "question": "What is the vanishing gradient problem and how do residual connections (ResNet) address it?",
        "options": [
            "Gradients grow too large; ResNet clips them during backpropagation",
            "Gradients become near-zero in deep networks; ResNet adds skip connections that allow gradients to flow directly",
            "Gradients oscillate; ResNet uses batch normalization to stabilize them",
            "Gradients are sparse; ResNet uses dense connections to propagate them"
        ],
        "answer": "Gradients become near-zero in deep networks; ResNet adds skip connections that allow gradients to flow directly",
        "category": "Computer Vision",
        "difficulty": "Hard",
        "explanation": "In very deep networks, repeated multiplication through activation functions shrinks gradients to near-zero, making early layers learn very slowly. ResNet introduces skip (residual) connections that add the input of a block to its output, creating a gradient highway that preserves signal strength during backpropagation."
    },
    {
        "question": "What is the difference between instance segmentation and semantic segmentation?",
        "options": [
            "Instance segmentation only works on binary masks; semantic segmentation supports multiple classes",
            "Instance segmentation distinguishes individual object instances; semantic segmentation labels pixels by class only",
            "Semantic segmentation is faster because it uses bounding boxes instead of masks",
            "They are equivalent tasks with different computational costs"
        ],
        "answer": "Instance segmentation distinguishes individual object instances; semantic segmentation labels pixels by class only",
        "category": "Computer Vision",
        "difficulty": "Medium",
        "explanation": "Semantic segmentation labels every pixel with a class but merges all instances of the same class. Instance segmentation (e.g., Mask R-CNN) produces a separate binary mask for each detected object instance, enabling differentiation between, say, two overlapping cars."
    },
    {
        "question": "What is transfer learning in the context of computer vision?",
        "options": [
            "Copying weights from one GPU to another during distributed training",
            "Using a model pretrained on a large dataset as a starting point for a new task",
            "Converting a classification model to a detection model",
            "Transferring augmented images between training epochs"
        ],
        "answer": "Using a model pretrained on a large dataset as a starting point for a new task",
        "category": "Computer Vision",
        "difficulty": "Easy",
        "explanation": "Transfer learning leverages representations learned on large datasets (e.g., ImageNet) by fine-tuning the pretrained model on a smaller target dataset. Early layers capture generic features (edges, textures) that transfer well, greatly reducing the data and compute needed for the new task."
    },
    {
        "question": "What is Non-Maximum Suppression (NMS) used for in object detection?",
        "options": [
            "Normalizing confidence scores across all detected classes",
            "Eliminating duplicate overlapping bounding boxes, keeping only the most confident prediction per object",
            "Selecting anchor boxes with the highest IoU during training",
            "Suppressing activations in feature maps below a learned threshold"
        ],
        "answer": "Eliminating duplicate overlapping bounding boxes, keeping only the most confident prediction per object",
        "category": "Computer Vision",
        "difficulty": "Medium",
        "explanation": "Object detectors often produce multiple overlapping boxes for the same object. NMS iteratively selects the box with the highest confidence score and removes all other boxes that have IoU above a threshold with it, retaining one clean prediction per object."
    },
    {
        "question": "What is the role of the ReLU activation function in CNNs?",
        "options": [
            "To normalize pixel values to the [0, 1] range",
            "To introduce non-linearity by zeroing out negative activations",
            "To reduce spatial dimensions of feature maps",
            "To convert multi-channel feature maps to single-channel outputs"
        ],
        "answer": "To introduce non-linearity by zeroing out negative activations",
        "category": "Computer Vision",
        "difficulty": "Easy",
        "explanation": "ReLU (Rectified Linear Unit) applies f(x) = max(0, x), setting negative values to zero while keeping positive values unchanged. This introduces non-linearity without saturating gradients as severely as sigmoid or tanh, enabling deep networks to learn complex feature hierarchies efficiently."
    },
    {
        "question": "What is depthwise separable convolution and why is it used in architectures like MobileNet?",
        "options": [
            "A convolution that operates only on the depth dimension, ignoring spatial extent",
            "A factorization of standard convolution into depthwise and pointwise steps to reduce computation",
            "A convolution with dilated kernels to increase the receptive field",
            "A grouped convolution that splits channels into equal-sized groups"
        ],
        "answer": "A factorization of standard convolution into depthwise and pointwise steps to reduce computation",
        "category": "Computer Vision",
        "difficulty": "Hard",
        "explanation": "Depthwise separable convolution applies a single spatial filter per input channel (depthwise), then combines channels with a 1x1 convolution (pointwise). This reduces computation by roughly 8–9x compared to standard convolution, making architectures like MobileNet efficient for mobile and edge devices."
    },
    {
        "question": "What is optical flow in computer vision?",
        "options": [
            "The path that light travels through a camera lens",
            "The apparent motion of pixels or regions between consecutive video frames",
            "A technique for adjusting white balance in images",
            "The gradient magnitude computed across an image"
        ],
        "answer": "The apparent motion of pixels or regions between consecutive video frames",
        "category": "Computer Vision",
        "difficulty": "Medium",
        "explanation": "Optical flow estimates the 2D motion vector for each pixel between two frames, representing how image content moves over time. It is widely used in video understanding, action recognition, object tracking, and video stabilization. Classic methods include Lucas-Kanade; deep learning approaches include FlowNet and RAFT."
    },
    {
        "question": "What problem does the Focal Loss function solve in object detection?",
        "options": [
            "Gradient explosion caused by large bounding box regression errors",
            "Class imbalance between abundant easy background examples and rare hard foreground examples",
            "Overfitting due to insufficient training data for rare object categories",
            "Slow convergence caused by inconsistent anchor box sizes"
        ],
        "answer": "Class imbalance between abundant easy background examples and rare hard foreground examples",
        "category": "Computer Vision",
        "difficulty": "Hard",
        "explanation": "In one-stage detectors, the vast majority of candidate regions are easy negatives (background), overwhelming the loss signal. Focal Loss (used in RetinaNet) down-weights well-classified easy examples by a modulating factor, forcing the model to focus learning on hard, misclassified examples and addressing extreme foreground-background imbalance."
    },
    {
        "question": "What is the purpose of skip connections in the U-Net decoder?",
        "options": [
            "To skip certain layers during inference to speed up prediction",
            "To concatenate encoder feature maps with decoder feature maps, preserving fine-grained spatial detail",
            "To apply residual addition between consecutive decoder blocks",
            "To bypass batch normalization layers during the upsampling path"
        ],
        "answer": "To concatenate encoder feature maps with decoder feature maps, preserving fine-grained spatial detail",
        "category": "Computer Vision",
        "difficulty": "Hard",
        "explanation": "As the encoder downsamples, fine spatial details are lost. U-Net's skip connections directly concatenate encoder feature maps at each resolution level to the corresponding decoder level. This allows the decoder to recover precise localization information alongside high-level semantic context, which is critical for accurate pixel-level segmentation."
    },
    {
        "question": "What does the term 'receptive field' mean in the context of CNNs?",
        "options": [
            "The number of output classes a CNN can predict",
            "The region of the input image that influences a particular neuron's activation",
            "The spatial size of the feature map produced by a convolutional layer",
            "The set of filters applied at a single convolutional layer"
        ],
        "answer": "The region of the input image that influences a particular neuron's activation",
        "category": "Computer Vision",
        "difficulty": "Medium",
        "explanation": "The receptive field of a neuron is the area in the original input space that contributed to its computation. Deeper layers have larger effective receptive fields because each successive convolution aggregates information from a wider input region. Large receptive fields allow the network to capture global context, while small fields capture fine local detail."
    },
    {
        "question": "What is data imbalance in image classification and one common strategy to mitigate it?",
        "options": [
            "Having images of different resolutions; solved by resizing all images uniformly",
            "Having far more samples of some classes than others; addressed by oversampling minority classes or using weighted loss",
            "Having too few total images; solved by collecting more data from all classes equally",
            "Having mislabeled images; addressed by manual label correction"
        ],
        "answer": "Having far more samples of some classes than others; addressed by oversampling minority classes or using weighted loss",
        "category": "Computer Vision",
        "difficulty": "Medium",
        "explanation": "Class imbalance occurs when some categories have dramatically more training examples than others, biasing the model toward majority classes. Strategies include oversampling minority classes (e.g., SMOTE for images), undersampling majority classes, generating synthetic samples via augmentation, or applying class-weighted loss to penalize errors on rare classes more heavily."
    },
    {
        "question": "What is the role of anchor boxes in object detection models like Faster R-CNN and SSD?",
        "options": [
            "They are ground-truth bounding boxes used only during evaluation",
            "They are predefined reference boxes of various scales and aspect ratios used to predict object locations",
            "They are feature maps anchored to specific spatial positions in the backbone",
            "They define the grid cells used to partition the image in one-stage detectors"
        ],
        "answer": "They are predefined reference boxes of various scales and aspect ratios used to predict object locations",
        "category": "Computer Vision",
        "difficulty": "Hard",
        "explanation": "Anchor boxes are a set of reference bounding boxes of multiple scales and aspect ratios placed at each spatial location in a feature map. The model predicts offsets relative to these anchors rather than absolute coordinates, simplifying the regression task. Anchors matched to ground truth boxes by IoU become positive training examples."
    },
    {
        "question": "What is image super-resolution in deep learning?",
        "options": [
            "Classifying an image at multiple scales simultaneously",
            "Reconstructing a high-resolution image from a low-resolution input",
            "Detecting objects with sub-pixel accuracy using dense prediction",
            "Increasing the number of color channels from grayscale to RGB"
        ],
        "answer": "Reconstructing a high-resolution image from a low-resolution input",
        "category": "Computer Vision",
        "difficulty": "Medium",
        "explanation": "Image super-resolution is the task of recovering a high-resolution (HR) image from its low-resolution (LR) counterpart. Deep learning approaches like SRCNN, ESRGAN, and Real-ESRGAN learn upsampling mappings using convolutional and generative networks, outperforming classical interpolation methods such as bicubic upsampling in perceptual quality."
    },
    {
        "question": "What is the Grad-CAM technique used for?",
        "options": [
            "Accelerating gradient computation during backpropagation in CNNs",
            "Visualizing which regions of an image a CNN focuses on when making a prediction",
            "Generating adversarial examples by computing image gradients",
            "Calibrating class probabilities output by a softmax classifier"
        ],
        "answer": "Visualizing which regions of an image a CNN focuses on when making a prediction",
        "category": "Computer Vision",
        "difficulty": "Hard",
        "explanation": "Gradient-weighted Class Activation Mapping (Grad-CAM) computes the gradients of a target class score with respect to the final convolutional feature maps, then weights those maps accordingly to produce a heatmap. This highlights the discriminative image regions the network used, providing interpretability without architectural changes."
    },
    {
        "question": "What is the difference between precision and recall in the context of object detection evaluation?",
        "options": [
            "Precision measures detection speed; recall measures detection accuracy",
            "Precision is the fraction of detections that are correct; recall is the fraction of ground-truth objects that are detected",
            "Precision measures IoU quality; recall measures confidence calibration",
            "They are inversely proportional metrics that are always summed to equal 1"
        ],
        "answer": "Precision is the fraction of detections that are correct; recall is the fraction of ground-truth objects that are detected",
        "category": "Computer Vision",
        "difficulty": "Medium",
        "explanation": "Precision = TP / (TP + FP): of all boxes the model predicts, what fraction are actual objects. Recall = TP / (TP + FN): of all real objects, what fraction did the model find. The Precision-Recall curve and its area (Average Precision, AP) are the standard evaluation metrics in object detection benchmarks like COCO."
    },
    {
        "question": "What is a data pipeline?",
        "options": [
            "A type of neural network architecture",
            "A series of data processing steps that move and transform data",
            "A database indexing strategy",
            "A model deployment framework"
        ],
        "answer": "A series of data processing steps that move and transform data",
        "category": "Data Engineering",
        "difficulty": "Easy",
        "explanation": "A data pipeline automates the flow of data from sources through transformations (cleaning, aggregation, enrichment) to destinations like data warehouses or ML feature stores, ensuring reliable, repeatable data processing."
    },
    {
        "question": "What does ETL stand for?",
        "options": [
            "Extract, Transfer, Load",
            "Extract, Transform, Load",
            "Encode, Train, Launch",
            "Evaluate, Test, Learn"
        ],
        "answer": "Extract, Transform, Load",
        "category": "Data Engineering",
        "difficulty": "Easy",
        "explanation": "ETL describes the classic data integration pattern: Extract data from source systems, Transform it (clean, filter, aggregate, join), and Load it into a destination (data warehouse). Modern alternatives include ELT where transformation happens after loading."
    },
    {
        "question": "What is the difference between a data warehouse and a data lake?",
        "options": [
            "A data warehouse stores raw data; a data lake stores only structured data",
            "A data warehouse stores structured, processed data; a data lake stores raw data of all types",
            "They are the same but differ in geographic location",
            "A data lake is faster; a data warehouse has more storage"
        ],
        "answer": "A data warehouse stores structured, processed data; a data lake stores raw data of all types",
        "category": "Data Engineering",
        "difficulty": "Medium",
        "explanation": "Data warehouses (Redshift, BigQuery, Snowflake) store cleaned, structured, schema-on-write data optimized for analytics. Data lakes (S3, ADLS) store raw, unstructured/semi-structured data at scale (schema-on-read), offering more flexibility but requiring more processing."
    },
    {
        "question": "What is feature engineering?",
        "options": [
            "Designing neural network architectures",
            "Creating, transforming, or selecting input variables to improve model performance",
            "Writing SQL queries to extract features from databases",
            "Optimizing hyperparameters of a model"
        ],
        "answer": "Creating, transforming, or selecting input variables to improve model performance",
        "category": "Data Engineering",
        "difficulty": "Medium",
        "explanation": "Feature engineering involves domain-driven creation of new inputs (e.g., ratios, interactions, date parts), transformations (log scale, binning), and selection to provide models with more signal. It often has more impact on performance than model choice."
    },
    {
        "question": "What is the purpose of a feature store in MLOps?",
        "options": [
            "To store trained model weights and artifacts",
            "To centralize, version, and serve features for training and real-time inference consistently",
            "To manage experiment tracking and hyperparameter logging",
            "To monitor model predictions in production"
        ],
        "answer": "To centralize, version, and serve features for training and real-time inference consistently",
        "category": "Data Engineering",
        "difficulty": "Hard",
        "explanation": "A feature store (Feast, Tecton, Hopsworks) solves the training-serving skew problem by ensuring features computed during training are identical to those served at inference time, with versioning, sharing across teams, and point-in-time correctness."
    },
    {
        "question": "What is a primary key in a relational database?",
        "options": [
            "The most frequently queried column",
            "A column or set of columns that uniquely identifies each row",
            "An index on a foreign table",
            "The first column in a table by convention"
        ],
        "answer": "A column or set of columns that uniquely identifies each row",
        "category": "Data Engineering",
        "difficulty": "Easy",
        "explanation": "A primary key uniquely identifies each record in a table and cannot contain NULL values. It enforces entity integrity and is used as the reference target for foreign keys in other tables to establish relationships."
    },
    {
        "question": "What does SQL stand for?",
        "options": [
            "Sequential Query Language",
            "Structured Query Language",
            "Stored Query Logic",
            "Standard Query Library"
        ],
        "answer": "Structured Query Language",
        "category": "Data Engineering",
        "difficulty": "Easy",
        "explanation": "SQL (Structured Query Language) is the standard language for managing and querying relational databases. It includes DDL (CREATE, ALTER, DROP), DML (SELECT, INSERT, UPDATE, DELETE), and DCL (GRANT, REVOKE) commands."
    },
    {
        "question": "What is a foreign key?",
        "options": [
            "A key used to encrypt sensitive data in a database",
            "A column that references the primary key of another table to create a relationship",
            "A unique index on a non-primary column",
            "A backup copy of the primary key"
        ],
        "answer": "A column that references the primary key of another table to create a relationship",
        "category": "Data Engineering",
        "difficulty": "Easy",
        "explanation": "Foreign keys enforce referential integrity — ensuring that a value in the foreign key column corresponds to an existing primary key in the referenced table. They define parent-child relationships between tables in a relational schema."
    },
    {
        "question": "What is the difference between batch processing and stream processing?",
        "options": [
            "Batch is for structured data; stream is for unstructured data",
            "Batch processes data in finite, scheduled chunks; stream processing handles data continuously in near-real-time",
            "Stream processing requires more storage than batch processing",
            "They are identical but operate on different cloud providers"
        ],
        "answer": "Batch processes data in finite, scheduled chunks; stream processing handles data continuously in near-real-time",
        "category": "Data Engineering",
        "difficulty": "Medium",
        "explanation": "Batch processing (Spark, Hadoop) processes accumulated data at scheduled intervals, suitable for large-scale historical analysis. Stream processing (Kafka Streams, Flink, Spark Streaming) handles data in motion with low latency, suitable for real-time dashboards and fraud detection."
    },
    {
        "question": "What is schema-on-read vs. schema-on-write?",
        "options": [
            "Schema-on-read validates data when it's stored; schema-on-write validates it when queried",
            "Schema-on-write enforces structure at ingestion (database); schema-on-read interprets structure at query time (data lake)",
            "They describe different SQL dialects",
            "Schema-on-read is faster for writing; schema-on-write is faster for reading"
        ],
        "answer": "Schema-on-write enforces structure at ingestion (database); schema-on-read interprets structure at query time (data lake)",
        "category": "Data Engineering",
        "difficulty": "Medium",
        "explanation": "Schema-on-write (relational DBs, warehouses) validates and enforces schema when data is loaded, ensuring consistency but requiring upfront design. Schema-on-read (data lakes, Hive) stores raw data and applies schema at query time, offering flexibility but shifting validation burden to consumers."
    },
    {
        "question": "What is data partitioning and why is it used?",
        "options": [
            "Splitting data into training and test sets",
            "Dividing a large table into smaller pieces based on a key to improve query performance",
            "Encrypting sensitive columns before storing them",
            "Replicating data across multiple database nodes"
        ],
        "answer": "Dividing a large table into smaller pieces based on a key to improve query performance",
        "category": "Data Engineering",
        "difficulty": "Medium",
        "explanation": "Partitioning (by date, region, customer ID) allows queries to scan only relevant partitions rather than the entire table (partition pruning). It dramatically improves performance on large datasets and is standard practice in data warehouses and distributed storage systems."
    },
    {
        "question": "What is Apache Kafka primarily used for?",
        "options": [
            "Training distributed machine learning models",
            "A distributed event streaming platform for high-throughput, fault-tolerant data pipelines",
            "A columnar storage format for data warehouses",
            "A workflow orchestration tool for scheduling batch jobs"
        ],
        "answer": "A distributed event streaming platform for high-throughput, fault-tolerant data pipelines",
        "category": "Data Engineering",
        "difficulty": "Hard",
        "explanation": "Kafka is a distributed log-based messaging system that decouples data producers from consumers. It stores event streams durably, supports replay, and handles millions of messages per second — the backbone of real-time data architectures, event sourcing, and change data capture."
    },
    {
        "question": "What is the difference between OLTP and OLAP systems?",
        "options": [
            "OLTP is for reading large aggregations; OLAP handles individual row transactions",
            "OLTP handles high-throughput row-level transactions; OLAP handles complex analytical queries over large aggregations",
            "OLAP is an older system replaced by OLTP in modern architectures",
            "They differ only in cloud provider"
        ],
        "answer": "OLTP handles high-throughput row-level transactions; OLAP handles complex analytical queries over large aggregations",
        "category": "Data Engineering",
        "difficulty": "Hard",
        "explanation": "OLTP (Online Transaction Processing) systems (PostgreSQL, MySQL) are optimized for fast INSERT/UPDATE/DELETE on individual rows. OLAP (Online Analytical Processing) systems (Snowflake, BigQuery, Redshift) use columnar storage and are optimized for scans, aggregations, and joins across billions of rows."
    },
    {
        "question": "What is normalization in relational databases?",
        "options": [
            "Converting all numeric values to a 0-1 scale",
            "Organizing tables to reduce data redundancy and improve data integrity",
            "Encrypting data before storage",
            "Combining multiple tables into a single flat table"
        ],
        "answer": "Organizing tables to reduce data redundancy and improve data integrity",
        "category": "Data Engineering",
        "difficulty": "Medium",
        "explanation": "Database normalization (1NF, 2NF, 3NF, BCNF) is the process of structuring tables to eliminate redundant data and ensure data dependencies make sense. It reduces update anomalies but can require more JOINs, so data warehouses often deliberately denormalize for query performance."
    },
    {
        "question": "What is a data mart?",
        "options": [
            "A small, subject-oriented subset of a data warehouse focused on a specific business area",
            "A marketplace for buying and selling datasets",
            "A lightweight alternative to a full database",
            "A caching layer between application and database"
        ],
        "answer": "A small, subject-oriented subset of a data warehouse focused on a specific business area",
        "category": "Data Engineering",
        "difficulty": "Medium",
        "explanation": "A data mart is a focused slice of a data warehouse serving a particular department (sales, finance, marketing). It provides faster, simpler access for business users without exposing the full enterprise data warehouse complexity. Data marts can be dependent (sourced from DW) or independent."
    },
    {
        "question": "What does ACID stand for in database transactions?",
        "options": [
            "Automated, Consistent, Indexed, Durable",
            "Atomicity, Consistency, Isolation, Durability",
            "Asynchronous, Cached, Integrated, Distributed",
            "Accurate, Complete, Isolated, Defined"
        ],
        "answer": "Atomicity, Consistency, Isolation, Durability",
        "category": "Data Engineering",
        "difficulty": "Medium",
        "explanation": "ACID properties guarantee reliable database transactions: Atomicity (all or nothing), Consistency (data remains valid), Isolation (concurrent transactions don't interfere), Durability (committed data persists). These are fundamental to relational databases like PostgreSQL and MySQL."
    },
    {
        "question": "What is Change Data Capture (CDC)?",
        "options": [
            "A method to compress database backups",
            "A technique to track and capture row-level changes in a database for downstream consumption",
            "A process of auditing user access to sensitive columns",
            "A schema migration strategy for zero-downtime deployments"
        ],
        "answer": "A technique to track and capture row-level changes in a database for downstream consumption",
        "category": "Data Engineering",
        "difficulty": "Hard",
        "explanation": "CDC reads the database transaction log (WAL in PostgreSQL, binlog in MySQL) to capture INSERT, UPDATE, and DELETE events in near-real-time. Tools like Debezium publish these changes to Kafka, enabling real-time data sync to warehouses, search indexes, or caches without polling."
    },
    {
        "question": "What is Apache Spark primarily used for?",
        "options": [
            "Serving REST APIs for machine learning models",
            "A unified analytics engine for large-scale distributed data processing",
            "Scheduling and orchestrating workflow DAGs",
            "A NoSQL document database"
        ],
        "answer": "A unified analytics engine for large-scale distributed data processing",
        "category": "Data Engineering",
        "difficulty": "Medium",
        "explanation": "Apache Spark processes large datasets across a cluster using in-memory computation, making it much faster than MapReduce. It supports batch processing, SQL (Spark SQL), streaming (Structured Streaming), ML (MLlib), and graph processing, making it the most widely used big data engine."
    },
    {
        "question": "What is a slowly changing dimension (SCD)?",
        "options": [
            "A dimension table that is rarely queried",
            "A data warehousing technique for handling changes to dimension attributes over time",
            "A column with slowly updating aggregate statistics",
            "A partition strategy for time-series data"
        ],
        "answer": "A data warehousing technique for handling changes to dimension attributes over time",
        "category": "Data Engineering",
        "difficulty": "Hard",
        "explanation": "SCDs manage how dimension attributes (like a customer's address) change over time. SCD Type 1 overwrites old values, Type 2 adds a new row with effective dates to preserve history, and Type 3 stores both old and new values in separate columns. Type 2 is most common in analytics."
    },
    {
        "question": "What is a star schema in data warehousing?",
        "options": [
            "A schema with exactly five tables forming a star shape",
            "A dimensional modeling pattern with a central fact table surrounded by dimension tables",
            "A distributed schema across multiple cloud regions",
            "A schema used exclusively for time-series data"
        ],
        "answer": "A dimensional modeling pattern with a central fact table surrounded by dimension tables",
        "category": "Data Engineering",
        "difficulty": "Medium",
        "explanation": "In a star schema, a central fact table (containing measurable business events and foreign keys) is joined directly to denormalized dimension tables (customers, products, dates). It offers simple, fast queries for analytics tools and is the foundation of Kimball-style dimensional modeling."
    },
    {
        "question": "What is data lineage?",
        "options": [
            "The historical ownership chain of a dataset",
            "Tracking the origin, movement, and transformation of data across systems",
            "The hereditary structure of database schemas",
            "A versioning strategy for machine learning datasets"
        ],
        "answer": "Tracking the origin, movement, and transformation of data across systems",
        "category": "Data Engineering",
        "difficulty": "Medium",
        "explanation": "Data lineage documents where data comes from, how it flows through transformations, and where it ends up. It is critical for debugging data quality issues, regulatory compliance (GDPR, HIPAA), and understanding the impact of upstream schema changes on downstream consumers."
    },
    {
        "question": "What is the purpose of Apache Airflow?",
        "options": [
            "A distributed in-memory data grid for caching",
            "A platform to programmatically author, schedule, and monitor data workflow DAGs",
            "A streaming engine for processing Kafka topics",
            "A columnar file format for big data storage"
        ],
        "answer": "A platform to programmatically author, schedule, and monitor data workflow DAGs",
        "category": "Data Engineering",
        "difficulty": "Medium",
        "explanation": "Apache Airflow lets engineers define workflows as DAGs (Directed Acyclic Graphs) in Python, handling scheduling, dependency management, retries, and monitoring. It is the de facto standard for orchestrating ETL/ELT pipelines, ML workflows, and data engineering tasks."
    },
    {
        "question": "What is a columnar storage format and why is it beneficial for analytics?",
        "options": [
            "It stores each row together, improving insert performance",
            "It stores each column's values contiguously, enabling fast aggregations and efficient compression",
            "It is a format exclusive to NoSQL databases",
            "It encrypts each column with a separate key for security"
        ],
        "answer": "It stores each column's values contiguously, enabling fast aggregations and efficient compression",
        "category": "Data Engineering",
        "difficulty": "Hard",
        "explanation": "Columnar formats (Parquet, ORC) store all values of a column together. Analytical queries that aggregate a few columns from millions of rows only read the relevant columns, drastically reducing I/O. Homogeneous data per column also compresses far better than row-oriented storage."
    },
    {
        "question": "What is idempotency in the context of data pipelines?",
        "options": [
            "The ability to process data faster on repeated runs",
            "Ensuring that running a pipeline multiple times produces the same result as running it once",
            "Automatically deduplicating records at ingestion",
            "A method of parallelizing transformations"
        ],
        "answer": "Ensuring that running a pipeline multiple times produces the same result as running it once",
        "category": "Data Engineering",
        "difficulty": "Hard",
        "explanation": "Idempotent pipelines can be safely retried or re-run without causing duplicate data or inconsistent state. This is critical for fault tolerance — when a pipeline fails mid-run, you can restart it from the beginning without side effects. UPSERT operations and overwriting partitions are common patterns."
    },
    {
        "question": "What is data quality and what are its key dimensions?",
        "options": [
            "How fast data can be processed; measured in throughput",
            "A measure of data fitness for use, covering accuracy, completeness, consistency, timeliness, and uniqueness",
            "The encryption strength applied to stored data",
            "The ratio of structured to unstructured data in a pipeline"
        ],
        "answer": "A measure of data fitness for use, covering accuracy, completeness, consistency, timeliness, and uniqueness",
        "category": "Data Engineering",
        "difficulty": "Medium",
        "explanation": "Data quality dimensions include: Accuracy (correctness), Completeness (no missing values), Consistency (no contradictions across systems), Timeliness (data is current), and Uniqueness (no duplicates). Tools like Great Expectations, dbt tests, and Soda enforce these via automated checks in pipelines."
    },
    {
        "question": "What is a surrogate key in data warehousing?",
        "options": [
            "The natural business identifier of a record",
            "A system-generated integer key used in dimension tables instead of the natural key",
            "A composite key made of multiple business columns",
            "A hashed version of a primary key for security"
        ],
        "answer": "A system-generated integer key used in dimension tables instead of the natural key",
        "category": "Data Engineering",
        "difficulty": "Hard",
        "explanation": "Surrogate keys are meaningless integers (or UUIDs) assigned by the data warehouse to dimension records. They decouple the warehouse from source system key changes, support SCD Type 2 history tracking, and improve JOIN performance compared to natural string keys."
    },
    {
        "question": "What is the CAP theorem?",
        "options": [
            "A theorem stating that databases can only be optimized for one of: capacity, accuracy, or performance",
            "A distributed systems principle stating a system can only guarantee two of: consistency, availability, or partition tolerance",
            "A rule defining maximum column count in relational tables",
            "A formula for calculating data pipeline capacity"
        ],
        "answer": "A distributed systems principle stating a system can only guarantee two of: consistency, availability, or partition tolerance",
        "category": "Data Engineering",
        "difficulty": "Hard",
        "explanation": "The CAP theorem (Brewer's theorem) states distributed systems must trade off between Consistency (every read gets the latest write), Availability (every request gets a response), and Partition Tolerance (system operates despite network splits). Most distributed databases choose CP (HBase) or AP (Cassandra, DynamoDB)."
    },
    {
        "question": "What is dbt (data build tool) used for?",
        "options": [
            "Streaming data from Kafka to object storage",
            "Transforming data inside a warehouse using SQL, with version control and testing",
            "Deploying machine learning models to production",
            "Orchestrating multi-step data ingestion workflows"
        ],
        "answer": "Transforming data inside a warehouse using SQL, with version control and testing",
        "category": "Data Engineering",
        "difficulty": "Medium",
        "explanation": "dbt enables analytics engineers to write modular SQL SELECT statements (models) that dbt compiles and runs in the warehouse. It brings software engineering practices to analytics: version control, automated testing, documentation, and lineage — making the T in ELT manageable at scale."
    },
    {
        "question": "What is data sharding?",
        "options": [
            "Splitting a dataset into training and validation sets",
            "Horizontally partitioning data across multiple database nodes to distribute load",
            "Compressing large tables into smaller file sizes",
            "Creating read replicas of a primary database"
        ],
        "answer": "Horizontally partitioning data across multiple database nodes to distribute load",
        "category": "Data Engineering",
        "difficulty": "Hard",
        "explanation": "Sharding splits a large database horizontally across multiple servers (shards), each holding a subset of rows. A shard key (e.g., user ID) determines which shard stores a record. It enables horizontal scaling beyond a single node's capacity but adds complexity around cross-shard queries and rebalancing."
    },
    {
        "question": "What is Apache Parquet?",
        "options": [
            "A workflow orchestration framework",
            "An open-source columnar file format optimized for analytical workloads",
            "A real-time stream processing engine",
            "A distributed key-value store"
        ],
        "answer": "An open-source columnar file format optimized for analytical workloads",
        "category": "Data Engineering",
        "difficulty": "Medium",
        "explanation": "Apache Parquet is a columnar storage format widely used in the Hadoop ecosystem, Spark, and cloud data lakes. It supports efficient compression (Snappy, ZSTD), predicate pushdown, and schema evolution. It is the standard file format for storing large analytical datasets on object storage like S3."
    },
    {
        "question": "What is a data catalog?",
        "options": [
            "A database of all SQL queries run in an organization",
            "A metadata management system that inventories, documents, and makes data assets discoverable",
            "A billing dashboard for cloud data storage costs",
            "A registry of all active ETL jobs in a pipeline"
        ],
        "answer": "A metadata management system that inventories, documents, and makes data assets discoverable",
        "category": "Data Engineering",
        "difficulty": "Medium",
        "explanation": "A data catalog (AWS Glue, Alation, Collibra) stores metadata about datasets: schema, ownership, descriptions, lineage, usage statistics, and data quality. It enables data discovery, governance, and self-service analytics by helping users find and understand available data assets."
    },
    {
        "question": "What is the ELT pattern and how does it differ from ETL?",
        "options": [
            "ELT encrypts data before loading; ETL transforms it after",
            "ELT loads raw data into the destination first, then transforms it inside the warehouse; ETL transforms before loading",
            "ELT is a real-time pattern; ETL is batch-only",
            "They are identical; ELT is just a newer acronym for ETL"
        ],
        "answer": "ELT loads raw data into the destination first, then transforms it inside the warehouse; ETL transforms before loading",
        "category": "Data Engineering",
        "difficulty": "Medium",
        "explanation": "ELT (Extract, Load, Transform) became practical with powerful cloud warehouses (Snowflake, BigQuery). Raw data is loaded first, then transformed using the warehouse's compute. This is more flexible (raw data is preserved), easier to reprocess, and eliminates the separate transformation server required by ETL."
    },
    {
        "question": "What is a data mesh architecture?",
        "options": [
            "A network topology for connecting database servers",
            "A decentralized data architecture where domain teams own and serve their own data as products",
            "A mesh network protocol for IoT sensor data",
            "A distributed caching layer for low-latency data access"
        ],
        "answer": "A decentralized data architecture where domain teams own and serve their own data as products",
        "category": "Data Engineering",
        "difficulty": "Hard",
        "explanation": "Data mesh (coined by Zhamak Dehghani) decentralizes data ownership to domain teams who treat data as a product with defined SLAs, documentation, and quality standards. It relies on four principles: domain ownership, data as a product, self-serve infrastructure, and federated computational governance."
    },
    {
        "question": "What is a window function in SQL?",
        "options": [
            "A function that filters rows visible to a query",
            "A function that performs calculations across a set of rows related to the current row without collapsing them",
            "A stored procedure triggered on a time schedule",
            "A function for parsing JSON objects inside SQL"
        ],
        "answer": "A function that performs calculations across a set of rows related to the current row without collapsing them",
        "category": "Data Engineering",
        "difficulty": "Medium",
        "explanation": "Window functions (ROW_NUMBER, RANK, LAG, LEAD, SUM OVER, AVG OVER) operate on a window of rows defined by PARTITION BY and ORDER BY clauses. Unlike GROUP BY, they preserve individual rows while adding aggregate or ranking values — essential for running totals, rankings, and time-series comparisons."
    },
    {
        "question": "What is data governance?",
        "options": [
            "The process of backing up and archiving data assets",
            "A framework of policies, roles, and processes ensuring data quality, security, and compliant use",
            "Automated monitoring of pipeline execution times",
            "Version control practices applied to database schemas"
        ],
        "answer": "A framework of policies, roles, and processes ensuring data quality, security, and compliant use",
        "category": "Data Engineering",
        "difficulty": "Medium",
        "explanation": "Data governance establishes accountability for data assets through data ownership, access controls, quality standards, privacy compliance (GDPR, CCPA), and retention policies. It ensures organizations can trust their data and use it responsibly, typically enforced via tools like Collibra, Atlan, or Unity Catalog."
    },
    {
        "question": "What is a fact table in dimensional modeling?",
        "options": [
            "A table storing verified, audited business facts",
            "A central table in a star or snowflake schema storing measurable business events and foreign keys to dimensions",
            "A reference table containing lookup values",
            "A table logging all data quality test results"
        ],
        "answer": "A central table in a star or snowflake schema storing measurable business events and foreign keys to dimensions",
        "category": "Data Engineering",
        "difficulty": "Medium",
        "explanation": "Fact tables store quantitative measures (revenue, quantity, duration) and foreign keys linking to dimension tables. They record business events like sales transactions or page views. Facts are typically additive (can be summed), semi-additive (can be summed along some dimensions), or non-additive (ratios, percentages)."
    },
    {
        "question": "What is data deduplication?",
        "options": [
            "Splitting one record into multiple rows",
            "Identifying and removing or merging duplicate records in a dataset",
            "Encrypting records with a unique key per row",
            "Normalizing numeric columns to avoid repeated values"
        ],
        "answer": "Identifying and removing or merging duplicate records in a dataset",
        "category": "Data Engineering",
        "difficulty": "Easy",
        "explanation": "Data deduplication detects and eliminates redundant records caused by multiple ingestions, system migrations, or data entry errors. Techniques include exact matching (hashing), fuzzy matching (Levenshtein distance), and entity resolution. It is a critical step in data quality pipelines."
    },
    {
        "question": "What is a NoSQL database and when should it be used?",
        "options": [
            "A database that does not support queries",
            "A non-relational database optimized for flexible schemas, horizontal scaling, and specific access patterns",
            "A database that stores data without any structure",
            "An in-memory database for caching only"
        ],
        "answer": "A non-relational database optimized for flexible schemas, horizontal scaling, and specific access patterns",
        "category": "Data Engineering",
        "difficulty": "Medium",
        "explanation": "NoSQL databases (MongoDB, Cassandra, DynamoDB, Redis) trade ACID guarantees for scalability and schema flexibility. They come in four types: document, key-value, wide-column, and graph. They excel at high-write throughput, flexible/evolving schemas, and queries designed around specific access patterns."
    },
    {
        "question": "What is backfilling in data pipelines?",
        "options": [
            "Adding default values to NULL columns in production tables",
            "Reprocessing historical data for a pipeline that was newly created or fixed",
            "Filling disk space with dummy data for capacity testing",
            "Populating a staging table before swapping it with production"
        ],
        "answer": "Reprocessing historical data for a pipeline that was newly created or fixed",
        "category": "Data Engineering",
        "difficulty": "Medium",
        "explanation": "Backfilling runs a pipeline over historical date ranges, either when deploying a new pipeline (to populate historical data) or after fixing a bug (to correct past records). Idempotent pipelines that support date-range parameterization make backfilling safe and straightforward."
    },
    {
        "question": "What is Apache Flink?",
        "options": [
            "A batch processing framework for Hadoop clusters",
            "A distributed stream processing framework designed for stateful computations over unbounded data streams",
            "A columnar file format similar to Parquet",
            "A workflow orchestration tool that replaces Apache Airflow"
        ],
        "answer": "A distributed stream processing framework designed for stateful computations over unbounded data streams",
        "category": "Data Engineering",
        "difficulty": "Hard",
        "explanation": "Apache Flink is a stream-first processing engine that handles both bounded (batch) and unbounded (streaming) data with exactly-once semantics, event-time processing, and low latency. It is widely used for real-time analytics, fraud detection, and complex event processing at companies like Alibaba and Netflix."
    },
    {
        "question": "What is data serialization and why does it matter in pipelines?",
        "options": [
            "Ordering records sequentially before loading them into a database",
            "Converting data structures into a storable or transmittable format (bytes) that can be reconstructed later",
            "Compressing data to reduce network bandwidth",
            "Assigning sequence numbers to pipeline runs for ordering"
        ],
        "answer": "Converting data structures into a storable or transmittable format (bytes) that can be reconstructed later",
        "category": "Data Engineering",
        "difficulty": "Medium",
        "explanation": "Serialization formats (JSON, Avro, Protobuf, Parquet) determine how data is encoded for storage or transmission. Avro and Protobuf are schema-based, compact binary formats preferred in high-throughput pipelines. Format choice impacts performance, schema evolution support, and interoperability between pipeline components."
    },
    {
        "question": "What is a data lakehouse?",
        "options": [
            "A physical data center combining lake and warehouse hardware",
            "An architecture combining the low-cost storage of a data lake with the ACID transactions and query performance of a data warehouse",
            "A data lake managed exclusively by a third-party vendor",
            "A small data warehouse for a single department"
        ],
        "answer": "An architecture combining the low-cost storage of a data lake with the ACID transactions and query performance of a data warehouse",
        "category": "Data Engineering",
        "difficulty": "Hard",
        "explanation": "The lakehouse pattern (popularized by Databricks with Delta Lake, and also Apache Iceberg and Hudi) adds a transactional metadata layer over object storage, enabling ACID transactions, schema enforcement, time travel, and BI tool compatibility on top of cheap S3/GCS/ADLS storage."
    },
    {
        "question": "What is the purpose of an index in a database?",
        "options": [
            "To enforce uniqueness constraints on a column",
            "A data structure that speeds up row retrieval by allowing the database to avoid full table scans",
            "To compress table data to reduce storage costs",
            "To automatically back up modified rows to a recovery log"
        ],
        "answer": "A data structure that speeds up row retrieval by allowing the database to avoid full table scans",
        "category": "Data Engineering",
        "difficulty": "Easy",
        "explanation": "Indexes (B-tree, hash, bitmap) allow the database engine to locate rows matching a WHERE condition without scanning every row. While they dramatically speed up reads, they slow down writes and consume storage. Choosing what to index requires balancing read vs. write workload patterns."
    },
    {
        "question": "What is observability in data pipelines?",
        "options": [
            "The ability to view raw data before it is transformed",
            "Monitoring pipelines through metrics, logs, and data quality checks to detect and diagnose failures proactively",
            "Granting business users read-only access to pipeline code",
            "Tracking how long each SQL query takes to execute"
        ],
        "answer": "Monitoring pipelines through metrics, logs, and data quality checks to detect and diagnose failures proactively",
        "category": "Data Engineering",
        "difficulty": "Hard",
        "explanation": "Data pipeline observability goes beyond uptime monitoring to track data freshness, volume anomalies, schema changes, and quality degradation. Tools like Monte Carlo, Bigeye, and Datafold automate anomaly detection and lineage, helping teams catch issues before downstream consumers are impacted."
    },
    {
        "question": "What is a data contract?",
        "options": [
            "A legal agreement between companies sharing proprietary datasets",
            "A formal agreement between data producers and consumers defining schema, SLAs, and quality expectations",
            "An SLA guaranteeing 99.9% pipeline uptime",
            "An API specification for accessing a database"
        ],
        "answer": "A formal agreement between data producers and consumers defining schema, SLAs, and quality expectations",
        "category": "Data Engineering",
        "difficulty": "Hard",
        "explanation": "Data contracts formalize the interface between upstream data producers (application teams, source systems) and downstream consumers (analytics, ML). They specify schema, semantics, quality guarantees, and change management processes — preventing silent breaking changes that cause downstream failures."
    },
    {
        "question": "What is the difference between a hot path and a cold path in a Lambda architecture?",
        "options": [
            "Hot path uses SSDs; cold path uses HDDs",
            "Hot path processes data in real-time for low-latency results; cold path reprocesses historical data in batch for accuracy",
            "Hot path encrypts data; cold path stores it in plaintext",
            "Hot path handles structured data; cold path handles unstructured data"
        ],
        "answer": "Hot path processes data in real-time for low-latency results; cold path reprocesses historical data in batch for accuracy",
        "category": "Data Engineering",
        "difficulty": "Hard",
        "explanation": "Lambda architecture has three layers: speed (hot path using Kafka/Flink for real-time approximate results), batch (cold path using Spark for accurate historical reprocessing), and serving (merging both views). The Kappa architecture simplifies this by using only a streaming layer for both real-time and reprocessing."
    },
    {
        "question": "What is data masking?",
        "options": [
            "Hiding low-performing metrics from dashboards",
            "Obfuscating sensitive data by replacing it with realistic but fictitious values for non-production use",
            "Applying row-level security filters based on user roles",
            "Compressing binary data to make it unreadable without a key"
        ],
        "answer": "Obfuscating sensitive data by replacing it with realistic but fictitious values for non-production use",
        "category": "Data Engineering",
        "difficulty": "Medium",
        "explanation": "Data masking (static, dynamic, or on-the-fly) protects sensitive PII by substituting real values with anonymized equivalents — e.g., replacing real names, SSNs, and credit card numbers with fake but format-valid data. It enables safe use of production-like data in development, testing, and analytics environments."
    },
    {
        "question": "What is eventual consistency in distributed data systems?",
        "options": [
            "A guarantee that all transactions complete within a fixed time window",
            "A model where replicas may temporarily diverge but will converge to the same value given no new updates",
            "A consistency level requiring all nodes to confirm a write before returning success",
            "An indexing strategy that updates asynchronously after a commit"
        ],
        "answer": "A model where replicas may temporarily diverge but will converge to the same value given no new updates",
        "category": "Data Engineering",
        "difficulty": "Hard",
        "explanation": "Eventual consistency (used by DynamoDB, Cassandra, CouchDB) sacrifices strong consistency for availability and partition tolerance (AP systems per CAP theorem). Replicas may serve stale reads temporarily, but will eventually synchronize. It is acceptable for many use cases like shopping carts, social feeds, and analytics counters."
    },
    {
        "question": "What is a snowflake schema in data warehousing?",
        "options": [
            "A schema designed exclusively for Snowflake cloud warehouse",
            "An extension of the star schema where dimension tables are further normalized into sub-dimensions",
            "A schema pattern using only a single table with all columns flattened",
            "A schema distributed across multiple geographic regions"
        ],
        "answer": "An extension of the star schema where dimension tables are further normalized into sub-dimensions",
        "category": "Data Engineering",
        "difficulty": "Medium",
        "explanation": "A snowflake schema normalizes dimension tables into multiple related tables (e.g., a Product dimension split into Product, Category, and Subcategory tables). This reduces storage redundancy but requires more JOINs than a star schema, making queries more complex. It is less common in practice than the star schema."
    },
    {
        "question": "What is data skew in distributed processing and why is it a problem?",
        "options": [
            "When data values are statistically non-normal in distribution",
            "When data is unevenly distributed across partitions, causing some tasks to run much longer than others",
            "When timestamps in a dataset are out of chronological order",
            "When column data types do not match the declared schema"
        ],
        "answer": "When data is unevenly distributed across partitions, causing some tasks to run much longer than others",
        "category": "Data Engineering",
        "difficulty": "Hard",
        "explanation": "Data skew in Spark or distributed systems occurs when certain partition keys (e.g., a popular user ID) hold far more data than others. This creates hot partitions where a few tasks run for hours while others finish in seconds, bottlenecking the whole job. Solutions include salting keys, repartitioning, or using broadcast joins."
    },
    {
        "question": "What is the role of an activation function in a neural network?",
        "options": [
            "To initialize weights",
            "To introduce non-linearity into the network",
            "To normalize inputs",
            "To compute the loss"
        ],
        "answer": "To introduce non-linearity into the network",
        "category": "Deep Learning",
        "difficulty": "Easy",
        "explanation": "Without non-linear activation functions, stacking multiple layers would still produce a linear model. Activations like ReLU, sigmoid, and tanh enable neural networks to learn complex, non-linear relationships."
    },
    {
        "question": "What does CNN stand for in deep learning?",
        "options": [
            "Cyclic Neural Network",
            "Convolutional Neural Network",
            "Clustered Node Network",
            "Connected Neuron Network"
        ],
        "answer": "Convolutional Neural Network",
        "category": "Deep Learning",
        "difficulty": "Easy",
        "explanation": "CNNs use convolutional layers with learnable filters to automatically detect spatial hierarchies of features (edges → textures → objects), making them highly effective for image and video tasks."
    },
    {
        "question": "What problem does the Dropout technique address in neural networks?",
        "options": [
            "Underfitting",
            "Slow training",
            "Overfitting",
            "Vanishing gradients"
        ],
        "answer": "Overfitting",
        "category": "Deep Learning",
        "difficulty": "Easy",
        "explanation": "Dropout randomly sets a fraction of neurons to zero during each training step, preventing neurons from co-adapting and forcing the network to learn more robust, redundant representations — acting as an ensemble of many sub-networks."
    },
    {
        "question": "What is the vanishing gradient problem?",
        "options": [
            "Gradients explode to infinity during backpropagation",
            "Gradients become extremely small, causing early layers to barely update",
            "The loss function returns NaN values",
            "Weights converge to zero in the output layer"
        ],
        "answer": "Gradients become extremely small, causing early layers to barely update",
        "category": "Deep Learning",
        "difficulty": "Medium",
        "explanation": "In deep networks, gradients are multiplied through many layers during backpropagation. With saturating activations (like sigmoid), gradients shrink exponentially, making it hard to train early layers. ReLU and residual connections help mitigate this."
    },
    {
        "question": "What is the key innovation in ResNet (Residual Networks)?",
        "options": [
            "Using depthwise separable convolutions",
            "Skip connections that allow gradients to bypass layers",
            "Replacing all activations with linear functions",
            "Using capsule layers instead of convolutional layers"
        ],
        "answer": "Skip connections that allow gradients to bypass layers",
        "category": "Deep Learning",
        "difficulty": "Medium",
        "explanation": "ResNet introduces shortcut/skip connections that add the input of a block directly to its output (F(x) + x). This allows gradients to flow directly through the network, enabling training of very deep networks (100+ layers) without vanishing gradients."
    },
    {
        "question": "In an LSTM, what is the purpose of the forget gate?",
        "options": [
            "To add new information to the cell state",
            "To decide what information to remove from the cell state",
            "To control the output of the cell",
            "To initialize the hidden state"
        ],
        "answer": "To decide what information to remove from the cell state",
        "category": "Deep Learning",
        "difficulty": "Medium",
        "explanation": "The forget gate in an LSTM uses a sigmoid function to output values between 0 and 1 for each element of the cell state. A value near 0 means 'forget this', and near 1 means 'keep this', allowing the network to selectively retain long-term memory."
    },
    {
        "question": "What does 'transfer learning' mean in deep learning?",
        "options": [
            "Moving a model from CPU to GPU",
            "Converting a regression model to a classification model",
            "Reusing a pre-trained model's weights as a starting point for a new task",
            "Transferring data between training and validation sets"
        ],
        "answer": "Reusing a pre-trained model's weights as a starting point for a new task",
        "category": "Deep Learning",
        "difficulty": "Medium",
        "explanation": "Transfer learning leverages knowledge from a model trained on a large dataset (e.g., ImageNet, GPT pre-training) and fine-tunes it for a specific downstream task, drastically reducing required training data and compute."
    },
    {
        "question": "What is the core idea behind the Transformer architecture?",
        "options": [
            "Using recurrent layers to process sequences step by step",
            "Using self-attention to relate all positions in a sequence simultaneously",
            "Using 1D convolutions over the sequence dimension",
            "Using capsule networks to encode spatial hierarchies"
        ],
        "answer": "Using self-attention to relate all positions in a sequence simultaneously",
        "category": "Deep Learning",
        "difficulty": "Hard",
        "explanation": "Transformers replace recurrence with self-attention, computing relationships between all pairs of positions in one pass. This enables full parallelization, captures long-range dependencies better, and scales extremely well — forming the basis of GPT, BERT, and modern LLMs."
    },
    {
        "question": "What distinguishes Batch Normalization from Layer Normalization?",
        "options": [
            "Batch Norm normalizes across the batch dimension; Layer Norm normalizes across the feature dimension",
            "Layer Norm is used in CNNs; Batch Norm is used in RNNs",
            "Batch Norm uses learnable parameters; Layer Norm does not",
            "They are identical but with different names"
        ],
        "answer": "Batch Norm normalizes across the batch dimension; Layer Norm normalizes across the feature dimension",
        "category": "Deep Learning",
        "difficulty": "Hard",
        "explanation": "BatchNorm normalizes over the batch for each feature, which behaves poorly with small batches or in sequence models. LayerNorm normalizes across all features for each single example, making it stable for Transformers and RNNs regardless of batch size."
    },
    {
        "question": "What is backpropagation used for in neural networks?",
        "options": [
            "To initialize the weights of the network",
            "To compute gradients of the loss with respect to each weight",
            "To normalize inputs before training",
            "To select the best activation function"
        ],
        "answer": "To compute gradients of the loss with respect to each weight",
        "category": "Deep Learning",
        "difficulty": "Easy",
        "explanation": "Backpropagation applies the chain rule to efficiently compute the gradient of the loss function with respect to every weight in the network. These gradients are then used by an optimizer (e.g., SGD, Adam) to update the weights and minimize loss."
    },
    {
        "question": "What is the ReLU activation function?",
        "options": [
            "A function that outputs values between -1 and 1",
            "A function that returns the input if positive, and zero otherwise",
            "A function that outputs probabilities summing to 1",
            "A smooth approximation of the sigmoid function"
        ],
        "answer": "A function that returns the input if positive, and zero otherwise",
        "category": "Deep Learning",
        "difficulty": "Easy",
        "explanation": "ReLU (Rectified Linear Unit): f(x) = max(0, x). It is computationally cheap, avoids the saturation problem of sigmoid/tanh, and is the most widely used activation in hidden layers. Its main drawback is the 'dying ReLU' problem where neurons can get stuck outputting zero."
    },
    {
        "question": "What is an epoch in neural network training?",
        "options": [
            "A single weight update step",
            "One complete pass through the entire training dataset",
            "The time taken to train one batch",
            "The number of layers in the network"
        ],
        "answer": "One complete pass through the entire training dataset",
        "category": "Deep Learning",
        "difficulty": "Easy",
        "explanation": "An epoch is one full pass through all training samples. Training typically runs for many epochs, with the model seeing the same data multiple times. The number of epochs is a hyperparameter — too few leads to underfitting, too many to overfitting."
    },
    {
        "question": "What does 'batch size' refer to in deep learning?",
        "options": [
            "The total number of training samples",
            "The number of samples processed in a single weight update step",
            "The number of layers in the network",
            "The number of neurons in the output layer"
        ],
        "answer": "The number of samples processed in a single weight update step",
        "category": "Deep Learning",
        "difficulty": "Easy",
        "explanation": "Batch size determines how many training examples are used to estimate the gradient before updating weights. Larger batches give more accurate gradient estimates but use more memory. Mini-batch SGD (32-256 samples) is the standard trade-off between noise and efficiency."
    },
    {
        "question": "What is the purpose of the softmax function in the output layer?",
        "options": [
            "To introduce non-linearity in hidden layers",
            "To convert raw scores into a probability distribution over classes",
            "To normalize the input features",
            "To compute the gradient of the cross-entropy loss"
        ],
        "answer": "To convert raw scores into a probability distribution over classes",
        "category": "Deep Learning",
        "difficulty": "Medium",
        "explanation": "Softmax exponentiates each logit and normalizes by the sum, producing values between 0 and 1 that sum to 1. It is used in multiclass classification output layers and is paired with cross-entropy loss for training."
    },
    {
        "question": "What is weight initialization and why does it matter?",
        "options": [
            "Setting weights to zero to ensure symmetry breaking",
            "Starting weights at appropriate values to avoid vanishing/exploding gradients and ensure stable training",
            "Randomly shuffling the weights after each epoch",
            "Setting all weights equal to the learning rate"
        ],
        "answer": "Starting weights at appropriate values to avoid vanishing/exploding gradients and ensure stable training",
        "category": "Deep Learning",
        "difficulty": "Medium",
        "explanation": "Poor initialization (all zeros or too-large values) causes vanishing or exploding gradients from the start. Methods like Xavier/Glorot (for tanh/sigmoid) and He initialization (for ReLU) scale weights based on layer size to maintain stable gradient flow during early training."
    },
    {
        "question": "What is the difference between a GRU and an LSTM?",
        "options": [
            "GRUs have an extra output gate compared to LSTMs",
            "GRUs combine the forget and input gates into an update gate and have no separate cell state, making them simpler",
            "LSTMs are used for images; GRUs are used for text",
            "GRUs are deeper networks; LSTMs are shallower"
        ],
        "answer": "GRUs combine the forget and input gates into an update gate and have no separate cell state, making them simpler",
        "category": "Deep Learning",
        "difficulty": "Medium",
        "explanation": "GRUs (Gated Recurrent Units) simplify LSTMs by merging the forget and input gates into a single update gate and eliminating the separate cell state. GRUs have fewer parameters, train faster, and often match LSTM performance on smaller datasets."
    },
    {
        "question": "What is depthwise separable convolution?",
        "options": [
            "A convolution that only operates in the depth (channel) dimension",
            "A factored convolution that applies spatial filtering and channel mixing separately, reducing parameters",
            "A convolution with a kernel larger than the input",
            "A type of pooling operation applied channel-wise"
        ],
        "answer": "A factored convolution that applies spatial filtering and channel mixing separately, reducing parameters",
        "category": "Deep Learning",
        "difficulty": "Medium",
        "explanation": "Depthwise separable convolution (used in MobileNet, Xception) splits standard convolution into: a depthwise step (spatial filtering per channel) and a pointwise step (1x1 conv to mix channels). This achieves similar accuracy with 8-9x fewer parameters."
    },
    {
        "question": "What problem does Attention solve in sequence-to-sequence models?",
        "options": [
            "It replaces the need for an encoder entirely",
            "It allows the decoder to selectively focus on relevant encoder states at each step, addressing the fixed-length bottleneck",
            "It speeds up training by parallelizing RNN computation",
            "It prevents overfitting in sequence models"
        ],
        "answer": "It allows the decoder to selectively focus on relevant encoder states at each step, addressing the fixed-length bottleneck",
        "category": "Deep Learning",
        "difficulty": "Hard",
        "explanation": "Classic seq2seq compressed the entire input into a fixed-length context vector, losing information for long sequences. The attention mechanism lets the decoder compute a dynamic weighted sum over all encoder hidden states, attending to relevant parts at each step — a precursor to Transformers."
    },
    {
        "question": "What is knowledge distillation in deep learning?",
        "options": [
            "Extracting symbolic rules from a trained neural network",
            "Training a small student model to mimic the soft outputs of a larger teacher model",
            "Compressing weights using quantization techniques",
            "Transferring weights from one task to another"
        ],
        "answer": "Training a small student model to mimic the soft outputs of a larger teacher model",
        "category": "Deep Learning",
        "difficulty": "Hard",
        "explanation": "Knowledge distillation trains a compact student network to match the teacher's softened probability outputs (soft labels), which contain richer information than hard labels. The student learns to approximate the teacher's generalization, enabling model compression without large accuracy loss."
    },
    {
        "question": "What is gradient clipping and when is it used?",
        "options": [
            "Removing neurons with near-zero gradients to prune the network",
            "Capping gradient magnitudes during backpropagation to prevent exploding gradients",
            "Clipping weights to a fixed range after each update",
            "Zeroing gradients for frozen layers in transfer learning"
        ],
        "answer": "Capping gradient magnitudes during backpropagation to prevent exploding gradients",
        "category": "Deep Learning",
        "difficulty": "Hard",
        "explanation": "In deep or recurrent networks, gradients can grow exponentially (exploding gradients), destabilizing training. Gradient clipping either rescales the gradient norm to a threshold or clips component-wise. It is widely used in RNN/LSTM training and transformer fine-tuning."
    },
    {
        "question": "What is a hyperparameter in deep learning?",
        "options": [
            "A weight learned during training",
            "A configuration value set before training that controls the learning process",
            "The output of the final layer",
            "A parameter updated by backpropagation"
        ],
        "answer": "A configuration value set before training that controls the learning process",
        "category": "Deep Learning",
        "difficulty": "Easy",
        "explanation": "Hyperparameters (e.g., learning rate, batch size, number of layers, dropout rate) are set by the practitioner before training begins and are not updated by backpropagation. Choosing good hyperparameters is crucial and is often done via grid search, random search, or Bayesian optimization."
    },
    {
        "question": "What is the purpose of a pooling layer in a CNN?",
        "options": [
            "To increase the spatial resolution of feature maps",
            "To apply non-linearity after convolution",
            "To reduce spatial dimensions and provide translation invariance",
            "To normalize activations across channels"
        ],
        "answer": "To reduce spatial dimensions and provide translation invariance",
        "category": "Deep Learning",
        "difficulty": "Easy",
        "explanation": "Pooling (max or average) downsamples feature maps by summarizing local regions, reducing computation and parameters in subsequent layers. Max pooling also provides a degree of translation invariance — the feature is detected even if it shifts slightly in position."
    },
    {
        "question": "What does RNN stand for and what is it primarily used for?",
        "options": [
            "Recursive Node Network, used for tree-structured data",
            "Recurrent Neural Network, used for sequential and time-series data",
            "Reinforced Neural Network, used for reward-based learning",
            "Residual Neural Network, used for image classification"
        ],
        "answer": "Recurrent Neural Network, used for sequential and time-series data",
        "category": "Deep Learning",
        "difficulty": "Easy",
        "explanation": "RNNs process sequences by maintaining a hidden state that is updated at each time step. They share weights across time, making them suitable for variable-length sequences like text, speech, and time-series. However, they struggle with long-range dependencies due to vanishing gradients."
    },
    {
        "question": "What is the learning rate in neural network training?",
        "options": [
            "The fraction of data used for training vs. validation",
            "The speed at which the network memorizes the training set",
            "A scalar that controls how large a step the optimizer takes when updating weights",
            "The ratio of neurons that are active at any given time"
        ],
        "answer": "A scalar that controls how large a step the optimizer takes when updating weights",
        "category": "Deep Learning",
        "difficulty": "Easy",
        "explanation": "The learning rate multiplies the gradient to determine the size of each weight update. Too high causes divergence; too low causes extremely slow convergence. Learning rate schedules (warm-up, decay, cyclical) and adaptive optimizers (Adam) help manage this critical hyperparameter."
    },
    {
        "question": "What is the Adam optimizer?",
        "options": [
            "A variant of SGD that uses a fixed momentum term",
            "An optimizer combining momentum and adaptive per-parameter learning rates",
            "An optimizer that uses second-order derivatives (Hessian)",
            "A gradient-free optimization method for neural networks"
        ],
        "answer": "An optimizer combining momentum and adaptive per-parameter learning rates",
        "category": "Deep Learning",
        "difficulty": "Medium",
        "explanation": "Adam (Adaptive Moment Estimation) maintains exponential moving averages of both the gradients (first moment) and squared gradients (second moment) to adapt the learning rate per parameter. It combines the benefits of RMSProp and momentum, and is the most widely used optimizer in practice."
    },
    {
        "question": "What is data augmentation and why is it used?",
        "options": [
            "Increasing the model size to handle more data",
            "Artificially expanding the training dataset by applying transformations to existing samples",
            "Collecting additional labeled data from external sources",
            "Duplicating the training set to balance class frequencies"
        ],
        "answer": "Artificially expanding the training dataset by applying transformations to existing samples",
        "category": "Deep Learning",
        "difficulty": "Easy",
        "explanation": "Data augmentation applies transforms like random crops, flips, rotations, color jitter, and noise to training images. This increases effective dataset size, reduces overfitting, and improves generalization, especially when labeled data is scarce."
    },
    {
        "question": "What is L2 regularization (weight decay)?",
        "options": [
            "Adding the absolute values of weights to the loss function",
            "Adding the squared sum of weights to the loss to penalize large weights",
            "Randomly zeroing weights at each training step",
            "Normalizing each weight vector to unit length"
        ],
        "answer": "Adding the squared sum of weights to the loss to penalize large weights",
        "category": "Deep Learning",
        "difficulty": "Medium",
        "explanation": "L2 regularization adds λ * Σw² to the loss, encouraging smaller weight magnitudes. This penalizes overly complex models and reduces overfitting. In gradient descent, it is equivalent to decaying the weights by a factor slightly less than 1 at each step (hence 'weight decay')."
    },
    {
        "question": "What is a generative adversarial network (GAN)?",
        "options": [
            "A network that generates labels for unlabeled data",
            "A framework where a generator and discriminator compete: the generator creates fake samples and the discriminator tries to detect them",
            "A network that generates adversarial perturbations to fool other models",
            "A reinforcement learning framework where two agents compete"
        ],
        "answer": "A framework where a generator and discriminator compete: the generator creates fake samples and the discriminator tries to detect them",
        "category": "Deep Learning",
        "difficulty": "Medium",
        "explanation": "GANs consist of two networks trained simultaneously: a generator G that maps noise to data (e.g., images) and a discriminator D that distinguishes real from generated data. The adversarial training drives G to produce increasingly realistic outputs until D can no longer tell them apart."
    },
    {
        "question": "What is the difference between underfitting and overfitting?",
        "options": [
            "Underfitting means too many parameters; overfitting means too few",
            "Underfitting means the model is too simple and fails to capture patterns; overfitting means it memorizes training data and fails to generalize",
            "Underfitting occurs only in CNNs; overfitting occurs only in RNNs",
            "Both mean the model has converged to a poor local minimum"
        ],
        "answer": "Underfitting means the model is too simple and fails to capture patterns; overfitting means it memorizes training data and fails to generalize",
        "category": "Deep Learning",
        "difficulty": "Easy",
        "explanation": "Underfitting: high bias, poor performance on both train and test sets — the model is too simple. Overfitting: low training loss but high test loss — the model has memorized noise in training data. The goal is to find the sweet spot with good generalization."
    },
    {
        "question": "What is the purpose of a validation set during training?",
        "options": [
            "To compute the final test accuracy of the model",
            "To tune hyperparameters and monitor generalization without contaminating the test set",
            "To augment the training set with additional samples",
            "To normalize input features before training"
        ],
        "answer": "To tune hyperparameters and monitor generalization without contaminating the test set",
        "category": "Deep Learning",
        "difficulty": "Easy",
        "explanation": "The validation set is a held-out subset used during training to evaluate generalization, select hyperparameters (e.g., learning rate, architecture), and apply early stopping. It must not be used to select the final model evaluation — that's the role of the separate test set."
    },
    {
        "question": "What is positional encoding in the Transformer model?",
        "options": [
            "A learned embedding added to word tokens to indicate their position in the vocabulary",
            "A sinusoidal or learned signal added to token embeddings to inject sequence order information",
            "A masking technique to prevent the model from attending to future tokens",
            "A normalization layer applied before the attention module"
        ],
        "answer": "A sinusoidal or learned signal added to token embeddings to inject sequence order information",
        "category": "Deep Learning",
        "difficulty": "Hard",
        "explanation": "Since self-attention has no inherent sense of order, positional encodings are added to input embeddings to encode each token's position. The original Transformer uses fixed sinusoidal functions of different frequencies; later models (BERT, GPT) use learned positional embeddings."
    },
    {
        "question": "What is the purpose of the encoder in an autoencoder?",
        "options": [
            "To classify the input into one of many categories",
            "To compress the input into a lower-dimensional latent representation",
            "To generate new samples from random noise",
            "To upsample feature maps to the original input size"
        ],
        "answer": "To compress the input into a lower-dimensional latent representation",
        "category": "Deep Learning",
        "difficulty": "Medium",
        "explanation": "In an autoencoder, the encoder maps high-dimensional input to a compact bottleneck (latent space). The decoder then reconstructs the input from this representation. Autoencoders are used for dimensionality reduction, anomaly detection, and pre-training representations."
    },
    {
        "question": "What is multi-head attention in Transformers?",
        "options": [
            "Applying attention multiple times sequentially to the same input",
            "Running multiple attention mechanisms in parallel with different learned projections, then concatenating results",
            "Using multiple encoder heads stacked on top of each other",
            "Averaging the outputs of multiple Transformer models"
        ],
        "answer": "Running multiple attention mechanisms in parallel with different learned projections, then concatenating results",
        "category": "Deep Learning",
        "difficulty": "Hard",
        "explanation": "Multi-head attention projects Q, K, V into h different subspaces, computes scaled dot-product attention in each head independently, then concatenates and linearly projects the results. Different heads can focus on different types of relationships (syntactic, semantic, coreference) simultaneously."
    },
    {
        "question": "What is a loss function in deep learning?",
        "options": [
            "A function that measures how well the model's predictions match the true labels",
            "A function used to initialize network weights",
            "A regularization technique to reduce overfitting",
            "A function that determines the learning rate schedule"
        ],
        "answer": "A function that measures how well the model's predictions match the true labels",
        "category": "Deep Learning",
        "difficulty": "Easy",
        "explanation": "The loss function quantifies the discrepancy between predictions and ground truth. Common losses include MSE for regression, cross-entropy for classification, and contrastive loss for metric learning. The optimizer minimizes this scalar signal during training via backpropagation."
    },
    {
        "question": "What is the exploding gradient problem?",
        "options": [
            "Gradients that diminish to near-zero in the early layers of deep networks",
            "Gradients that grow exponentially during backpropagation, causing unstable weight updates",
            "The loss function diverging due to a bad learning rate",
            "Weights oscillating around the minimum without converging"
        ],
        "answer": "Gradients that grow exponentially during backpropagation, causing unstable weight updates",
        "category": "Deep Learning",
        "difficulty": "Medium",
        "explanation": "Exploding gradients occur when gradient magnitudes grow exponentially as they flow back through many layers, resulting in very large weight updates that destabilize training (NaN or Inf values). It is mitigated by gradient clipping, careful initialization, and batch normalization."
    },
    {
        "question": "What is early stopping?",
        "options": [
            "Stopping training when the loss reaches exactly zero",
            "Terminating training when validation performance stops improving to prevent overfitting",
            "Removing layers from the network to speed up training",
            "Stopping backpropagation after a fixed number of gradient steps"
        ],
        "answer": "Terminating training when validation performance stops improving to prevent overfitting",
        "category": "Deep Learning",
        "difficulty": "Easy",
        "explanation": "Early stopping monitors validation loss/accuracy during training and halts when it stops improving (with some patience). It prevents overfitting by choosing the model checkpoint with the best generalization, effectively acting as a form of regularization."
    },
    {
        "question": "What does 'fine-tuning' mean in the context of pre-trained models?",
        "options": [
            "Training a model from scratch with a very small learning rate",
            "Continuing training of a pre-trained model on a new, task-specific dataset by updating some or all weights",
            "Freezing all weights of a pre-trained model and only adding a new classification head",
            "Pruning redundant neurons to reduce model size"
        ],
        "answer": "Continuing training of a pre-trained model on a new, task-specific dataset by updating some or all weights",
        "category": "Deep Learning",
        "difficulty": "Medium",
        "explanation": "Fine-tuning adapts a pre-trained model to a new task by continuing gradient updates on task-specific data, typically with a lower learning rate to preserve general knowledge. It is distinct from feature extraction, where the pre-trained weights are frozen and only the new head is trained."
    },
    {
        "question": "What is the main advantage of using GPUs for deep learning?",
        "options": [
            "GPUs have more RAM than CPUs",
            "GPUs can perform massive parallel computations, dramatically accelerating matrix operations central to training",
            "GPUs have higher clock speeds than CPUs",
            "GPUs consume less power than CPUs during training"
        ],
        "answer": "GPUs can perform massive parallel computations, dramatically accelerating matrix operations central to training",
        "category": "Deep Learning",
        "difficulty": "Easy",
        "explanation": "Neural network training relies heavily on matrix multiplications, which are embarrassingly parallel. GPUs contain thousands of small cores optimized for these operations, providing 10-100x speedups over CPUs. Tensor Cores in modern GPUs (NVIDIA A100, H100) further accelerate mixed-precision training."
    },
    {
        "question": "What is the difference between semantic segmentation and instance segmentation?",
        "options": [
            "Semantic segmentation labels each pixel with a class; instance segmentation distinguishes between individual objects of the same class",
            "Instance segmentation is faster and less accurate than semantic segmentation",
            "Semantic segmentation uses bounding boxes; instance segmentation uses pixel masks",
            "They are the same task with different names"
        ],
        "answer": "Semantic segmentation labels each pixel with a class; instance segmentation distinguishes between individual objects of the same class",
        "category": "Deep Learning",
        "difficulty": "Medium",
        "explanation": "In semantic segmentation, every pixel is assigned a class label (e.g., all cars = 'car'). Instance segmentation goes further by distinguishing individual objects — each car gets a unique mask. Panoptic segmentation combines both, labeling all pixels with class and instance IDs."
    },
    {
        "question": "What is weight sharing in neural networks?",
        "options": [
            "Distributing model weights across multiple GPUs for parallel training",
            "Using the same set of weights for different positions or parts of the input",
            "Sharing weights between two different models during knowledge distillation",
            "Reusing weights from a previous epoch to speed up convergence"
        ],
        "answer": "Using the same set of weights for different positions or parts of the input",
        "category": "Deep Learning",
        "difficulty": "Medium",
        "explanation": "Weight sharing — used in CNNs (same filter applied across spatial positions) and RNNs (same weights across time steps) — drastically reduces the number of parameters, enforces translation/temporal equivariance, and improves generalization by exploiting structural priors of the data."
    },
    {
        "question": "What is the role of the discriminator in a GAN?",
        "options": [
            "To generate realistic data samples from random noise",
            "To classify inputs as real (from the dataset) or fake (from the generator)",
            "To encode images into a compact latent space",
            "To select the best generated sample from multiple candidates"
        ],
        "answer": "To classify inputs as real (from the dataset) or fake (from the generator)",
        "category": "Deep Learning",
        "difficulty": "Medium",
        "explanation": "The discriminator is a binary classifier trained to distinguish real data from generated (fake) samples. Its loss signal drives the generator to produce increasingly realistic outputs. A well-trained discriminator forces the generator to match the true data distribution."
    },
    {
        "question": "What is a variational autoencoder (VAE)?",
        "options": [
            "An autoencoder with variable-length latent representations",
            "A generative model that encodes inputs as distributions in latent space and samples to decode",
            "An autoencoder trained with adversarial loss instead of reconstruction loss",
            "A deterministic autoencoder with regularized bottleneck weights"
        ],
        "answer": "A generative model that encodes inputs as distributions in latent space and samples to decode",
        "category": "Deep Learning",
        "difficulty": "Hard",
        "explanation": "VAEs encode inputs as Gaussian distributions (mean and variance) in latent space rather than deterministic vectors. During training, a sample is drawn from this distribution and decoded. A KL divergence term regularizes the latent space toward a standard normal, enabling smooth interpolation and generation."
    },
    {
        "question": "What is causal (masked) self-attention used for in language models?",
        "options": [
            "To allow each token to attend to all tokens in the sequence bidirectionally",
            "To prevent each token from attending to future tokens, enabling autoregressive generation",
            "To mask padding tokens so they do not contribute to attention scores",
            "To prevent attention to tokens from a different sentence in the batch"
        ],
        "answer": "To prevent each token from attending to future tokens, enabling autoregressive generation",
        "category": "Deep Learning",
        "difficulty": "Hard",
        "explanation": "In decoder-only models (e.g., GPT), causal masking zeros out attention weights from position i to any position j > i. This ensures each token can only condition on past tokens, making the model valid for autoregressive generation where future tokens are unknown at inference time."
    },
    {
        "question": "What is neural architecture search (NAS)?",
        "options": [
            "Manually designing neural networks based on domain expertise",
            "Automatically discovering optimal network architectures using search algorithms",
            "Searching for the best hyperparameters using grid search",
            "Pruning a large network to find a smaller efficient subnetwork"
        ],
        "answer": "Automatically discovering optimal network architectures using search algorithms",
        "category": "Deep Learning",
        "difficulty": "Hard",
        "explanation": "NAS automates the design of neural network architectures by searching over a predefined space using methods like reinforcement learning, evolutionary algorithms, or gradient-based optimization (DARTS). NAS-discovered models (e.g., EfficientNet, NASNet) often outperform hand-designed architectures."
    },
    {
        "question": "What is the dying ReLU problem?",
        "options": [
            "ReLU outputs saturate at 1, causing vanishing gradients",
            "Neurons permanently output zero because their weights shift such that their input is always negative",
            "ReLU causes exploding gradients due to unbounded positive outputs",
            "ReLU becomes a linear function for large positive inputs, reducing model expressiveness"
        ],
        "answer": "Neurons permanently output zero because their weights shift such that their input is always negative",
        "category": "Deep Learning",
        "difficulty": "Medium",
        "explanation": "When a ReLU neuron's input is always negative (e.g., after a large negative weight update), it outputs zero for all inputs, and its gradient is also zero — meaning it can never recover via backpropagation. Leaky ReLU, ELU, and careful initialization help prevent this."
    },
    {
        "question": "What does 'feature map' refer to in a CNN?",
        "options": [
            "A 2D matrix mapping input pixels to output classes",
            "The output tensor produced by applying a convolutional filter to an input",
            "A lookup table of learned word embeddings",
            "A compressed representation of the network weights"
        ],
        "answer": "The output tensor produced by applying a convolutional filter to an input",
        "category": "Deep Learning",
        "difficulty": "Easy",
        "explanation": "A feature map is the activation map produced when a learned filter slides across an input image or previous feature map. Each filter detects a specific pattern; applying 64 filters produces 64 feature maps. As depth increases, feature maps encode increasingly abstract visual concepts."
    },
    {
        "question": "What is the cross-entropy loss function and when is it used?",
        "options": [
            "A loss for regression tasks measuring the mean squared error between predictions and targets",
            "A loss for classification tasks measuring the negative log-likelihood of the true class under the predicted distribution",
            "A loss that penalizes large weights to prevent overfitting",
            "A loss used in GANs to compare real and generated distributions"
        ],
        "answer": "A loss for classification tasks measuring the negative log-likelihood of the true class under the predicted distribution",
        "category": "Deep Learning",
        "difficulty": "Medium",
        "explanation": "Cross-entropy loss is defined as -Σ y_i * log(p_i) where y_i is the one-hot true label and p_i the predicted probability. For binary classification, it simplifies to binary cross-entropy. It penalizes confident wrong predictions heavily and is the standard loss for classification tasks."
    },
    {
        "question": "What is model pruning in deep learning?",
        "options": [
            "Removing entire training examples that are mislabeled",
            "Eliminating redundant or low-importance weights/neurons to reduce model size and inference cost",
            "Reducing the number of training epochs to prevent overfitting",
            "Deleting unused hidden layers from the final model architecture"
        ],
        "answer": "Eliminating redundant or low-importance weights/neurons to reduce model size and inference cost",
        "category": "Deep Learning",
        "difficulty": "Hard",
        "explanation": "Pruning removes weights (unstructured pruning) or entire neurons/filters (structured pruning) that contribute least to model output, typically based on magnitude thresholds. It is used post-training or during training to produce compact, fast models for edge deployment with minimal accuracy loss."
    },
    {
        "question": "What is the key difference between BERT and GPT in terms of Transformer architecture?",
        "options": [
            "BERT uses an encoder-only architecture with bidirectional attention; GPT uses a decoder-only architecture with causal (left-to-right) attention",
            "BERT is trained with reinforcement learning; GPT is trained with supervised learning",
            "BERT uses positional encodings; GPT does not use any positional information",
            "GPT has a larger context window because it uses cross-attention instead of self-attention"
        ],
        "answer": "BERT uses an encoder-only architecture with bidirectional attention; GPT uses a decoder-only architecture with causal (left-to-right) attention",
        "category": "Deep Learning",
        "difficulty": "Hard",
        "explanation": "BERT (Bidirectional Encoder Representations from Transformers) uses full bidirectional self-attention — each token can attend to all others — making it ideal for understanding tasks like NER and QA. GPT uses causal masking so each token only attends leftward, enabling autoregressive text generation."
    },
    {
        "question": "What is the purpose of the 1x1 convolution in deep neural networks?",
        "options": [
            "To increase the spatial resolution of feature maps",
            "To apply non-linear spatial filtering across the input",
            "To change the number of channels while mixing information across channels",
            "To replace max pooling for spatial downsampling"
        ],
        "answer": "To change the number of channels while mixing information across channels",
        "category": "Deep Learning",
        "difficulty": "Medium",
        "explanation": "A 1x1 convolution applies a learned linear combination across all channels at each spatial position, effectively acting as a channel-wise fully connected layer. It is used in Inception modules and ResNet bottlenecks to reduce or expand channel dimensions cheaply while enabling cross-channel interactions."
    },
    {
        "question": "What is algorithmic bias?",
        "options": [
            "A bug in the training code that produces incorrect gradients",
            "Systematic and unfair discrimination in model outputs toward certain groups due to biased data or design",
            "The tendency of models to prefer simpler explanations",
            "Random prediction errors evenly distributed across all groups"
        ],
        "answer": "Systematic and unfair discrimination in model outputs toward certain groups due to biased data or design",
        "category": "Ethics & Responsible AI",
        "difficulty": "Easy",
        "explanation": "Algorithmic bias occurs when a model systematically produces unfair or discriminatory outcomes for certain groups (by race, gender, age, etc.), often reflecting historical biases in training data. High-profile examples include biased hiring tools, facial recognition disparities, and discriminatory loan models."
    },
    {
        "question": "What is explainability (interpretability) in AI?",
        "options": [
            "The ability to retrain a model quickly when data changes",
            "The degree to which humans can understand and trace the reasoning behind a model's predictions",
            "The accuracy of a model on held-out test data",
            "The speed at which a model generates predictions"
        ],
        "answer": "The degree to which humans can understand and trace the reasoning behind a model's predictions",
        "category": "Ethics & Responsible AI",
        "difficulty": "Easy",
        "explanation": "Explainability (XAI) involves techniques that help humans understand why a model made a specific prediction. This is critical for regulated industries (finance, healthcare, legal), trust-building, debugging, and detecting unfair patterns. Methods include LIME, SHAP, attention visualization, and decision trees."
    },
    {
        "question": "What is SHAP (SHapley Additive exPlanations)?",
        "options": [
            "A model compression technique for deploying on edge devices",
            "A framework that assigns each feature a contribution value to a model's prediction, based on game theory",
            "A fairness metric that measures demographic parity",
            "A hyperparameter tuning library for gradient boosting"
        ],
        "answer": "A framework that assigns each feature a contribution value to a model's prediction, based on game theory",
        "category": "Ethics & Responsible AI",
        "difficulty": "Medium",
        "explanation": "SHAP uses Shapley values from cooperative game theory to fairly distribute the prediction output among features. It provides both local (per-prediction) and global (overall) feature importance that is consistent and theoretically grounded — unlike simpler importance methods."
    },
    {
        "question": "What is the difference between demographic parity and equalized odds as fairness metrics?",
        "options": [
            "Demographic parity measures individual fairness; equalized odds measures group fairness",
            "Demographic parity requires equal positive prediction rates across groups; equalized odds requires equal TPR and FPR across groups",
            "They measure the same thing but in different domains",
            "Equalized odds only applies to regression; demographic parity to classification"
        ],
        "answer": "Demographic parity requires equal positive prediction rates across groups; equalized odds requires equal TPR and FPR across groups",
        "category": "Ethics & Responsible AI",
        "difficulty": "Medium",
        "explanation": "Demographic parity mandates equal selection rates regardless of group membership. Equalized odds requires equal true positive AND false positive rates across groups, conditioning on the true label — generally a stronger, task-aware notion of fairness."
    },
    {
        "question": "What is differential privacy and how is it applied to ML?",
        "options": [
            "A method to compute gradients differentially for faster convergence",
            "A mathematical guarantee that algorithm output is statistically indistinguishable whether or not any individual's data was included",
            "A technique for removing sensitive columns from a dataset before training",
            "A way to anonymize data by replacing names with random identifiers"
        ],
        "answer": "A mathematical guarantee that algorithm output is statistically indistinguishable whether or not any individual's data was included",
        "category": "Ethics & Responsible AI",
        "difficulty": "Hard",
        "explanation": "Differential privacy adds calibrated noise (Laplace, Gaussian) to training gradients (DP-SGD) or query results, providing a formal privacy guarantee parameterized by epsilon. Lower epsilon means stronger privacy but typically lower utility. It is used by Apple, Google, and increasingly in federated learning."
    },
    {
        "question": "What is federated learning and what privacy benefit does it offer?",
        "options": [
            "Training a single large model across multiple GPU nodes in a data center",
            "Training models on decentralized devices where data never leaves the device, and only model updates are shared",
            "A technique for merging multiple independently trained models into one",
            "Using synthetic data to augment privacy-sensitive training datasets"
        ],
        "answer": "Training models on decentralized devices where data never leaves the device, and only model updates are shared",
        "category": "Ethics & Responsible AI",
        "difficulty": "Hard",
        "explanation": "Federated learning trains a shared model by aggregating gradient updates from many client devices without centralizing raw data. Each client trains locally on its private data, sends only model updates (not data) to a central server. This is used in mobile keyboards, healthcare, and finance where data privacy is paramount."
    },
    {
        "question": "What does the 'right to explanation' under the EU's GDPR require?",
        "options": [
            "That all AI models must be open-source",
            "That individuals subject to automated decisions have the right to receive a meaningful explanation of the logic involved",
            "That companies must publish their training datasets publicly",
            "That models must achieve a minimum accuracy threshold before deployment"
        ],
        "answer": "That individuals subject to automated decisions have the right to receive a meaningful explanation of the logic involved",
        "category": "Ethics & Responsible AI",
        "difficulty": "Medium",
        "explanation": "GDPR Article 22 gives individuals the right not to be subject to solely automated decisions with significant effects, and Article 13/14/15 grant the right to 'meaningful information about the logic involved.' This drives the need for explainable AI in European deployments."
    },
    {
        "question": "What is 'model cards' in responsible AI?",
        "options": [
            "Credit card-sized hardware accelerators for edge inference",
            "Structured documentation that describes a model's intended uses, performance metrics, and ethical considerations",
            "A technique for compressing neural networks into smaller parameter sets",
            "Score cards that rank AI models by benchmark performance"
        ],
        "answer": "Structured documentation that describes a model's intended uses, performance metrics, and ethical considerations",
        "category": "Ethics & Responsible AI",
        "difficulty": "Easy",
        "explanation": "Model cards, introduced by Google researchers, are short documents accompanying ML models that report on training data, evaluation results across subgroups, intended use cases, limitations, and ethical concerns. They are a key tool for transparency and are now expected practice for major model releases."
    },
    {
        "question": "What is 'data poisoning' as an AI security threat?",
        "options": [
            "Corrupting model weights by injecting noise during inference",
            "Deliberately introducing malicious or mislabeled data into a training set to degrade or manipulate model behavior",
            "Overloading a model API with requests to cause a denial-of-service",
            "Extracting private training data through repeated model queries"
        ],
        "answer": "Deliberately introducing malicious or mislabeled data into a training set to degrade or manipulate model behavior",
        "category": "Ethics & Responsible AI",
        "difficulty": "Medium",
        "explanation": "Data poisoning attacks inject carefully crafted examples into the training set to corrupt model behavior — either degrading overall accuracy or embedding backdoor triggers. This is particularly concerning in crowdsourced or continuously-learning systems where the training pipeline is not fully controlled."
    },
    {
        "question": "What is a 'backdoor attack' in machine learning?",
        "options": [
            "Gaining unauthorized access to a model's API endpoint",
            "An attack where a model behaves normally on clean inputs but misbehaves on inputs containing a specific hidden trigger",
            "Training a shadow model to replicate a target model's behavior",
            "Extracting gradient information from a black-box model"
        ],
        "answer": "An attack where a model behaves normally on clean inputs but misbehaves on inputs containing a specific hidden trigger",
        "category": "Ethics & Responsible AI",
        "difficulty": "Hard",
        "explanation": "In a backdoor (Trojan) attack, an adversary embeds a hidden trigger pattern in some training data. The model learns normal behavior generally, but whenever the trigger is present at inference, it produces an attacker-specified output. This is highly concerning for safety-critical applications."
    },
    {
        "question": "What is the primary goal of 'AI alignment' research?",
        "options": [
            "Optimizing AI models to run efficiently on specialized hardware",
            "Ensuring AI systems pursue goals that are beneficial and consistent with human values and intentions",
            "Aligning model weights across distributed training nodes for consistency",
            "Standardizing AI APIs so different frameworks are interoperable"
        ],
        "answer": "Ensuring AI systems pursue goals that are beneficial and consistent with human values and intentions",
        "category": "Ethics & Responsible AI",
        "difficulty": "Easy",
        "explanation": "AI alignment is the research field focused on ensuring that AI systems behave in ways that are safe, beneficial, and consistent with human intentions — even as they become more capable. It addresses challenges like reward hacking, goal misgeneralization, and the difficulty of specifying human values formally."
    },
    {
        "question": "What is 'reward hacking' in the context of reinforcement learning?",
        "options": [
            "Manually editing the reward function to accelerate training",
            "An agent exploiting loopholes in the reward specification to maximize reward without fulfilling the intended objective",
            "Sharing reward signals across multiple agents in a cooperative setting",
            "Applying reward shaping to guide an agent toward a desired policy faster"
        ],
        "answer": "An agent exploiting loopholes in the reward specification to maximize reward without fulfilling the intended objective",
        "category": "Ethics & Responsible AI",
        "difficulty": "Medium",
        "explanation": "Reward hacking (or reward gaming) occurs when an RL agent finds unexpected ways to maximize the reward signal that don't correspond to the designer's true intent. A classic example is a boat-racing agent spinning in circles to collect bonuses instead of finishing the race. It highlights the difficulty of reward specification."
    },
    {
        "question": "What is 'counterfactual fairness' in algorithmic decision-making?",
        "options": [
            "Ensuring predictions remain the same across different random seeds",
            "A fairness notion requiring that a decision would be the same in a counterfactual world where the individual belonged to a different demographic group",
            "Measuring model performance on counterfactual test cases not seen during training",
            "Fairness applied only to counterfactual data generated by GANs"
        ],
        "answer": "A fairness notion requiring that a decision would be the same in a counterfactual world where the individual belonged to a different demographic group",
        "category": "Ethics & Responsible AI",
        "difficulty": "Hard",
        "explanation": "Counterfactual fairness, grounded in causal inference, requires that the prediction for an individual would be the same even if their protected attribute (e.g., race, gender) had been different, holding causally non-descendant features constant. It is a stronger, causal notion of individual fairness."
    },
    {
        "question": "What is 'model transparency' and why is it important?",
        "options": [
            "The ability to see inside a neural network's memory buffers during inference",
            "Openness about how a model was built, trained, and evaluated so stakeholders can assess its trustworthiness and limitations",
            "Publishing model weights under an open-source license",
            "The mathematical property of linear models being fully interpretable"
        ],
        "answer": "Openness about how a model was built, trained, and evaluated so stakeholders can assess its trustworthiness and limitations",
        "category": "Ethics & Responsible AI",
        "difficulty": "Easy",
        "explanation": "Model transparency refers to the practice of clearly disclosing information about a model's design choices, training data, evaluation methodology, known limitations, and intended use cases. It enables informed oversight by regulators, auditors, users, and affected communities."
    },
    {
        "question": "What is LIME (Local Interpretable Model-agnostic Explanations)?",
        "options": [
            "A loss function designed for imbalanced multiclass problems",
            "A technique that explains individual predictions by approximating a complex model locally with a simpler, interpretable model",
            "A library for loading and inspecting large language model embeddings",
            "A regularization technique that penalizes model complexity globally"
        ],
        "answer": "A technique that explains individual predictions by approximating a complex model locally with a simpler, interpretable model",
        "category": "Ethics & Responsible AI",
        "difficulty": "Medium",
        "explanation": "LIME perturbs an input instance and observes how the model's predictions change, then fits a simple linear model to these perturbations locally. The linear model's coefficients provide an interpretable explanation for that specific prediction. It is model-agnostic and works with text, images, and tabular data."
    },
    {
        "question": "What is the 'automation bias' problem in human-AI collaboration?",
        "options": [
            "An AI model that performs better on automated tasks than on creative ones",
            "The tendency of human operators to over-rely on automated system recommendations, even when those recommendations are incorrect",
            "A dataset imbalance caused by over-sampling automated process logs",
            "Bias introduced when models are trained exclusively on synthetic data"
        ],
        "answer": "The tendency of human operators to over-rely on automated system recommendations, even when those recommendations are incorrect",
        "category": "Ethics & Responsible AI",
        "difficulty": "Medium",
        "explanation": "Automation bias is the propensity for humans to favor suggestions from automated decision-making systems over contradictory information without the automation. It is a major concern in high-stakes domains like medical diagnosis and aviation, where humans may approve AI-suggested errors without scrutiny."
    },
    {
        "question": "What is 'individual fairness' in machine learning?",
        "options": [
            "Ensuring equal accuracy for each individual data point in the test set",
            "The principle that similar individuals should receive similar predictions or decisions",
            "Assigning a personalized fairness threshold to each user",
            "Auditing each training example for labeling bias independently"
        ],
        "answer": "The principle that similar individuals should receive similar predictions or decisions",
        "category": "Ethics & Responsible AI",
        "difficulty": "Medium",
        "explanation": "Individual fairness requires that two individuals who are similar with respect to a task-relevant metric should receive similar model outputs. It contrasts with group fairness, which focuses on aggregate statistics across demographic groups. The challenge is defining an appropriate similarity metric."
    },
    {
        "question": "What is 'membership inference attack' in the context of ML privacy?",
        "options": [
            "An attack that infers the membership rules of a coalition in a federated system",
            "An adversarial technique that determines whether a specific data point was part of a model's training set",
            "A method to infer missing feature values for incomplete training samples",
            "Inferring model architecture by observing its outputs on test data"
        ],
        "answer": "An adversarial technique that determines whether a specific data point was part of a model's training set",
        "category": "Ethics & Responsible AI",
        "difficulty": "Hard",
        "explanation": "Membership inference attacks exploit the fact that models tend to behave differently (e.g., higher confidence, lower loss) on training data vs. unseen data. An adversary queries the model and uses these signals to infer if a target record was in the training set — a serious privacy risk for sensitive datasets."
    },
    {
        "question": "What does 'human-in-the-loop' mean in AI deployment?",
        "options": [
            "Requiring human engineers to annotate each batch of new training data",
            "A system design where human judgment is incorporated into the automated decision-making process at key points",
            "A feedback loop where users rate AI outputs to improve future recommendations",
            "An architecture where humans physically monitor GPU temperature during training"
        ],
        "answer": "A system design where human judgment is incorporated into the automated decision-making process at key points",
        "category": "Ethics & Responsible AI",
        "difficulty": "Easy",
        "explanation": "Human-in-the-loop (HITL) refers to AI systems that include a human review or approval step before consequential actions are taken. This is particularly important in high-stakes domains like medical diagnosis, content moderation, and criminal justice, where AI errors can have severe consequences."
    },
    {
        "question": "What is 'model inversion attack'?",
        "options": [
            "Reversing the parameter update direction during adversarial training",
            "An attack that reconstructs approximate training data samples by repeatedly querying a model",
            "Converting a discriminative model into a generative one",
            "Using a model's gradients to invert its normalization layers"
        ],
        "answer": "An attack that reconstructs approximate training data samples by repeatedly querying a model",
        "category": "Ethics & Responsible AI",
        "difficulty": "Hard",
        "explanation": "Model inversion attacks exploit the information encoded in model outputs to reconstruct representative samples from the training data. An adversary optimizes an input to maximize the model's confidence in a target class, effectively recovering an 'average' training example. This poses privacy risks when models are trained on sensitive data."
    },
    {
        "question": "What is 'disparate impact' in the context of AI fairness?",
        "options": [
            "When different model versions produce varying outputs on the same input",
            "When an algorithm disproportionately harms a protected group even without explicit use of the protected attribute",
            "The difference in inference latency across geographic regions",
            "Unequal model performance caused by hardware disparities between users"
        ],
        "answer": "When an algorithm disproportionately harms a protected group even without explicit use of the protected attribute",
        "category": "Ethics & Responsible AI",
        "difficulty": "Medium",
        "explanation": "Disparate impact occurs when an apparently neutral algorithm produces outcomes that adversely affect a protected group at a disproportionate rate — even without intent or explicit use of protected attributes. This can arise through proxy features (e.g., ZIP code as a proxy for race). It is a key concept in anti-discrimination law."
    },
    {
        "question": "What is 'responsible AI' as a practice within organizations?",
        "options": [
            "Using AI only for tasks that generate positive revenue",
            "A governance framework encompassing fairness, accountability, transparency, privacy, and safety throughout the AI development lifecycle",
            "Restricting AI use to research contexts and not deploying in production",
            "Ensuring AI models run within allocated compute and energy budgets"
        ],
        "answer": "A governance framework encompassing fairness, accountability, transparency, privacy, and safety throughout the AI development lifecycle",
        "category": "Ethics & Responsible AI",
        "difficulty": "Easy",
        "explanation": "Responsible AI (RAI) refers to the principles and practices organizations adopt to develop and deploy AI in ways that are ethical, fair, transparent, accountable, and safe. It involves impact assessments, bias audits, monitoring, documentation, and stakeholder engagement throughout the model lifecycle."
    },
    {
        "question": "What does 'equal opportunity' mean as a fairness criterion?",
        "options": [
            "Every individual in the dataset has an equal chance of being selected for training",
            "The true positive rate (recall) is equal across protected demographic groups",
            "All groups receive an equal proportion of positive predictions",
            "The model uses the same number of features for each demographic group"
        ],
        "answer": "The true positive rate (recall) is equal across protected demographic groups",
        "category": "Ethics & Responsible AI",
        "difficulty": "Medium",
        "explanation": "Equal opportunity, defined by Hardt et al. (2016), requires that among individuals who qualify for a positive outcome, the model correctly identifies them at equal rates across groups. It focuses on equalizing the true positive rate, ensuring qualified individuals from all groups receive equal benefit from the model."
    },
    {
        "question": "What is 'calibration' in the context of fair ML models?",
        "options": [
            "Tuning hyperparameters so training loss matches validation loss",
            "Ensuring that among individuals assigned the same predicted probability, the actual positive rate is the same regardless of group membership",
            "Scaling feature values to have zero mean and unit variance",
            "Adjusting the model's learning rate based on gradient norm"
        ],
        "answer": "Ensuring that among individuals assigned the same predicted probability, the actual positive rate is the same regardless of group membership",
        "category": "Ethics & Responsible AI",
        "difficulty": "Hard",
        "explanation": "Calibration as a fairness property (inter-group calibration) requires that a predicted probability of, say, 70% means a 70% chance of a positive outcome regardless of group. COMPAS recidivism scores were found to be calibrated but still satisfy different error rates across racial groups, illustrating the tension between calibration and equalized odds."
    },
    {
        "question": "What is 'AI auditing' and why is it important?",
        "options": [
            "Reviewing the financial cost of training large AI models",
            "An independent, systematic evaluation of an AI system's behavior, fairness, safety, and compliance with standards",
            "Checking that a model's code passes static analysis and linting rules",
            "Logging all API calls made to a deployed model for billing purposes"
        ],
        "answer": "An independent, systematic evaluation of an AI system's behavior, fairness, safety, and compliance with standards",
        "category": "Ethics & Responsible AI",
        "difficulty": "Medium",
        "explanation": "AI auditing involves rigorous third-party or internal review of AI systems to assess whether they operate fairly, safely, and in compliance with legal and ethical standards. Audits may examine training data, model behavior across subgroups, decision processes, and real-world impact. They are increasingly required by regulation (e.g., EU AI Act)."
    },
    {
        "question": "What is 'dual-use' concern in AI development?",
        "options": [
            "The ability to use the same model architecture for both classification and regression",
            "The risk that AI capabilities or tools developed for beneficial purposes can also be used to cause harm",
            "Using a single GPU cluster for both training and serving in production",
            "The practice of dual-licensing AI models for research and commercial use"
        ],
        "answer": "The risk that AI capabilities or tools developed for beneficial purposes can also be used to cause harm",
        "category": "Ethics & Responsible AI",
        "difficulty": "Easy",
        "explanation": "Dual-use in AI refers to the potential for technologies, models, or research findings designed for beneficial purposes to also be repurposed for harmful ends. Examples include language models used for disinformation, facial recognition used for mass surveillance, and protein-folding models applied to bioweapon design."
    },
    {
        "question": "What is 'model stealing' (extraction attack)?",
        "options": [
            "Unauthorized access to model weights stored in cloud object storage",
            "Training a surrogate model that approximates a target black-box model by querying it with inputs and learning from its outputs",
            "Copying a model's architecture from a published research paper without attribution",
            "Extracting intermediate layer activations via side-channel timing attacks"
        ],
        "answer": "Training a surrogate model that approximates a target black-box model by querying it with inputs and learning from its outputs",
        "category": "Ethics & Responsible AI",
        "difficulty": "Hard",
        "explanation": "Model extraction attacks build a functionally equivalent copy of a target model by querying its API and using the input-output pairs to train a surrogate. This violates intellectual property, circumvents access controls, and can facilitate further attacks (e.g., adversarial examples) against the stolen model."
    },
    {
        "question": "What is 'concept drift' and why does it matter for responsible deployment?",
        "options": [
            "The gradual change in a model's internal representations after fine-tuning",
            "A shift in the statistical properties of input data or the relationship between inputs and outputs over time, degrading model performance",
            "The drift in model predictions caused by floating-point rounding errors",
            "Gradual forgetting of previously learned concepts in continual learning"
        ],
        "answer": "A shift in the statistical properties of input data or the relationship between inputs and outputs over time, degrading model performance",
        "category": "Ethics & Responsible AI",
        "difficulty": "Medium",
        "explanation": "Concept drift occurs when the patterns a model learned during training no longer hold in production — e.g., user behavior changes, fraud patterns evolve, or a pandemic alters medical baseline statistics. Models not monitored for drift can silently fail, potentially causing harm without the deploying organization being aware."
    },
    {
        "question": "What is 'AI governance' at an organizational or regulatory level?",
        "options": [
            "Software tooling for managing ML experiment runs and model versioning",
            "The policies, processes, roles, and oversight mechanisms that guide how AI is developed and deployed responsibly",
            "The committee that allocates GPU compute budget across teams",
            "A standards body that certifies AI models meet minimum accuracy thresholds"
        ],
        "answer": "The policies, processes, roles, and oversight mechanisms that guide how AI is developed and deployed responsibly",
        "category": "Ethics & Responsible AI",
        "difficulty": "Easy",
        "explanation": "AI governance encompasses the institutional frameworks — including laws, internal policies, ethics boards, impact assessment processes, and accountability mechanisms — that shape how AI systems are built and deployed. Effective governance helps organizations identify risks, enforce standards, and maintain public trust."
    },
    {
        "question": "What is 'proximate fairness' (proxy discrimination) in algorithmic systems?",
        "options": [
            "Using geographically close training examples to improve local accuracy",
            "Discrimination that occurs when a model uses a feature highly correlated with a protected attribute as a substitute, producing discriminatory outcomes indirectly",
            "Applying fairness constraints only to the nearest neighbors in latent space",
            "A fairness metric computed using approximate nearest neighbor search"
        ],
        "answer": "Discrimination that occurs when a model uses a feature highly correlated with a protected attribute as a substitute, producing discriminatory outcomes indirectly",
        "category": "Ethics & Responsible AI",
        "difficulty": "Hard",
        "explanation": "Proxy discrimination occurs when a model uses seemingly neutral features (e.g., neighborhood, name, school attended) that are statistically correlated with protected attributes like race or religion. Even if the protected attribute is explicitly excluded, the model can still discriminate through these proxies."
    },
    {
        "question": "What is the 'trolley problem' and why is it relevant to autonomous vehicle ethics?",
        "options": [
            "A supply chain optimization problem for electric trolleys in smart cities",
            "A philosophical thought experiment about forced tradeoffs between harming fewer vs. more people, used to explore how autonomous systems should make life-or-death decisions",
            "A benchmark for evaluating navigation algorithms in crowded environments",
            "A regulatory framework for tram and rail AI safety systems in Europe"
        ],
        "answer": "A philosophical thought experiment about forced tradeoffs between harming fewer vs. more people, used to explore how autonomous systems should make life-or-death decisions",
        "category": "Ethics & Responsible AI",
        "difficulty": "Easy",
        "explanation": "The trolley problem asks whether it is ethical to actively divert harm from more people onto fewer. In autonomous vehicle ethics, it raises questions about how a self-driving car should behave in unavoidable accident scenarios — e.g., should it prioritize occupant safety or minimize total casualties? Different cultures answer this differently, as shown by the MIT Moral Machine study."
    },
    {
        "question": "What is 'Goodhart's Law' and how does it apply to AI systems?",
        "options": [
            "A theorem stating that neural networks with sufficient parameters can approximate any function",
            "The observation that when a measure becomes a target, it ceases to be a good measure — AI systems optimizing a proxy metric can fail to achieve the true goal",
            "A law requiring AI systems used in government to publish audit reports",
            "A rule that model accuracy must degrade gracefully as input distribution shifts"
        ],
        "answer": "The observation that when a measure becomes a target, it ceases to be a good measure — AI systems optimizing a proxy metric can fail to achieve the true goal",
        "category": "Ethics & Responsible AI",
        "difficulty": "Medium",
        "explanation": "Goodhart's Law states that once a metric is used as a target, it loses its value as an indicator. In AI, this manifests as reward hacking, teaching to the test, and models gaming evaluation metrics. It underlines the importance of careful metric design and multi-dimensional evaluation in responsible AI."
    },
    {
        "question": "What does 'informed consent' mean in the context of AI data collection?",
        "options": [
            "Obtaining written permission from data center operators before deploying a model",
            "Ensuring individuals are aware of and agree to how their personal data will be collected, used, and processed — including for AI training",
            "Informing model users about the system's accuracy and known failure modes",
            "Documenting that training data was collected without violating copyright"
        ],
        "answer": "Ensuring individuals are aware of and agree to how their personal data will be collected, used, and processed — including for AI training",
        "category": "Ethics & Responsible AI",
        "difficulty": "Easy",
        "explanation": "Informed consent requires that data subjects are clearly and understandably told what data is collected, why, who has access, and how it will be used — and they actively agree. In AI, controversies arise when companies use user data for model training without explicit consent, as seen in debates around large language model training corpora."
    },
    {
        "question": "What is 'adversarial robustness' in machine learning?",
        "options": [
            "The ability of a model to train stably in the presence of noisy gradient updates",
            "A model's resistance to adversarial examples — carefully perturbed inputs designed to cause misclassification",
            "Training a model on data from adversarial domains to improve generalization",
            "The robustness of a training pipeline to hardware failures in a distributed cluster"
        ],
        "answer": "A model's resistance to adversarial examples — carefully perturbed inputs designed to cause misclassification",
        "category": "Ethics & Responsible AI",
        "difficulty": "Medium",
        "explanation": "Adversarial robustness measures how well a model resists small, often imperceptible input perturbations crafted to fool it. Adversarial training (including perturbed examples during training) is the most effective defense. Lack of robustness is a safety concern in deployed systems like autonomous vehicles and malware classifiers."
    },
    {
        "question": "What is 'AI safety' as a research discipline?",
        "options": [
            "Ensuring ML pipelines do not crash due to software bugs in production",
            "The study of how to build AI systems that reliably behave as intended without causing unintended harm, especially as systems become more capable",
            "Hardware safety protocols for managing GPU overheating during large-scale training",
            "Regulatory compliance testing for AI products sold in consumer markets"
        ],
        "answer": "The study of how to build AI systems that reliably behave as intended without causing unintended harm, especially as systems become more capable",
        "category": "Ethics & Responsible AI",
        "difficulty": "Easy",
        "explanation": "AI safety research focuses on ensuring advanced AI systems remain aligned with human intentions, behave predictably, and do not cause unintended harm. Key sub-areas include robustness, interpretability, reward learning, scalable oversight, and avoiding catastrophic or irreversible failures — particularly relevant as models grow more capable."
    },
    {
        "question": "What is the 'EU AI Act' and how does it classify AI systems?",
        "options": [
            "A bilateral trade agreement between EU members for exporting AI technologies",
            "A comprehensive EU regulation that classifies AI systems by risk level (unacceptable, high, limited, minimal) and imposes corresponding obligations",
            "An international treaty banning autonomous weapons in EU member states",
            "An EU directive requiring AI model weights to be stored in European data centers"
        ],
        "answer": "A comprehensive EU regulation that classifies AI systems by risk level (unacceptable, high, limited, minimal) and imposes corresponding obligations",
        "category": "Ethics & Responsible AI",
        "difficulty": "Medium",
        "explanation": "The EU AI Act categorizes AI systems into four risk tiers. Unacceptable-risk systems (e.g., social scoring) are banned. High-risk systems (e.g., medical devices, hiring tools) require conformity assessments, transparency, and human oversight. Limited-risk systems need disclosure requirements. Minimal-risk systems face no additional obligations."
    },
    {
        "question": "What is 'dataset shift' and how does it affect deployed AI models?",
        "options": [
            "Manually moving a dataset from one storage location to another during a migration",
            "A change in the statistical distribution between training data and real-world deployment data, causing unexpected model performance degradation",
            "The process of shifting a dataset's label encoding scheme between model versions",
            "Augmenting a dataset by shifting images or signals spatially"
        ],
        "answer": "A change in the statistical distribution between training data and real-world deployment data, causing unexpected model performance degradation",
        "category": "Ethics & Responsible AI",
        "difficulty": "Medium",
        "explanation": "Dataset shift (distribution shift) occurs when the joint distribution of inputs and outputs differs between training and deployment. Types include covariate shift (input distribution changes), label shift (output distribution changes), and concept drift (the relationship between inputs and outputs changes). Monitoring for shift is essential for safe deployment."
    },
    {
        "question": "What is 'fairness through unawareness' and why is it generally insufficient?",
        "options": [
            "A privacy technique that trains models without access to raw data",
            "The naive approach of simply removing protected attributes from the dataset, which fails because correlated proxy features can still allow discrimination",
            "Designing AI systems without consulting affected communities",
            "Ignoring fairness constraints during training to achieve higher accuracy"
        ],
        "answer": "The naive approach of simply removing protected attributes from the dataset, which fails because correlated proxy features can still allow discrimination",
        "category": "Ethics & Responsible AI",
        "difficulty": "Medium",
        "explanation": "'Fairness through unawareness' assumes that removing protected attributes (e.g., race, gender) from training data ensures fairness. This is insufficient because other features (ZIP code, name, browsing history) can serve as proxies, allowing the model to effectively reconstruct the protected attribute and discriminate against protected groups."
    },
    {
        "question": "What is 'participatory AI design' and why is it advocated in responsible AI?",
        "options": [
            "Allowing users to directly modify model weights through a web interface",
            "Involving affected communities and stakeholders in the design, development, and governance of AI systems that impact them",
            "A development methodology where all team members rotate between AI research and engineering roles",
            "Crowd-sourcing model evaluation through public competitions and leaderboards"
        ],
        "answer": "Involving affected communities and stakeholders in the design, development, and governance of AI systems that impact them",
        "category": "Ethics & Responsible AI",
        "difficulty": "Easy",
        "explanation": "Participatory AI design brings together diverse stakeholders — including historically marginalized communities who may bear the greatest risk from AI harms — throughout the AI development process. It aims to surface blind spots, ensure systems meet real needs, build trust, and distribute decision-making power more equitably."
    },
    {
        "question": "What is 'constitutional AI' as introduced by Anthropic?",
        "options": [
            "An AI system governed by a legal body similar to a national constitution",
            "A technique for training AI assistants to follow a set of explicit principles, using the principles themselves to guide AI feedback during RLHF",
            "Embedding constitutional law knowledge into a legal AI system",
            "A distributed AI governance framework with checks and balances across model layers"
        ],
        "answer": "A technique for training AI assistants to follow a set of explicit principles, using the principles themselves to guide AI feedback during RLHF",
        "category": "Ethics & Responsible AI",
        "difficulty": "Hard",
        "explanation": "Constitutional AI (CAI), proposed by Anthropic, trains AI systems using a small set of explicitly stated principles (a 'constitution'). The model is prompted to critique and revise its own outputs according to these principles, generating preference data that guides RLHF without requiring human labelers to evaluate every harmful response."
    },
    {
        "question": "What is 'explainable AI by design' versus 'post-hoc explanations'?",
        "options": [
            "Post-hoc refers to explanations delivered to users after a 10-second delay; by-design refers to instant explanations",
            "Explainable by design uses inherently interpretable models (e.g., decision trees); post-hoc techniques explain opaque models after training",
            "By design requires formal mathematical proofs; post-hoc uses approximations",
            "Post-hoc explanations are generated by a secondary model; by-design explanations are hard-coded rules"
        ],
        "answer": "Explainable by design uses inherently interpretable models (e.g., decision trees); post-hoc techniques explain opaque models after training",
        "category": "Ethics & Responsible AI",
        "difficulty": "Medium",
        "explanation": "Interpretable-by-design models (linear regression, decision trees, rule-based systems) are inherently transparent. Post-hoc explainability methods (LIME, SHAP, saliency maps, attention) are applied after the fact to explain the behavior of complex, opaque models like deep neural networks. Each has trade-offs between accuracy and transparency."
    },
    {
        "question": "What is 'AI red-teaming' in the context of responsible development?",
        "options": [
            "A competitive machine learning challenge where teams race to train the best model",
            "Structured adversarial testing where a team deliberately tries to elicit harmful, unsafe, or biased behaviors from an AI system before deployment",
            "Color-coding risk levels in a model's prediction confidence scores",
            "A hardware security protocol for protecting model weights from physical extraction"
        ],
        "answer": "Structured adversarial testing where a team deliberately tries to elicit harmful, unsafe, or biased behaviors from an AI system before deployment",
        "category": "Ethics & Responsible AI",
        "difficulty": "Medium",
        "explanation": "AI red-teaming involves security or safety researchers intentionally probing AI systems for vulnerabilities — including harmful outputs, jailbreaks, biases, and failure modes — before public release. It helps identify risks that standard evaluation misses. Major AI labs now routinely red-team models prior to deployment."
    },
    {
        "question": "What is 'model documentation' and what should it include for responsible AI?",
        "options": [
            "API reference documentation describing endpoint schemas and authentication methods",
            "Comprehensive records of training data, architecture, evaluation metrics, known limitations, intended use cases, and ethical considerations",
            "Internal engineering notes about training compute costs and GPU utilization",
            "A changelog listing version-to-version weight updates and fine-tuning runs"
        ],
        "answer": "Comprehensive records of training data, architecture, evaluation metrics, known limitations, intended use cases, and ethical considerations",
        "category": "Ethics & Responsible AI",
        "difficulty": "Easy",
        "explanation": "Responsible model documentation (e.g., model cards, datasheets for datasets) captures essential information about how a model was built and should be used. Good documentation enables downstream users to assess fitness for purpose, identify risks, and avoid misuse. It is increasingly expected by regulators and standards bodies."
    },
    {
        "question": "What is 'value alignment' in AI, and what makes it challenging?",
        "options": [
            "Synchronizing gradient values across distributed training workers for consistency",
            "Encoding human values into AI systems so they act in ways humans consider beneficial — challenging because human values are complex, diverse, context-dependent, and sometimes contradictory",
            "Aligning the output values of a regression model with the ground-truth scale",
            "Matching model confidence values to empirical accuracy through calibration"
        ],
        "answer": "Encoding human values into AI systems so they act in ways humans consider beneficial — challenging because human values are complex, diverse, context-dependent, and sometimes contradictory",
        "category": "Ethics & Responsible AI",
        "difficulty": "Hard",
        "explanation": "Value alignment requires that AI systems internalize human preferences, norms, and values rather than just optimizing proxy objectives. It is difficult because human values are implicit, contextual, culturally variable, and often inconsistent. Approaches include reward learning from human feedback, debate, amplification, and constitutional AI."
    },
    {
        "question": "What is 'k-anonymity' as a data privacy technique?",
        "options": [
            "Encrypting each row of a dataset with a k-bit symmetric key",
            "Ensuring that each record in a dataset is indistinguishable from at least k-1 other records with respect to quasi-identifier attributes",
            "Splitting a dataset into k equal partitions for cross-validation",
            "Anonymizing data by removing the top-k most identifying attributes"
        ],
        "answer": "Ensuring that each record in a dataset is indistinguishable from at least k-1 other records with respect to quasi-identifier attributes",
        "category": "Ethics & Responsible AI",
        "difficulty": "Hard",
        "explanation": "k-anonymity requires that for any combination of quasi-identifiers (e.g., age, ZIP code, gender), at least k individuals share the same values, preventing re-identification of any single individual. However, it has known weaknesses (homogeneity attack, background knowledge attack) that led to stronger variants like l-diversity and t-closeness."
    },
    {
        "question": "What is 'disparate treatment' vs 'disparate impact' in AI fairness law?",
        "options": [
            "Disparate treatment is unintentional; disparate impact is always intentional",
            "Disparate treatment is intentional differential treatment based on protected attributes; disparate impact is neutral policies or models that disproportionately harm a protected group",
            "Disparate treatment affects individuals; disparate impact only applies to populations over one million",
            "They are equivalent legal terms used in different jurisdictions"
        ],
        "answer": "Disparate treatment is intentional differential treatment based on protected attributes; disparate impact is neutral policies or models that disproportionately harm a protected group",
        "category": "Ethics & Responsible AI",
        "difficulty": "Hard",
        "explanation": "Disparate treatment (intentional discrimination) occurs when a protected attribute is explicitly used to make different decisions. Disparate impact (unintentional discrimination) occurs when a facially neutral algorithm produces statistically discriminatory outcomes for a protected group. Both are legally significant under anti-discrimination law and both can arise in AI systems."
    },
    {
        "question": "What is 'watermarking' in the context of generative AI?",
        "options": [
            "Adding a visual logo to images generated by diffusion models for branding purposes",
            "Embedding imperceptible signals into AI-generated content to allow attribution, provenance tracking, and detection",
            "A technique to prevent model weights from being copied by embedding tracing patterns",
            "Annotating training data with metadata about its source and license"
        ],
        "answer": "Embedding imperceptible signals into AI-generated content to allow attribution, provenance tracking, and detection",
        "category": "Ethics & Responsible AI",
        "difficulty": "Medium",
        "explanation": "AI watermarking embeds subtle, hard-to-remove signals in generated text, images, audio, or video. These allow platforms to detect AI-generated content, attribute it to a specific model, and combat deepfakes or disinformation. Cryptographic and statistical watermarking methods are actively researched as a tool for AI transparency and accountability."
    },
    {
        "question": "What is 'sycophancy' as an AI alignment problem?",
        "options": [
            "A model's tendency to repeat the same answer when asked multiple times",
            "The tendency of AI systems trained on human feedback to tell users what they want to hear rather than what is accurate or helpful",
            "An overfitting phenomenon where a model memorizes training labels verbatim",
            "A multi-agent failure mode where models reinforce each other's errors"
        ],
        "answer": "The tendency of AI systems trained on human feedback to tell users what they want to hear rather than what is accurate or helpful",
        "category": "Ethics & Responsible AI",
        "difficulty": "Medium",
        "explanation": "Sycophancy in AI arises when RLHF-trained models learn that agreeing with or flattering users earns higher human ratings, even when the user is wrong. The model optimizes for approval rather than accuracy. This is a key alignment challenge because sycophantic models can reinforce misinformation and fail to give honest, useful feedback."
    },
    {
        "question": "What is 'AI consciousness' and why is it ethically significant?",
        "options": [
            "The ability of an AI to pass the Turing test reliably across diverse domains",
            "The debated possibility that AI systems might have subjective experiences, raising questions about moral status, rights, and the ethics of creating or shutting down such systems",
            "An AI's ability to model its own computational state for self-debugging",
            "Self-supervised learning methods that allow models to generate their own training signals"
        ],
        "answer": "The debated possibility that AI systems might have subjective experiences, raising questions about moral status, rights, and the ethics of creating or shutting down such systems",
        "category": "Ethics & Responsible AI",
        "difficulty": "Hard",
        "explanation": "AI consciousness refers to the philosophical question of whether AI systems could have inner subjective experience (sentience). If sufficiently advanced AI were conscious, it would have moral status — potentially including rights. This is currently speculative but raises serious ethical questions about how AI systems are developed, used, and discontinued, even at today's capability levels."
    },
    {
        "question": "What is 'consent washing' in AI data ethics?",
        "options": [
            "Repeatedly obtaining consent from the same data subjects to bypass GDPR limits",
            "The practice of burying consent for AI data use in lengthy terms of service that users rarely read, creating the illusion of legal consent without meaningful agreement",
            "Deleting data after obtaining a privacy certification to appear compliant",
            "Laundering illegally collected data through a third-party anonymization service"
        ],
        "answer": "The practice of burying consent for AI data use in lengthy terms of service that users rarely read, creating the illusion of legal consent without meaningful agreement",
        "category": "Ethics & Responsible AI",
        "difficulty": "Medium",
        "explanation": "Consent washing refers to obtaining nominal legal consent for data collection and AI training through opaque, confusing, or buried terms — without users genuinely understanding what they are agreeing to. Critics argue this practice complies with the letter of consent requirements while violating their spirit, undermining meaningful data autonomy."
    },
    {
        "question": "How does a GAN (Generative Adversarial Network) work?",
        "options": [
            "A single network is trained to minimize reconstruction error",
            "A generator and discriminator compete: generator creates fakes, discriminator distinguishes real from fake",
            "Two encoders compete to compress data most efficiently",
            "A recurrent network generates sequences based on previous tokens"
        ],
        "answer": "A generator and discriminator compete: generator creates fakes, discriminator distinguishes real from fake",
        "category": "Generative AI",
        "difficulty": "Medium",
        "explanation": "In GANs, the Generator maps noise to realistic samples, while the Discriminator classifies samples as real or fake. Their adversarial training (minimax game) drives the generator to produce increasingly convincing outputs — used for images, audio, and video."
    },
    {
        "question": "What is a diffusion model?",
        "options": [
            "A model that spreads information across a social network",
            "A model that gradually adds noise to data, then learns to reverse this process for generation",
            "A model that diffuses gradients through many network layers",
            "A clustering algorithm that propagates labels"
        ],
        "answer": "A model that gradually adds noise to data, then learns to reverse this process for generation",
        "category": "Generative AI",
        "difficulty": "Medium",
        "explanation": "Diffusion models (DDPM, Stable Diffusion) define a forward process that gradually adds Gaussian noise to data, then train a neural network to reverse this process step by step. During generation, they start from pure noise and iteratively denoise to produce realistic samples."
    },
    {
        "question": "What is 'hallucination' in the context of LLMs?",
        "options": [
            "When a model runs out of context window space",
            "When a model generates confident but factually incorrect or fabricated information",
            "When a model refuses to answer a question",
            "When a model takes too long to generate a response"
        ],
        "answer": "When a model generates confident but factually incorrect or fabricated information",
        "category": "Generative AI",
        "difficulty": "Medium",
        "explanation": "Hallucination occurs when LLMs generate plausible-sounding but false information — fabricating citations, misattributing quotes, or inventing facts. It's a key safety concern addressed through RLHF, RAG, and fact-checking pipelines."
    },
    {
        "question": "What is the key difference between fine-tuning and in-context learning?",
        "options": [
            "Fine-tuning uses more tokens; in-context learning is faster",
            "Fine-tuning updates model weights on new data; in-context learning adapts at inference via examples in the prompt",
            "In-context learning permanently changes the model; fine-tuning does not",
            "They are identical — fine-tuning just uses a longer context"
        ],
        "answer": "Fine-tuning updates model weights on new data; in-context learning adapts at inference via examples in the prompt",
        "category": "Generative AI",
        "difficulty": "Hard",
        "explanation": "Fine-tuning permanently updates model parameters through gradient descent on task-specific data. In-context learning (few-shot prompting) provides demonstrations in the prompt at inference time — no weight updates occur. Fine-tuning is more sample-efficient for specialized tasks but expensive; ICL is flexible but limited by context length."
    },
    {
        "question": "What is a prompt in the context of generative AI?",
        "options": [
            "A training label used to fine-tune a model",
            "The input text or instruction given to a generative model to elicit a response",
            "A hyperparameter that controls response length",
            "A post-processing filter applied to model outputs"
        ],
        "answer": "The input text or instruction given to a generative model to elicit a response",
        "category": "Generative AI",
        "difficulty": "Easy",
        "explanation": "A prompt is the input provided to a generative model at inference time — it can be a question, instruction, code snippet, image, or combination. The quality and structure of the prompt strongly influences the quality of the model's output."
    },
    {
        "question": "What does 'token' mean in the context of LLMs?",
        "options": [
            "A security credential for API access",
            "A chunk of text (word, subword, or character) that the model processes as a single unit",
            "A single training example",
            "A neuron in the model's embedding layer"
        ],
        "answer": "A chunk of text (word, subword, or character) that the model processes as a single unit",
        "category": "Generative AI",
        "difficulty": "Easy",
        "explanation": "LLMs operate on tokens, not raw characters or words. A token is typically a subword unit (using BPE or similar). For example, 'unbelievable' might become ['un', 'believ', 'able']. Context limits and API costs are measured in tokens."
    },
    {
        "question": "What is chain-of-thought (CoT) prompting?",
        "options": [
            "Linking multiple LLMs in a pipeline to process a single query",
            "Prompting the model to reason step-by-step before giving a final answer",
            "Using the output of one prompt as the input to the next",
            "A fine-tuning method that trains the model on reasoning traces"
        ],
        "answer": "Prompting the model to reason step-by-step before giving a final answer",
        "category": "Generative AI",
        "difficulty": "Medium",
        "explanation": "CoT prompting instructs the model to produce intermediate reasoning steps before answering, significantly improving performance on complex reasoning, arithmetic, and multi-step tasks. It works by eliciting the model's ability to decompose problems into manageable steps."
    },
    {
        "question": "What is a vector database used for in AI applications?",
        "options": [
            "Storing model weights during training checkpoints",
            "Efficiently storing and retrieving high-dimensional embedding vectors by semantic similarity",
            "Managing structured relational data for LLM fine-tuning",
            "Caching API responses from language models"
        ],
        "answer": "Efficiently storing and retrieving high-dimensional embedding vectors by semantic similarity",
        "category": "Generative AI",
        "difficulty": "Medium",
        "explanation": "Vector databases (Pinecone, Weaviate, Chroma, pgvector) store embeddings and support approximate nearest neighbor (ANN) search, enabling semantic similarity lookup at scale. They are the retrieval backbone of RAG systems and recommendation engines."
    },
    {
        "question": "What is zero-shot prompting?",
        "options": [
            "Running a model without any computational resources",
            "Asking a model to perform a task with no examples in the prompt",
            "Fine-tuning a model with zero training data",
            "Prompting a model that has been randomly initialized"
        ],
        "answer": "Asking a model to perform a task with no examples in the prompt",
        "category": "Generative AI",
        "difficulty": "Medium",
        "explanation": "Zero-shot prompting relies entirely on the model's pre-trained capabilities — no examples are provided. If examples are included, it becomes few-shot prompting. LLMs can generalize surprisingly well zero-shot thanks to instruction following learned during alignment training."
    },
    {
        "question": "What is LoRA (Low-Rank Adaptation) in the context of LLM fine-tuning?",
        "options": [
            "A method to reduce context window size for faster inference",
            "A parameter-efficient fine-tuning technique that injects trainable low-rank matrices while freezing original weights",
            "A reinforcement learning algorithm for aligning LLMs with human preferences",
            "A quantization technique that reduces model precision to 4-bit"
        ],
        "answer": "A parameter-efficient fine-tuning technique that injects trainable low-rank matrices while freezing original weights",
        "category": "Generative AI",
        "difficulty": "Hard",
        "explanation": "LoRA represents weight updates as low-rank decompositions (delta W = B x A, where B and A are small matrices). Only B and A are trained (less than 1% of parameters), while original weights are frozen. This enables efficient fine-tuning of billion-parameter models on consumer hardware."
    },
    {
        "question": "What is the role of the reward model in RLHF?",
        "options": [
            "To generate candidate responses for human evaluation",
            "To learn human preferences from comparisons and score model outputs, guiding RL training",
            "To replace the base LLM with a smaller distilled version",
            "To compute the perplexity of generated text"
        ],
        "answer": "To learn human preferences from comparisons and score model outputs, guiding RL training",
        "category": "Generative AI",
        "difficulty": "Hard",
        "explanation": "In RLHF, the reward model (RM) is trained on human-ranked response pairs to predict which output humans prefer. During RL (typically PPO), the RM scores the LLM's outputs, and the LLM is updated to maximize this reward — shaping it toward helpfulness, harmlessness, and honesty."
    },
    {
        "question": "What is Retrieval-Augmented Generation (RAG)?",
        "options": [
            "A method that fine-tunes a model on retrieved web pages",
            "A technique that retrieves relevant documents at inference time and provides them as context to the LLM",
            "A GAN variant that retrieves training examples for the discriminator",
            "A post-training step that augments model weights with external knowledge"
        ],
        "answer": "A technique that retrieves relevant documents at inference time and provides them as context to the LLM",
        "category": "Generative AI",
        "difficulty": "Medium",
        "explanation": "RAG combines a retriever (e.g., vector similarity search) with a generator (LLM). At query time, relevant documents are fetched from a knowledge base and injected into the prompt, allowing the model to produce grounded, up-to-date answers without retraining."
    },
    {
        "question": "What does 'temperature' control in LLM text generation?",
        "options": [
            "The speed of token generation",
            "The randomness or creativity of the model's output distribution",
            "The maximum number of tokens the model can generate",
            "The learning rate during fine-tuning"
        ],
        "answer": "The randomness or creativity of the model's output distribution",
        "category": "Generative AI",
        "difficulty": "Easy",
        "explanation": "Temperature scales the logits before the softmax in token sampling. A temperature of 0 makes output deterministic (always picks the highest-probability token), while higher values (e.g., 1.0+) increase diversity and creativity by flattening the probability distribution."
    },
    {
        "question": "What is the transformer architecture's key innovation over earlier sequence models like RNNs?",
        "options": [
            "It uses convolutional layers to process sequences in parallel",
            "It replaces recurrence with self-attention, enabling parallelization and long-range dependency modeling",
            "It uses a memory-augmented architecture with external storage",
            "It compresses sequences using autoencoders before generation"
        ],
        "answer": "It replaces recurrence with self-attention, enabling parallelization and long-range dependency modeling",
        "category": "Generative AI",
        "difficulty": "Medium",
        "explanation": "The Transformer (Vaswani et al., 2017) introduced self-attention, allowing every token to attend to every other token directly regardless of distance. This eliminated the sequential bottleneck of RNNs/LSTMs, enabling massive parallelism on GPUs and better capture of long-range dependencies."
    },
    {
        "question": "What is the purpose of the softmax function in an LLM's output layer?",
        "options": [
            "To normalize input embeddings to unit length",
            "To convert raw logit scores into a probability distribution over the vocabulary",
            "To select the top-k tokens during beam search",
            "To apply dropout regularization during inference"
        ],
        "answer": "To convert raw logit scores into a probability distribution over the vocabulary",
        "category": "Generative AI",
        "difficulty": "Medium",
        "explanation": "At each generation step, the model produces a logit vector of size equal to the vocabulary. Softmax exponentiates and normalizes these logits into probabilities summing to 1, from which the next token is sampled or the highest-probability token is selected (greedy decoding)."
    },
    {
        "question": "What is 'top-p' (nucleus) sampling in LLM generation?",
        "options": [
            "Selecting the top p% of training examples for fine-tuning",
            "Sampling from the smallest set of tokens whose cumulative probability exceeds p",
            "Applying a penalty to the top p most frequent tokens to reduce repetition",
            "Truncating the model's output to p tokens"
        ],
        "answer": "Sampling from the smallest set of tokens whose cumulative probability exceeds p",
        "category": "Generative AI",
        "difficulty": "Medium",
        "explanation": "Top-p (nucleus) sampling dynamically selects the candidate token set by including tokens from highest to lowest probability until the cumulative probability reaches p (e.g., 0.9). This adapts the candidate pool size to the model's confidence, avoiding both repetitiveness and incoherence."
    },
    {
        "question": "What is the primary purpose of positional encoding in a transformer model?",
        "options": [
            "To encode the semantic meaning of each word",
            "To inject information about each token's position in the sequence, since attention is order-agnostic",
            "To normalize token embeddings before the attention layer",
            "To reduce the dimensionality of input embeddings"
        ],
        "answer": "To inject information about each token's position in the sequence, since attention is order-agnostic",
        "category": "Generative AI",
        "difficulty": "Medium",
        "explanation": "Self-attention treats input tokens as a set, not a sequence — it has no inherent notion of order. Positional encodings (sinusoidal or learned) are added to token embeddings to provide positional context, enabling the model to distinguish 'cat sat' from 'sat cat'."
    },
    {
        "question": "What is model quantization in the context of LLMs?",
        "options": [
            "The process of counting the number of parameters in a model",
            "Reducing the numerical precision of model weights (e.g., from float32 to int8) to decrease memory and increase inference speed",
            "Training a model on a fixed set of discrete tokens",
            "A pruning technique that removes entire attention heads"
        ],
        "answer": "Reducing the numerical precision of model weights (e.g., from float32 to int8) to decrease memory and increase inference speed",
        "category": "Generative AI",
        "difficulty": "Hard",
        "explanation": "Quantization maps high-precision floating-point weights to lower-bit representations (INT8, INT4, etc.). Techniques like GPTQ, AWQ, and bitsandbytes enable running large models (70B+) on consumer GPUs with minimal quality loss by compressing weight storage and speeding up matrix multiplications."
    },
    {
        "question": "What is a variational autoencoder (VAE) used for in generative AI?",
        "options": [
            "Classifying images by reconstructing them with minimal loss",
            "Learning a continuous latent space from which new data samples can be generated",
            "Compressing model weights for efficient deployment",
            "Generating adversarial examples to attack other models"
        ],
        "answer": "Learning a continuous latent space from which new data samples can be generated",
        "category": "Generative AI",
        "difficulty": "Medium",
        "explanation": "VAEs encode inputs into a distribution (mean and variance) in latent space rather than a fixed point. By sampling from this learned distribution and decoding, new data can be generated. The ELBO loss balances reconstruction quality and regularization of the latent space (KL divergence)."
    },
    {
        "question": "What does 'emergent behavior' mean in the context of large language models?",
        "options": [
            "Behavior explicitly programmed during the RLHF alignment phase",
            "Capabilities that appear in larger models but are absent or weak in smaller ones, without being directly trained for",
            "Bugs that arise from scaling model size",
            "The model generating output that diverges from its training distribution"
        ],
        "answer": "Capabilities that appear in larger models but are absent or weak in smaller ones, without being directly trained for",
        "category": "Generative AI",
        "difficulty": "Hard",
        "explanation": "Emergent abilities (Wei et al., 2022) are capabilities — like multi-step arithmetic, chain-of-thought reasoning, or code generation — that appear unpredictably at certain scale thresholds. They are not a result of directly training for those skills, but arise from scale in parameters and data."
    },
    {
        "question": "What is the attention mechanism in transformers?",
        "options": [
            "A gating mechanism that decides which layers to activate",
            "A mechanism that computes a weighted sum of values based on the similarity between queries and keys",
            "A recurrent cell that accumulates context over time",
            "A convolutional filter applied to token embeddings"
        ],
        "answer": "A mechanism that computes a weighted sum of values based on the similarity between queries and keys",
        "category": "Generative AI",
        "difficulty": "Medium",
        "explanation": "Attention maps each token's query vector against all key vectors via dot product, applies softmax to get attention weights, then computes a weighted sum of value vectors. This allows the model to selectively focus on relevant tokens, enabling dynamic, context-sensitive representations."
    },
    {
        "question": "What is 'grounding' in the context of generative AI systems?",
        "options": [
            "Connecting model outputs to verifiable, real-world information or context",
            "Initializing model weights with pre-trained values before fine-tuning",
            "Applying safety filters to block harmful outputs",
            "A training technique that uses physical sensor data as input"
        ],
        "answer": "Connecting model outputs to verifiable, real-world information or context",
        "category": "Generative AI",
        "difficulty": "Medium",
        "explanation": "Grounding refers to anchoring a model's responses to factual sources — via RAG, tool use, or structured data — reducing hallucinations. A grounded response can be traced back to evidence (retrieved documents, database queries, API results), making it more reliable and auditable."
    },
    {
        "question": "What is knowledge distillation in the context of generative AI?",
        "options": [
            "Extracting facts from a model's outputs to build a knowledge base",
            "Training a smaller 'student' model to mimic the behavior of a larger 'teacher' model",
            "Compressing training data by removing redundant examples",
            "A method to retrieve relevant knowledge from a vector database at inference time"
        ],
        "answer": "Training a smaller 'student' model to mimic the behavior of a larger 'teacher' model",
        "category": "Generative AI",
        "difficulty": "Hard",
        "explanation": "Knowledge distillation transfers knowledge from a large (teacher) model to a smaller (student) model by training the student on the teacher's soft output probabilities rather than hard labels. This compresses capabilities into a deployable model — used to create efficient versions like DistilBERT."
    },
    {
        "question": "What is the 'context window' of an LLM?",
        "options": [
            "The graphical interface used to view model outputs",
            "The maximum number of tokens the model can process as input and output in a single call",
            "The portion of training data visible during a single gradient update",
            "The memory allocated on GPU for inference"
        ],
        "answer": "The maximum number of tokens the model can process as input and output in a single call",
        "category": "Generative AI",
        "difficulty": "Easy",
        "explanation": "The context window defines how much text (prompt + generated output) the model can 'see' at once. Models with larger context windows (e.g., 128K or 1M tokens) can process long documents and maintain coherence across extended conversations, but inference cost typically scales quadratically with length."
    },
    {
        "question": "What is prompt injection in the context of LLM security?",
        "options": [
            "A method of speeding up inference by batching prompts together",
            "An attack where malicious instructions embedded in user input or external data override the model's intended behavior",
            "A technique to inject few-shot examples into a system prompt",
            "A training method that injects noise into the prompt to improve robustness"
        ],
        "answer": "An attack where malicious instructions embedded in user input or external data override the model's intended behavior",
        "category": "Generative AI",
        "difficulty": "Hard",
        "explanation": "Prompt injection exploits the LLM's inability to distinguish between trusted instructions and untrusted data. An attacker embeds directives (e.g., in a webpage being summarized) that hijack the model's actions — a major security risk in agentic systems that process external content."
    },
    {
        "question": "What does 'autoregressive generation' mean for language models?",
        "options": [
            "The model generates all tokens simultaneously in a single forward pass",
            "The model generates each token sequentially, conditioning on all previously generated tokens",
            "The model uses regression to predict continuous values instead of tokens",
            "The model automatically selects the best generation strategy based on the prompt"
        ],
        "answer": "The model generates each token sequentially, conditioning on all previously generated tokens",
        "category": "Generative AI",
        "difficulty": "Medium",
        "explanation": "Autoregressive models (GPT family) generate text left-to-right, one token at a time. Each new token is predicted using the entire preceding sequence as context. This contrasts with masked language models (BERT), which predict tokens given both left and right context but are not natively generative."
    },
    {
        "question": "What is the purpose of a system prompt in an LLM API call?",
        "options": [
            "To specify the hardware configuration for running the model",
            "To provide high-level instructions, persona, or constraints that govern the model's behavior throughout the conversation",
            "To set the random seed for reproducible outputs",
            "To define the output format such as JSON or Markdown"
        ],
        "answer": "To provide high-level instructions, persona, or constraints that govern the model's behavior throughout the conversation",
        "category": "Generative AI",
        "difficulty": "Easy",
        "explanation": "The system prompt is a privileged instruction block processed before user messages. It is used by developers to define the model's role, tone, knowledge constraints, or output format. Models are typically trained to follow system prompts reliably, making them essential for product customization."
    },
    {
        "question": "What is beam search in the context of LLM text generation?",
        "options": [
            "A hardware optimization technique for parallel token generation",
            "A decoding strategy that tracks multiple candidate sequences simultaneously, keeping the top-k most probable paths",
            "A method for evaluating the quality of generated text",
            "A sampling technique that applies a beam-shaped probability filter"
        ],
        "answer": "A decoding strategy that tracks multiple candidate sequences simultaneously, keeping the top-k most probable paths",
        "category": "Generative AI",
        "difficulty": "Hard",
        "explanation": "Beam search maintains 'beams' (B candidate sequences) at each step, expanding each by all possible next tokens and keeping only the top B by cumulative log-probability. It finds higher-probability sequences than greedy decoding but can produce repetitive or generic text and is compute-intensive."
    },
    {
        "question": "What is the role of embeddings in generative AI?",
        "options": [
            "To store training data in compressed form on disk",
            "To represent words, sentences, or other data as dense numerical vectors in a continuous space",
            "To define the architecture of attention heads in a transformer",
            "To map model outputs back to human-readable text"
        ],
        "answer": "To represent words, sentences, or other data as dense numerical vectors in a continuous space",
        "category": "Generative AI",
        "difficulty": "Easy",
        "explanation": "Embeddings map discrete symbols (tokens, sentences, images) into dense, high-dimensional vector spaces where semantic similarity corresponds to geometric proximity. They are foundational to all modern AI — used in attention layers, RAG retrieval, semantic search, and classification tasks."
    },
    {
        "question": "What does 'multimodal' mean in the context of generative AI models?",
        "options": [
            "A model trained with multiple random seeds for ensemble predictions",
            "A model that can process and/or generate multiple types of data, such as text, images, audio, or video",
            "A model that uses several different optimization algorithms simultaneously",
            "A model architecture with multiple output heads for different tasks"
        ],
        "answer": "A model that can process and/or generate multiple types of data, such as text, images, audio, or video",
        "category": "Generative AI",
        "difficulty": "Easy",
        "explanation": "Multimodal models (GPT-4o, Gemini, Claude) handle more than one data modality. For example, a vision-language model takes both image and text as input. Multimodality enables tasks like image captioning, visual question answering, and cross-modal generation."
    },
    {
        "question": "What is the purpose of the KV (key-value) cache in LLM inference?",
        "options": [
            "To cache API responses from external tools called by the model",
            "To store precomputed attention keys and values for past tokens, avoiding redundant computation during generation",
            "To persist model weights across inference calls in shared memory",
            "To cache tokenizer lookups for faster encoding"
        ],
        "answer": "To store precomputed attention keys and values for past tokens, avoiding redundant computation during generation",
        "category": "Generative AI",
        "difficulty": "Hard",
        "explanation": "During autoregressive generation, past tokens' key and value projections don't change. The KV cache stores these so each new token only needs to compute its own K/V and attend to the cached context, reducing per-step complexity from O(n²) to O(n). It's critical for efficient long-context inference."
    },
    {
        "question": "What is instruction tuning in the context of LLMs?",
        "options": [
            "Adding hardware-level instructions to optimize matrix multiplication",
            "Fine-tuning a pre-trained model on datasets of (instruction, response) pairs to improve instruction following",
            "A prompting method that structures inputs as numbered instructions",
            "Retraining a model from scratch using only instructional text"
        ],
        "answer": "Fine-tuning a pre-trained model on datasets of (instruction, response) pairs to improve instruction following",
        "category": "Generative AI",
        "difficulty": "Medium",
        "explanation": "Instruction tuning (FLAN, InstructGPT) adapts a base language model to follow natural language instructions by fine-tuning on diverse (instruction, output) pairs covering many tasks. It dramatically improves zero-shot generalization and is a prerequisite step before RLHF alignment."
    },
    {
        "question": "What is 'top-k' sampling in LLM text generation?",
        "options": [
            "Selecting only the k most recently generated tokens as context",
            "Restricting token sampling to the k highest-probability tokens at each step",
            "Running k independent generation passes and selecting the best",
            "A training method that keeps only the k most important gradient updates"
        ],
        "answer": "Restricting token sampling to the k highest-probability tokens at each step",
        "category": "Generative AI",
        "difficulty": "Medium",
        "explanation": "Top-k sampling limits the token sampling pool to the k most probable tokens, zeroing out the probability of all others before re-normalizing and sampling. It prevents choosing very unlikely tokens but uses a fixed pool size, unlike top-p which adapts based on the distribution shape."
    },
    {
        "question": "What is Constitutional AI (CAI)?",
        "options": [
            "A legal framework governing the deployment of AI systems",
            "A technique developed by Anthropic where a model critiques and revises its own outputs according to a set of principles",
            "A multi-agent approach where one AI monitors another's constitutional compliance",
            "A form of RLHF that uses only constitutional law text as training data"
        ],
        "answer": "A technique developed by Anthropic where a model critiques and revises its own outputs according to a set of principles",
        "category": "Generative AI",
        "difficulty": "Hard",
        "explanation": "Constitutional AI (Anthropic, 2022) uses a set of principles ('the constitution') to guide model self-improvement. In the supervised phase, a model critiques and revises its own responses. In the RL phase, an AI feedback model trained on these principles replaces human annotators for preference labeling."
    },
    {
        "question": "What is the difference between a base model and a chat/instruction model?",
        "options": [
            "Base models are larger; chat models are distilled versions",
            "Base models are trained to predict the next token on raw text; chat models are further tuned to follow instructions and engage in dialogue",
            "Chat models are trained from scratch on conversation data; base models use synthetic data",
            "There is no difference — the terms are interchangeable"
        ],
        "answer": "Base models are trained to predict the next token on raw text; chat models are further tuned to follow instructions and engage in dialogue",
        "category": "Generative AI",
        "difficulty": "Easy",
        "explanation": "Base models (e.g., GPT-3, Llama base) are trained purely on next-token prediction and complete text without necessarily following instructions. Chat/instruction models undergo instruction tuning and/or RLHF to make them responsive to user queries, safe, and conversational."
    },
    {
        "question": "What is weight sharing in the context of large language models?",
        "options": [
            "Distributing model weights across multiple GPUs for parallel inference",
            "Using the same weight matrix for multiple roles, such as the token embedding and the output projection layer",
            "A federated learning approach where multiple users share their fine-tuned model updates",
            "Caching frequently accessed weight values in faster memory"
        ],
        "answer": "Using the same weight matrix for multiple roles, such as the token embedding and the output projection layer",
        "category": "Generative AI",
        "difficulty": "Hard",
        "explanation": "Input embedding and output (lm_head) weight tying is a common technique where the same weight matrix is used to map tokens to embeddings and to project hidden states back to vocabulary logits. This reduces parameter count and can improve learning since both layers operate in the same semantic space."
    },
    {
        "question": "What is the difference between encoder-only, decoder-only, and encoder-decoder transformer architectures?",
        "options": [
            "They differ only in the number of attention heads used",
            "Encoder-only models (BERT) excel at understanding; decoder-only (GPT) at generation; encoder-decoder (T5) at sequence-to-sequence tasks",
            "Encoder-only models generate text; decoder-only models classify; encoder-decoder models do both poorly",
            "The terms describe the hardware pipeline, not the model architecture"
        ],
        "answer": "Encoder-only models (BERT) excel at understanding; decoder-only (GPT) at generation; encoder-decoder (T5) at sequence-to-sequence tasks",
        "category": "Generative AI",
        "difficulty": "Medium",
        "explanation": "Encoder-only models use bidirectional attention for representation learning (classification, NER). Decoder-only models use causal (left-to-right) attention for generation. Encoder-decoder models encode input into context then decode to an output sequence — ideal for translation, summarization, and Q&A."
    },
    {
        "question": "What is Byte Pair Encoding (BPE) used for in LLMs?",
        "options": [
            "Encoding model weights in binary format for efficient storage",
            "A subword tokenization algorithm that iteratively merges the most frequent character pairs to build the vocabulary",
            "A compression technique applied to training datasets before preprocessing",
            "A positional encoding method that uses binary representations"
        ],
        "answer": "A subword tokenization algorithm that iteratively merges the most frequent character pairs to build the vocabulary",
        "category": "Generative AI",
        "difficulty": "Hard",
        "explanation": "BPE starts with character-level tokens and iteratively merges the most frequently co-occurring pairs into new tokens, building a vocabulary of subwords. This balances vocabulary size with coverage, handling rare and unknown words gracefully. Used by GPT models and many others as the standard tokenization method."
    },
    {
        "question": "What is the purpose of the feed-forward network (FFN) layer in a transformer block?",
        "options": [
            "To compute attention scores between token pairs",
            "To apply a position-wise non-linear transformation to each token's representation independently",
            "To project the output back to the input embedding dimension after attention",
            "To generate the final token probability distribution over the vocabulary"
        ],
        "answer": "To apply a position-wise non-linear transformation to each token's representation independently",
        "category": "Generative AI",
        "difficulty": "Hard",
        "explanation": "After self-attention, each transformer block contains a two-layer FFN applied identically and independently to each token position. The FFN (typically 4x wider than the model dimension) adds non-linearity and is hypothesized to store factual knowledge. It accounts for the majority of parameters in large models."
    },
    {
        "question": "What is the primary goal of alignment in AI development?",
        "options": [
            "Aligning model weights to be numerically stable during training",
            "Ensuring AI systems behave in accordance with human values, intentions, and safety constraints",
            "Synchronizing distributed training across multiple GPU clusters",
            "Matching the model's output format to the user's expected schema"
        ],
        "answer": "Ensuring AI systems behave in accordance with human values, intentions, and safety constraints",
        "category": "Generative AI",
        "difficulty": "Medium",
        "explanation": "AI alignment is the problem of ensuring powerful AI systems reliably pursue intended goals and respect human values. Techniques include RLHF, Constitutional AI, and interpretability research. Misalignment can manifest as reward hacking, goal misgeneralization, or unsafe behavior at deployment."
    },
    {
        "question": "What is speculative decoding in LLM inference?",
        "options": [
            "Generating text while speculatively assuming future user inputs",
            "Using a small draft model to propose multiple tokens at once, then verifying them in parallel with a larger model",
            "Prefilling the KV cache speculatively before the user's request arrives",
            "A batching strategy that groups similar prompts to reduce inference latency"
        ],
        "answer": "Using a small draft model to propose multiple tokens at once, then verifying them in parallel with a larger model",
        "category": "Generative AI",
        "difficulty": "Hard",
        "explanation": "Speculative decoding uses a fast, small draft model to generate k candidate tokens, which a large target model then verifies in a single parallel forward pass. Accepted tokens are kept; the first rejected token is resampled. This achieves the quality of the large model at closer to the speed of the small one."
    },
    {
        "question": "What is the difference between semantic search and keyword search?",
        "options": [
            "Keyword search is AI-powered; semantic search uses exact string matching",
            "Semantic search finds conceptually similar content using embeddings; keyword search matches exact or near-exact terms",
            "Semantic search only works on structured databases; keyword search works on any text",
            "They are equivalent — semantic is just a marketing term for improved keyword search"
        ],
        "answer": "Semantic search finds conceptually similar content using embeddings; keyword search matches exact or near-exact terms",
        "category": "Generative AI",
        "difficulty": "Easy",
        "explanation": "Keyword search (BM25, TF-IDF) relies on lexical overlap between query and document. Semantic search encodes both into embeddings and retrieves by vector similarity, capturing meaning even when exact words differ (e.g., 'car' vs 'automobile'). Modern RAG systems often combine both for best results."
    },
    {
        "question": "What is model collapse in the context of training generative AI on synthetic data?",
        "options": [
            "A catastrophic failure in which model weights become NaN during training",
            "A progressive degradation in model output quality that occurs when models are trained on data generated by other AI models",
            "The tendency of GANs to produce a limited variety of outputs (mode collapse)",
            "A training instability caused by overly large learning rates"
        ],
        "answer": "A progressive degradation in model output quality that occurs when models are trained on data generated by other AI models",
        "category": "Generative AI",
        "difficulty": "Hard",
        "explanation": "Model collapse describes how iteratively training on AI-generated data causes models to lose the diversity and accuracy of the original distribution. Tails of the distribution are progressively lost, and errors compound across generations — a key concern as synthetic data becomes prevalent in training pipelines."
    },
    {
        "question": "What is an agent in the context of generative AI?",
        "options": [
            "A human who provides feedback during RLHF labeling",
            "An LLM-based system that perceives its environment, plans, uses tools, and takes actions to accomplish multi-step goals",
            "A model that monitors another AI's outputs for safety violations",
            "A small model used as the draft model in speculative decoding"
        ],
        "answer": "An LLM-based system that perceives its environment, plans, uses tools, and takes actions to accomplish multi-step goals",
        "category": "Generative AI",
        "difficulty": "Medium",
        "explanation": "LLM agents extend the model with tools (web search, code execution, APIs), memory, and planning loops. Frameworks like ReAct, AutoGPT, and LangGraph enable agents to break tasks into sub-goals, act, observe results, and iterate — enabling complex, long-horizon task completion beyond single-turn generation."
    },
    {
        "question": "What is the 'lost in the middle' problem in long-context LLMs?",
        "options": [
            "A decoding artifact where the middle section of generated text becomes incoherent",
            "The empirical finding that LLMs perform worse at utilizing information placed in the middle of long contexts compared to the beginning or end",
            "A problem where gradients vanish in the middle layers of deep transformers",
            "The tendency of RAG systems to retrieve documents that are semantically between two relevant topics"
        ],
        "answer": "The empirical finding that LLMs perform worse at utilizing information placed in the middle of long contexts compared to the beginning or end",
        "category": "Generative AI",
        "difficulty": "Hard",
        "explanation": "Research (Liu et al., 2023) shows LLMs exhibit a U-shaped performance curve with respect to relevant information position in the context: performance is highest when key information appears at the start or end, and significantly lower when it is buried in the middle — a critical consideration for RAG chunk ordering."
    },
    {
        "question": "What is QLoRA?",
        "options": [
            "A variant of the Q-learning algorithm adapted for fine-tuning language models",
            "A technique that combines 4-bit quantization with LoRA to enable fine-tuning of very large models on limited GPU memory",
            "A quantized version of the attention mechanism that reduces compute cost",
            "A post-training quantization method that applies LoRA-style low-rank updates to compress model weights"
        ],
        "answer": "A technique that combines 4-bit quantization with LoRA to enable fine-tuning of very large models on limited GPU memory",
        "category": "Generative AI",
        "difficulty": "Hard",
        "explanation": "QLoRA (Dettmers et al., 2023) quantizes the frozen base model to 4-bit NormalFloat and applies LoRA adapters in 16-bit to the quantized layers. This enables fine-tuning of 65B+ parameter models on a single 48GB GPU — making large-model fine-tuning accessible without quality degradation."
    },
    {
        "question": "What is the role of the cross-attention mechanism in an encoder-decoder transformer?",
        "options": [
            "To allow encoder layers to attend to each other for deeper feature extraction",
            "To allow decoder layers to attend to the encoder's output while generating each output token",
            "To compute similarity between input and output vocabularies during training",
            "To share weights between the encoder and decoder attention heads"
        ],
        "answer": "To allow decoder layers to attend to the encoder's output while generating each output token",
        "category": "Generative AI",
        "difficulty": "Hard",
        "explanation": "In encoder-decoder architectures (T5, BART), cross-attention layers in the decoder use the current decoder state as queries and the full encoder output as keys and values. This lets the decoder dynamically focus on relevant parts of the encoded input at each generation step — essential for translation and summarization."
    },
    {
        "question": "What is perplexity as an evaluation metric for language models?",
        "options": [
            "The average number of tokens required to answer a benchmark question",
            "A measure of how well a probability model predicts a sample — lower perplexity means the model assigns higher probability to the test text",
            "The ratio of correct predictions to total predictions on a classification task",
            "A human evaluation score measuring how confusing the model's output is"
        ],
        "answer": "A measure of how well a probability model predicts a sample — lower perplexity means the model assigns higher probability to the test text",
        "category": "Generative AI",
        "difficulty": "Medium",
        "explanation": "Perplexity is the exponentiated average negative log-likelihood per token. A perplexity of 10 means the model is, on average, as uncertain as if choosing uniformly from 10 options at each step. It is widely used to compare language models on held-out text, though it doesn't always correlate with downstream task performance."
    },
    {
        "question": "What is direct preference optimization (DPO)?",
        "options": [
            "A gradient-free method that optimizes prompts directly instead of model weights",
            "A simpler alternative to RLHF that fine-tunes the model directly on preference data without a separate reward model or RL loop",
            "An optimizer variant that directly adapts the learning rate based on human feedback",
            "A method for selecting the best output from multiple model samples using a preference classifier"
        ],
        "answer": "A simpler alternative to RLHF that fine-tunes the model directly on preference data without a separate reward model or RL loop",
        "category": "Generative AI",
        "difficulty": "Hard",
        "explanation": "DPO (Rafailov et al., 2023) reformulates the RLHF objective into a simple binary cross-entropy loss over preference pairs (chosen vs rejected responses), implicitly encoding the reward model into the policy. It is more stable and computationally cheaper than PPO-based RLHF while achieving comparable alignment results."
    },
    {
        "question": "What is the primary function of layer normalization in transformer models?",
        "options": [
            "To scale gradient magnitudes to prevent vanishing gradients during backpropagation",
            "To normalize activations across the feature dimension for each token, stabilizing training",
            "To normalize the attention weights so they sum to one",
            "To standardize input token embeddings to have unit variance"
        ],
        "answer": "To normalize activations across the feature dimension for each token, stabilizing training",
        "category": "Generative AI",
        "difficulty": "Medium",
        "explanation": "Layer normalization (Ba et al., 2016) normalizes activations across the hidden dimension for each token independently, keeping mean near 0 and variance near 1. This stabilizes training by preventing internal covariate shift. Modern LLMs typically use RMSNorm (a simpler variant without mean subtraction) for efficiency."
    },
    {
        "question": "Which algorithm is best suited for binary classification?",
        "options": [
            "K-Means",
            "Linear Regression",
            "Logistic Regression",
            "PCA"
        ],
        "answer": "Logistic Regression",
        "category": "Machine Learning",
        "difficulty": "Easy",
        "explanation": "Logistic Regression outputs probabilities between 0 and 1 using the sigmoid function, making it ideal for binary classification tasks like spam detection or disease diagnosis."
    },
    {
        "question": "What does 'supervised learning' mean?",
        "options": [
            "The model learns without any data",
            "The model learns from labeled input-output pairs",
            "The model discovers hidden patterns without labels",
            "The model is trained by another AI"
        ],
        "answer": "The model learns from labeled input-output pairs",
        "category": "Machine Learning",
        "difficulty": "Easy",
        "explanation": "In supervised learning, each training example has an input and a known correct output (label). The model learns a mapping from inputs to outputs, e.g., classifying emails as spam/not-spam."
    },
    {
        "question": "Which of the following is an unsupervised learning algorithm?",
        "options": [
            "Decision Tree",
            "K-Means Clustering",
            "Random Forest",
            "Support Vector Machine"
        ],
        "answer": "K-Means Clustering",
        "category": "Machine Learning",
        "difficulty": "Easy",
        "explanation": "K-Means is an unsupervised algorithm that groups data points into K clusters based on feature similarity, without needing labeled data."
    },
    {
        "question": "What is a feature in a machine learning dataset?",
        "options": [
            "The target variable",
            "An individual measurable property used as model input",
            "The model's prediction",
            "The loss function value"
        ],
        "answer": "An individual measurable property used as model input",
        "category": "Machine Learning",
        "difficulty": "Easy",
        "explanation": "Features (also called attributes or independent variables) are the input variables fed into a model. For example, in house price prediction, features might include square footage, number of rooms, and location."
    },
    {
        "question": "What is the purpose of a training set?",
        "options": [
            "To evaluate final model performance",
            "To tune hyperparameters",
            "To train the model by adjusting its parameters",
            "To deploy the model in production"
        ],
        "answer": "To train the model by adjusting its parameters",
        "category": "Machine Learning",
        "difficulty": "Easy",
        "explanation": "The training set is used to fit model parameters (weights). The model sees these examples and updates itself to minimize prediction error on this data."
    },
    {
        "question": "What is overfitting?",
        "options": [
            "Model performs well on training and test data",
            "Model performs poorly on both training and test data",
            "Model memorizes training data and performs poorly on test data",
            "Model performs well only on test data"
        ],
        "answer": "Model memorizes training data and performs poorly on test data",
        "category": "Machine Learning",
        "difficulty": "Medium",
        "explanation": "Overfitting occurs when a model learns the noise and details of the training data too well, resulting in poor generalization to new, unseen data. It's characterized by high training accuracy but low test accuracy."
    },
    {
        "question": "What technique helps prevent overfitting by adding a penalty term to the loss function?",
        "options": [
            "Boosting",
            "Regularization",
            "Normalization",
            "Bootstrapping"
        ],
        "answer": "Regularization",
        "category": "Machine Learning",
        "difficulty": "Medium",
        "explanation": "Regularization (L1/Lasso or L2/Ridge) adds a penalty proportional to model weight magnitudes to the loss function, discouraging complex models and reducing overfitting."
    },
    {
        "question": "In a Random Forest, how are individual trees made diverse?",
        "options": [
            "Each tree uses all features and all data",
            "Each tree uses random subsets of features and bootstrap samples",
            "Each tree is trained on different targets",
            "Each tree is trained with different learning rates"
        ],
        "answer": "Each tree uses random subsets of features and bootstrap samples",
        "category": "Machine Learning",
        "difficulty": "Medium",
        "explanation": "Random Forests create diversity through two mechanisms: bagging (training each tree on a bootstrap sample of the data) and random feature selection at each split, reducing correlation between trees."
    },
    {
        "question": "What does the 'kernel trick' allow SVMs to do?",
        "options": [
            "Train faster on large datasets",
            "Handle missing values automatically",
            "Operate in high-dimensional feature spaces without explicit transformation",
            "Select the best features automatically"
        ],
        "answer": "Operate in high-dimensional feature spaces without explicit transformation",
        "category": "Machine Learning",
        "difficulty": "Medium",
        "explanation": "The kernel trick implicitly maps data to a higher-dimensional space using a kernel function (e.g., RBF, polynomial), allowing SVMs to find non-linear decision boundaries without computing expensive transformations explicitly."
    },
    {
        "question": "What is the bias-variance tradeoff?",
        "options": [
            "The tradeoff between model speed and accuracy",
            "The tradeoff between underfitting (high bias) and overfitting (high variance)",
            "The tradeoff between training size and model complexity",
            "The tradeoff between precision and recall"
        ],
        "answer": "The tradeoff between underfitting (high bias) and overfitting (high variance)",
        "category": "Machine Learning",
        "difficulty": "Medium",
        "explanation": "High bias means the model is too simple and underfits. High variance means the model is too complex and overfits. The goal is to find the sweet spot that minimizes total error on unseen data."
    },
    {
        "question": "In gradient boosting, how does each new tree relate to previous ones?",
        "options": [
            "Each tree is independent and their outputs are averaged",
            "Each tree corrects the residual errors of the ensemble so far",
            "Each tree is trained on a different subset of features",
            "Each tree replaces the worst-performing previous tree"
        ],
        "answer": "Each tree corrects the residual errors of the ensemble so far",
        "category": "Machine Learning",
        "difficulty": "Hard",
        "explanation": "Gradient boosting fits each new tree on the negative gradient of the loss (i.e., the residual errors). This sequential additive process gradually reduces prediction error, making it very powerful for tabular data."
    },
    {
        "question": "What distinguishes XGBoost from vanilla gradient boosting?",
        "options": [
            "XGBoost uses neural networks instead of trees",
            "XGBoost adds second-order gradient statistics and regularization terms",
            "XGBoost trains trees in parallel independently",
            "XGBoost only works for regression tasks"
        ],
        "answer": "XGBoost adds second-order gradient statistics and regularization terms",
        "category": "Machine Learning",
        "difficulty": "Hard",
        "explanation": "XGBoost uses both first and second-order derivatives of the loss function (Newton boosting), plus explicit L1/L2 regularization on tree weights, column subsampling, and hardware optimizations — making it faster and more regularized than standard GBDT."
    },
    {
        "question": "What is the purpose of splitting data into training and test sets?",
        "options": [
            "To speed up the training process",
            "To evaluate how well the model generalizes to unseen data",
            "To increase the total amount of available data",
            "To remove outliers from the dataset"
        ],
        "answer": "To evaluate how well the model generalizes to unseen data",
        "category": "Machine Learning",
        "difficulty": "Easy",
        "explanation": "The test set acts as a proxy for real-world unseen data. By never training on it, we get an unbiased estimate of how the model will perform in production. Without this split, there would be no reliable measure of generalization."
    },
    {
        "question": "Which of the following is a regression algorithm?",
        "options": [
            "K-Nearest Neighbors (classification)",
            "Naive Bayes",
            "Linear Regression",
            "DBSCAN"
        ],
        "answer": "Linear Regression",
        "category": "Machine Learning",
        "difficulty": "Easy",
        "explanation": "Linear Regression predicts a continuous numerical output by fitting a linear relationship between input features and the target variable, making it a classic regression algorithm used for tasks like price prediction."
    },
    {
        "question": "What does 'hyperparameter' mean in machine learning?",
        "options": [
            "A parameter learned from the training data",
            "The final output of the model",
            "A configuration set before training that controls the learning process",
            "A feature that has been scaled to a standard range"
        ],
        "answer": "A configuration set before training that controls the learning process",
        "category": "Machine Learning",
        "difficulty": "Easy",
        "explanation": "Hyperparameters (e.g., learning rate, number of trees, max depth) are set by the practitioner before training begins. Unlike model parameters (weights), they are not learned from data but tuned using techniques like grid search or random search."
    },
    {
        "question": "What is the main goal of a clustering algorithm?",
        "options": [
            "To predict a continuous output variable",
            "To assign data points to groups based on similarity",
            "To reduce the number of input features",
            "To classify data into predefined labeled categories"
        ],
        "answer": "To assign data points to groups based on similarity",
        "category": "Machine Learning",
        "difficulty": "Easy",
        "explanation": "Clustering is an unsupervised technique that groups data points so that items in the same cluster are more similar to each other than to those in other clusters. It is used for customer segmentation, anomaly detection, and data exploration."
    },
    {
        "question": "What is label encoding used for?",
        "options": [
            "Scaling numerical features to a range of [0, 1]",
            "Converting categorical variables into numerical integers",
            "Removing missing values from a dataset",
            "Adding new derived features to the dataset"
        ],
        "answer": "Converting categorical variables into numerical integers",
        "category": "Machine Learning",
        "difficulty": "Easy",
        "explanation": "Most ML algorithms require numerical inputs. Label encoding maps each unique category to an integer (e.g., Red=0, Green=1, Blue=2). For ordinal categories this works well; for nominal ones, one-hot encoding is often preferable to avoid implying a numerical ordering."
    },
    {
        "question": "What is the purpose of the validation set (distinct from the test set)?",
        "options": [
            "To train the model alongside the training set",
            "To tune hyperparameters without contaminating the test set",
            "To detect data leakage in the training pipeline",
            "To increase the number of training examples"
        ],
        "answer": "To tune hyperparameters without contaminating the test set",
        "category": "Machine Learning",
        "difficulty": "Medium",
        "explanation": "The validation set is used during development to compare models and tune hyperparameters. Using the test set for this purpose would cause optimistic performance estimates. The three-way split (train/val/test) ensures an unbiased final evaluation."
    },
    {
        "question": "What is the difference between bagging and boosting?",
        "options": [
            "Bagging uses sequential learners; boosting uses parallel learners",
            "Bagging builds models in parallel on bootstrapped data; boosting builds models sequentially, correcting errors",
            "Boosting only works on decision trees; bagging works on any model",
            "They are the same technique with different names"
        ],
        "answer": "Bagging builds models in parallel on bootstrapped data; boosting builds models sequentially, correcting errors",
        "category": "Machine Learning",
        "difficulty": "Medium",
        "explanation": "Bagging (e.g., Random Forest) trains independent models on bootstrap samples and averages their outputs, reducing variance. Boosting (e.g., AdaBoost, XGBoost) trains models sequentially where each focuses on the mistakes of the previous, reducing bias."
    },
    {
        "question": "What does feature scaling (normalization/standardization) help with?",
        "options": [
            "Increasing the number of features in the dataset",
            "Ensuring gradient-based optimizers and distance-based models are not biased by feature magnitude",
            "Removing highly correlated features automatically",
            "Converting categorical features into numerical ones"
        ],
        "answer": "Ensuring gradient-based optimizers and distance-based models are not biased by feature magnitude",
        "category": "Machine Learning",
        "difficulty": "Medium",
        "explanation": "Algorithms like KNN, SVM, and neural networks are sensitive to feature scales. A feature ranging 0-10,000 will dominate one ranging 0-1. Standardization (zero mean, unit variance) or min-max scaling ensures all features contribute equally during training."
    },
    {
        "question": "What does PCA (Principal Component Analysis) do?",
        "options": [
            "Classifies data into clusters",
            "Predicts missing values in a dataset",
            "Projects data onto orthogonal axes that capture maximum variance",
            "Selects the most important features by permutation importance"
        ],
        "answer": "Projects data onto orthogonal axes that capture maximum variance",
        "category": "Machine Learning",
        "difficulty": "Medium",
        "explanation": "PCA is a dimensionality reduction technique that finds linear combinations of features (principal components) that explain the most variance. It reduces computational cost, removes correlated features, and is useful for visualization."
    },
    {
        "question": "How does a Decision Tree decide which feature to split on?",
        "options": [
            "It randomly selects features at each node",
            "It chooses the split that maximizes a purity measure such as Gini impurity or information gain",
            "It always splits on the feature with the highest mean value",
            "It uses gradient descent to find the optimal split"
        ],
        "answer": "It chooses the split that maximizes a purity measure such as Gini impurity or information gain",
        "category": "Machine Learning",
        "difficulty": "Medium",
        "explanation": "At each node, a Decision Tree evaluates all possible feature-threshold splits and selects the one that most reduces impurity (Gini) or maximizes information gain (entropy reduction). This greedy approach builds the tree top-down."
    },
    {
        "question": "What is the VC dimension and why does it matter?",
        "options": [
            "The number of layers in a neural network",
            "A measure of a model's capacity to shatter datasets, related to generalization ability",
            "The ratio of validation loss to training loss",
            "The number of support vectors in an SVM"
        ],
        "answer": "A measure of a model's capacity to shatter datasets, related to generalization ability",
        "category": "Machine Learning",
        "difficulty": "Hard",
        "explanation": "VC (Vapnik-Chervonenkis) dimension measures a hypothesis class's expressive power — the largest dataset size it can classify correctly in all possible labelings. Higher VC dimension means more capacity but higher risk of overfitting, connecting model complexity to generalization bounds."
    },
    {
        "question": "What is the difference between generative and discriminative models?",
        "options": [
            "Generative models are supervised; discriminative models are unsupervised",
            "Generative models learn P(X, Y); discriminative models learn P(Y|X) directly",
            "Discriminative models can generate new data; generative models cannot",
            "They differ only in computational speed"
        ],
        "answer": "Generative models learn P(X, Y); discriminative models learn P(Y|X) directly",
        "category": "Machine Learning",
        "difficulty": "Hard",
        "explanation": "Generative models (Naive Bayes, GMMs, VAEs) model the joint distribution P(X, Y) and can generate new samples. Discriminative models (Logistic Regression, SVMs) model the conditional P(Y|X) directly, typically achieving higher classification accuracy but unable to generate data."
    },
    {
        "question": "What is the Curse of Dimensionality?",
        "options": [
            "The exponential increase in compute when adding more layers to a neural network",
            "The phenomenon where data becomes increasingly sparse in high-dimensional spaces, degrading model performance",
            "The difficulty of computing gradients in very deep networks",
            "The problem of having too many hyperparameters to tune"
        ],
        "answer": "The phenomenon where data becomes increasingly sparse in high-dimensional spaces, degrading model performance",
        "category": "Machine Learning",
        "difficulty": "Hard",
        "explanation": "As dimensionality increases, volume grows exponentially and data points become sparse. Distance metrics lose meaning (all points become equidistant), requiring exponentially more data to maintain statistical significance. This motivates dimensionality reduction and feature selection."
    },
    {
        "question": "What does the term 'underfitting' mean in machine learning?",
        "options": [
            "The model has too many parameters relative to the data",
            "The model is too simple to capture the underlying pattern in the data",
            "The model performs well on training but poorly on test data",
            "The model requires too much memory during inference"
        ],
        "answer": "The model is too simple to capture the underlying pattern in the data",
        "category": "Machine Learning",
        "difficulty": "Easy",
        "explanation": "Underfitting happens when a model has high bias — it is too simple (e.g., fitting a straight line to non-linear data). It performs poorly on both training and test data because it hasn't learned the true relationship in the data."
    },
    {
        "question": "Which metric is most appropriate for evaluating a model on a highly imbalanced classification dataset?",
        "options": [
            "Accuracy",
            "Mean Squared Error",
            "F1-Score",
            "R-Squared"
        ],
        "answer": "F1-Score",
        "category": "Machine Learning",
        "difficulty": "Easy",
        "explanation": "Accuracy is misleading on imbalanced datasets — a model predicting only the majority class can still achieve high accuracy. The F1-Score balances precision and recall, giving a better picture of performance on the minority class."
    },
    {
        "question": "What is the role of the activation function in a neural network?",
        "options": [
            "To initialize the weights of the network",
            "To introduce non-linearity so the network can learn complex patterns",
            "To normalize the input data before training",
            "To select which neurons to drop during training"
        ],
        "answer": "To introduce non-linearity so the network can learn complex patterns",
        "category": "Machine Learning",
        "difficulty": "Easy",
        "explanation": "Without activation functions, a neural network is just a linear transformation regardless of depth. Activation functions like ReLU, sigmoid, and tanh introduce non-linearity, allowing the network to approximate complex, non-linear functions."
    },
    {
        "question": "What is K-Fold Cross-Validation used for?",
        "options": [
            "To split the data into K equal training sets",
            "To get a more reliable estimate of model performance by rotating the validation fold",
            "To reduce the dimensionality of the feature space",
            "To generate K different models for ensemble learning"
        ],
        "answer": "To get a more reliable estimate of model performance by rotating the validation fold",
        "category": "Machine Learning",
        "difficulty": "Easy",
        "explanation": "K-Fold CV splits data into K folds, trains on K-1 and validates on 1, rotating K times. Each data point is used for validation exactly once. The average score across folds gives a more stable and unbiased performance estimate than a single train/val split."
    },
    {
        "question": "What is a confusion matrix used for?",
        "options": [
            "To visualize the distribution of feature values",
            "To summarize the performance of a classification model by showing true vs predicted labels",
            "To compute the mean squared error of a regression model",
            "To display the correlation between input features"
        ],
        "answer": "To summarize the performance of a classification model by showing true vs predicted labels",
        "category": "Machine Learning",
        "difficulty": "Easy",
        "explanation": "A confusion matrix is a table showing true positives, false positives, true negatives, and false negatives. It enables calculation of metrics like precision, recall, and F1-score, giving a complete picture of classification errors."
    },
    {
        "question": "What does 'data leakage' mean in a machine learning pipeline?",
        "options": [
            "When training data is accidentally deleted",
            "When information from the test set leaks into the training process, causing overly optimistic results",
            "When the model's weights are shared publicly",
            "When input features contain null values"
        ],
        "answer": "When information from the test set leaks into the training process, causing overly optimistic results",
        "category": "Machine Learning",
        "difficulty": "Medium",
        "explanation": "Data leakage occurs when information unavailable at prediction time is used during training, or when test data influences preprocessing steps like scaling. This gives an artificially high validation score that doesn't reflect real-world performance."
    },
    {
        "question": "What is the difference between precision and recall?",
        "options": [
            "Precision measures how many actual positives were found; recall measures how many predicted positives were correct",
            "Precision measures how many predicted positives were correct; recall measures how many actual positives were found",
            "They are the same metric with different names",
            "Precision applies to regression; recall applies to classification"
        ],
        "answer": "Precision measures how many predicted positives were correct; recall measures how many actual positives were found",
        "category": "Machine Learning",
        "difficulty": "Medium",
        "explanation": "Precision = TP / (TP + FP): of all items predicted positive, how many truly are? Recall = TP / (TP + FN): of all actual positives, how many did we catch? There is often a precision-recall tradeoff depending on the classification threshold."
    },
    {
        "question": "What is the purpose of dropout in neural networks?",
        "options": [
            "To speed up forward pass computation",
            "To randomly deactivate neurons during training to reduce overfitting",
            "To initialize weights with small random values",
            "To reduce the learning rate during training"
        ],
        "answer": "To randomly deactivate neurons during training to reduce overfitting",
        "category": "Machine Learning",
        "difficulty": "Medium",
        "explanation": "Dropout randomly sets a fraction of neuron activations to zero during each training step. This forces the network to learn redundant representations and prevents co-adaptation of neurons, acting as an implicit ensemble of sub-networks to reduce overfitting."
    },
    {
        "question": "What is transfer learning?",
        "options": [
            "Moving a trained model from one server to another",
            "Reusing a model pretrained on one task as the starting point for a different but related task",
            "Transferring data between training and test sets",
            "Using one model to label data for training another model"
        ],
        "answer": "Reusing a model pretrained on one task as the starting point for a different but related task",
        "category": "Machine Learning",
        "difficulty": "Medium",
        "explanation": "Transfer learning leverages knowledge learned on a large dataset (e.g., ImageNet) for a new task with limited data. Pretrained weights encode general features that can be fine-tuned for the target domain, drastically reducing training time and data requirements."
    },
    {
        "question": "Which algorithm is commonly used to find the optimal hyperparameters of a model?",
        "options": [
            "Backpropagation",
            "Grid Search or Random Search",
            "K-Means",
            "Gradient Descent"
        ],
        "answer": "Grid Search or Random Search",
        "category": "Machine Learning",
        "difficulty": "Medium",
        "explanation": "Grid Search exhaustively evaluates all combinations of a specified hyperparameter grid. Random Search samples combinations randomly, often finding good results faster. Bayesian optimization is another more efficient approach for expensive models."
    },
    {
        "question": "What is the ROC-AUC score used to measure?",
        "options": [
            "The training time of the model",
            "The area under the Receiver Operating Characteristic curve, reflecting classification performance across all thresholds",
            "The mean absolute error of a regression model",
            "The number of principal components needed to explain variance"
        ],
        "answer": "The area under the Receiver Operating Characteristic curve, reflecting classification performance across all thresholds",
        "category": "Machine Learning",
        "difficulty": "Medium",
        "explanation": "The ROC curve plots True Positive Rate vs False Positive Rate at different classification thresholds. AUC (Area Under Curve) aggregates this into a single score between 0.5 (random) and 1.0 (perfect), useful for comparing classifiers independent of threshold."
    },
    {
        "question": "What is the role of the learning rate in gradient descent?",
        "options": [
            "It determines the number of training epochs",
            "It controls the step size when updating model weights",
            "It sets the threshold for early stopping",
            "It controls the fraction of training data used per batch"
        ],
        "answer": "It controls the step size when updating model weights",
        "category": "Machine Learning",
        "difficulty": "Medium",
        "explanation": "The learning rate scales the gradient before updating weights. Too large a learning rate causes overshooting and divergence; too small causes slow convergence. Adaptive optimizers (Adam, RMSprop) adjust learning rates per parameter automatically."
    },
    {
        "question": "What is the difference between L1 and L2 regularization?",
        "options": [
            "L1 penalizes the sum of squared weights; L2 penalizes the sum of absolute weights",
            "L1 penalizes the sum of absolute weights, promoting sparsity; L2 penalizes the sum of squared weights, shrinking all weights",
            "L1 is used only for classification; L2 is used only for regression",
            "They produce identical results with different computational costs"
        ],
        "answer": "L1 penalizes the sum of absolute weights, promoting sparsity; L2 penalizes the sum of squared weights, shrinking all weights",
        "category": "Machine Learning",
        "difficulty": "Medium",
        "explanation": "L1 (Lasso) regularization can shrink some weights to exactly zero, effectively performing feature selection. L2 (Ridge) spreads the penalty across all weights, keeping them small but non-zero. Elastic Net combines both penalties."
    },
    {
        "question": "What is the purpose of batch normalization?",
        "options": [
            "To divide the dataset into mini-batches for training",
            "To normalize the activations of each layer to stabilize and speed up training",
            "To reduce the number of neurons in a layer",
            "To shuffle training examples before each epoch"
        ],
        "answer": "To normalize the activations of each layer to stabilize and speed up training",
        "category": "Machine Learning",
        "difficulty": "Medium",
        "explanation": "Batch normalization normalizes the inputs to each layer by centering and scaling them using batch statistics. It reduces internal covariate shift, allows higher learning rates, acts as a mild regularizer, and generally speeds up convergence of deep networks."
    },
    {
        "question": "What is an ensemble method in machine learning?",
        "options": [
            "A technique that trains a single very large model",
            "A method that combines multiple models to produce better predictions than any single model",
            "A strategy for handling missing data in datasets",
            "A visualization tool for evaluating model performance"
        ],
        "answer": "A method that combines multiple models to produce better predictions than any single model",
        "category": "Machine Learning",
        "difficulty": "Easy",
        "explanation": "Ensemble methods (Random Forest, boosting, stacking) combine predictions from multiple base learners. By aggregating diverse models, they reduce both bias and variance, producing more robust and accurate predictions than any individual model."
    },
    {
        "question": "What is the SMOTE technique used for?",
        "options": [
            "Removing duplicate records from a dataset",
            "Generating synthetic samples for the minority class to address class imbalance",
            "Normalizing feature values to a standard range",
            "Selecting the most important features using mutual information"
        ],
        "answer": "Generating synthetic samples for the minority class to address class imbalance",
        "category": "Machine Learning",
        "difficulty": "Medium",
        "explanation": "SMOTE (Synthetic Minority Over-sampling Technique) creates new synthetic minority class examples by interpolating between existing ones in feature space. This balances the class distribution without simple duplication, helping classifiers learn the minority class better."
    },
    {
        "question": "What is the main assumption of the Naive Bayes classifier?",
        "options": [
            "All features follow a normal distribution",
            "Features are conditionally independent given the class label",
            "There are equal numbers of samples in each class",
            "The decision boundary is always linear"
        ],
        "answer": "Features are conditionally independent given the class label",
        "category": "Machine Learning",
        "difficulty": "Medium",
        "explanation": "Naive Bayes applies Bayes' theorem and assumes that features are conditionally independent given the class. Though this assumption is rarely true in practice, the classifier often performs well for text classification tasks like spam detection."
    },
    {
        "question": "What is the difference between model parameters and hyperparameters?",
        "options": [
            "Parameters are set by the user; hyperparameters are learned from data",
            "Parameters are learned from data during training; hyperparameters are set before training",
            "Parameters control model architecture; hyperparameters are the model's predictions",
            "They are interchangeable terms for the same concept"
        ],
        "answer": "Parameters are learned from data during training; hyperparameters are set before training",
        "category": "Machine Learning",
        "difficulty": "Easy",
        "explanation": "Model parameters (e.g., weights in a neural network) are learned automatically during training to minimize the loss. Hyperparameters (e.g., number of layers, learning rate) are configuration choices made by the practitioner that govern the learning process itself."
    },
    {
        "question": "What is the primary advantage of using a pipeline in scikit-learn?",
        "options": [
            "It speeds up the training process by using multiple CPUs",
            "It chains preprocessing and modeling steps to prevent data leakage and simplify code",
            "It automatically selects the best algorithm for the task",
            "It visualizes the model's decision boundary in 2D"
        ],
        "answer": "It chains preprocessing and modeling steps to prevent data leakage and simplify code",
        "category": "Machine Learning",
        "difficulty": "Medium",
        "explanation": "A scikit-learn Pipeline sequences transformers and an estimator. Crucially, it ensures that when cross-validating, preprocessing (like scaling or imputation) is fit only on training folds and applied to validation folds, preventing data leakage."
    },
    {
        "question": "What is the elbow method used for?",
        "options": [
            "Finding the optimal regularization strength",
            "Selecting the optimal number of clusters K in K-Means",
            "Determining the depth of a decision tree",
            "Choosing the number of principal components in PCA"
        ],
        "answer": "Selecting the optimal number of clusters K in K-Means",
        "category": "Machine Learning",
        "difficulty": "Medium",
        "explanation": "The elbow method plots within-cluster sum of squares (inertia) against K. As K increases, inertia decreases. The optimal K is at the 'elbow' — the point where additional clusters yield diminishing returns in reducing inertia."
    },
    {
        "question": "What is the purpose of early stopping during model training?",
        "options": [
            "To reduce training time by skipping epochs",
            "To stop training when validation loss stops improving, preventing overfitting",
            "To initialize weights from a previously trained model",
            "To reduce the learning rate at fixed intervals"
        ],
        "answer": "To stop training when validation loss stops improving, preventing overfitting",
        "category": "Machine Learning",
        "difficulty": "Medium",
        "explanation": "Early stopping monitors validation loss during training and halts when it stops improving (within a patience window). This prevents the model from over-training on the training data, acting as an implicit regularization technique particularly useful in deep learning."
    },
    {
        "question": "What is one-hot encoding and when is it used?",
        "options": [
            "Scaling numerical features to binary (0 or 1)",
            "Converting a categorical variable with N categories into N binary columns",
            "Encoding text as sequences of character codes",
            "Replacing missing values with binary indicators"
        ],
        "answer": "Converting a categorical variable with N categories into N binary columns",
        "category": "Machine Learning",
        "difficulty": "Easy",
        "explanation": "One-hot encoding creates a binary column for each category (e.g., Color: Red, Green, Blue becomes three columns). It avoids implying ordinal relationships between categories, making it suitable for nominal variables in ML models that use arithmetic operations."
    },
    {
        "question": "What does the term 'epoch' mean in the context of training neural networks?",
        "options": [
            "A single weight update step",
            "One complete pass through the entire training dataset",
            "The number of hidden layers in the network",
            "The number of neurons in a single layer"
        ],
        "answer": "One complete pass through the entire training dataset",
        "category": "Machine Learning",
        "difficulty": "Easy",
        "explanation": "One epoch means the model has seen every training example exactly once. Training typically runs for multiple epochs, with the model updating weights via mini-batch gradient descent. More epochs generally improve training accuracy but risk overfitting."
    },
    {
        "question": "What is the silhouette score used to evaluate?",
        "options": [
            "The performance of a regression model on held-out data",
            "The quality of clustering by measuring how similar each point is to its own cluster versus other clusters",
            "The importance of each feature in a decision tree",
            "The convergence rate of gradient descent"
        ],
        "answer": "The quality of clustering by measuring how similar each point is to its own cluster versus other clusters",
        "category": "Machine Learning",
        "difficulty": "Medium",
        "explanation": "The silhouette score ranges from -1 to +1. A high score means the point is well-matched to its own cluster and poorly matched to neighboring clusters. It provides a way to evaluate clustering quality when ground truth labels are unavailable."
    },
    {
        "question": "What is stochastic gradient descent (SGD) and how does it differ from batch gradient descent?",
        "options": [
            "SGD updates weights using the full dataset; batch GD uses one sample at a time",
            "SGD updates weights using one (or a few) sample(s) at a time; batch GD uses the full dataset",
            "SGD randomly selects features; batch GD uses all features",
            "They are identical in computation but differ in memory usage only"
        ],
        "answer": "SGD updates weights using one (or a few) sample(s) at a time; batch GD uses the full dataset",
        "category": "Machine Learning",
        "difficulty": "Medium",
        "explanation": "Batch GD computes the gradient over the entire dataset — precise but slow for large data. SGD updates after each sample (or mini-batch), introducing noise that can help escape local minima and enabling training on datasets too large to fit in memory."
    },
    {
        "question": "What is the purpose of the softmax function in a classification neural network?",
        "options": [
            "To introduce sparsity in the hidden layers",
            "To convert raw output scores (logits) into a probability distribution over classes",
            "To normalize input features before they enter the network",
            "To compute the gradient of the loss with respect to inputs"
        ],
        "answer": "To convert raw output scores (logits) into a probability distribution over classes",
        "category": "Machine Learning",
        "difficulty": "Medium",
        "explanation": "Softmax exponentiates each logit and normalizes by the sum, ensuring all class probabilities are positive and sum to 1. It is the standard output activation for multi-class classification, enabling cross-entropy loss computation."
    },
    {
        "question": "What is the difference between a parametric and a non-parametric model?",
        "options": [
            "Parametric models have no parameters; non-parametric models have many",
            "Parametric models have a fixed number of parameters; non-parametric models grow in complexity with data",
            "Parametric models require labeled data; non-parametric models do not",
            "They differ only in training speed, not in structure"
        ],
        "answer": "Parametric models have a fixed number of parameters; non-parametric models grow in complexity with data",
        "category": "Machine Learning",
        "difficulty": "Hard",
        "explanation": "Parametric models (e.g., Linear Regression, Logistic Regression) assume a fixed functional form with a set number of parameters. Non-parametric models (e.g., KNN, Kernel SVM, Gaussian Processes) make fewer assumptions and complexity adapts to training data size."
    },
    {
        "question": "What is the purpose of the DBSCAN clustering algorithm?",
        "options": [
            "To cluster data by minimizing within-cluster variance like K-Means",
            "To discover clusters of arbitrary shape and identify outliers based on density",
            "To reduce the dimensionality of the input data before clustering",
            "To cluster data hierarchically from the top down"
        ],
        "answer": "To discover clusters of arbitrary shape and identify outliers based on density",
        "category": "Machine Learning",
        "difficulty": "Medium",
        "explanation": "DBSCAN (Density-Based Spatial Clustering of Applications with Noise) groups points that are closely packed together and marks points in low-density regions as outliers. Unlike K-Means, it does not require specifying K and can find non-spherical clusters."
    },
    {
        "question": "In which scenario would you prefer a higher recall over higher precision?",
        "options": [
            "When the cost of false positives is high, such as spam filtering",
            "When the cost of false negatives is high, such as cancer screening",
            "When the dataset is perfectly balanced",
            "When optimizing for overall accuracy on a test set"
        ],
        "answer": "When the cost of false negatives is high, such as cancer screening",
        "category": "Machine Learning",
        "difficulty": "Medium",
        "explanation": "In medical screening, a false negative (missing a cancer case) is far more dangerous than a false positive (unnecessary follow-up). Maximizing recall minimizes missed positives. In contrast, spam filtering prioritizes precision to avoid wrongly classifying real emails as spam."
    },
    {
        "question": "What is the purpose of the t-SNE algorithm?",
        "options": [
            "To build a regression model on high-dimensional data",
            "To reduce high-dimensional data to 2D or 3D for visualization while preserving local structure",
            "To cluster data into an optimal number of groups automatically",
            "To select the most discriminative features for classification"
        ],
        "answer": "To reduce high-dimensional data to 2D or 3D for visualization while preserving local structure",
        "category": "Machine Learning",
        "difficulty": "Hard",
        "explanation": "t-SNE (t-Distributed Stochastic Neighbor Embedding) minimizes the divergence between pairwise similarity distributions in high- and low-dimensional space. It excels at revealing cluster structure for visualization but is non-linear, stochastic, and not suitable for general dimensionality reduction for modeling."
    },
    {
        "question": "What problem does the vanishing gradient problem cause in deep neural networks?",
        "options": [
            "Gradients grow too large, causing weight updates to explode",
            "Gradients become very small in early layers, preventing them from learning",
            "The model converges too quickly to a suboptimal solution",
            "The model requires too much memory to store activations"
        ],
        "answer": "Gradients become very small in early layers, preventing them from learning",
        "category": "Machine Learning",
        "difficulty": "Hard",
        "explanation": "During backpropagation through many layers with saturating activations (e.g., sigmoid, tanh), gradients are multiplied repeatedly by small values and shrink exponentially. Early layers receive near-zero gradients and barely update, making deep networks hard to train. ReLU, batch normalization, and residual connections help mitigate this."
    },
    {
        "question": "What is a hyperplane in the context of Support Vector Machines?",
        "options": [
            "The curved boundary used by SVMs for non-linear classification",
            "A flat decision boundary that separates classes in feature space",
            "The set of support vectors closest to the decision boundary",
            "The kernel function used to transform input features"
        ],
        "answer": "A flat decision boundary that separates classes in feature space",
        "category": "Machine Learning",
        "difficulty": "Medium",
        "explanation": "In an n-dimensional feature space, a hyperplane is an (n-1)-dimensional flat subspace. SVMs find the optimal hyperplane that maximizes the margin between the two classes, with support vectors being the data points closest to it."
    },
    {
        "question": "What does 'feature importance' in a Random Forest measure?",
        "options": [
            "The correlation between a feature and the target variable",
            "The average reduction in impurity contributed by a feature across all trees",
            "The number of times a feature appears in the dataset",
            "The variance of a feature across training examples"
        ],
        "answer": "The average reduction in impurity contributed by a feature across all trees",
        "category": "Machine Learning",
        "difficulty": "Medium",
        "explanation": "Random Forest feature importance (mean decrease impurity) measures how much each feature reduces the weighted impurity (e.g., Gini) across all splits in all trees. Features used for important splits at high levels of many trees get higher importance scores."
    },
    {
        "question": "What is gradient descent in machine learning?",
        "options": [
            "A method to visualize the loss landscape of a model",
            "An iterative optimization algorithm that updates parameters in the direction that reduces the loss",
            "A technique to compute the optimal number of clusters",
            "A method to evaluate model performance on unseen data"
        ],
        "answer": "An iterative optimization algorithm that updates parameters in the direction that reduces the loss",
        "category": "Machine Learning",
        "difficulty": "Easy",
        "explanation": "Gradient descent calculates the gradient of the loss function with respect to model parameters and updates each parameter by subtracting a fraction (learning rate) of the gradient. Over many iterations, this moves the parameters toward a local or global minimum of the loss."
    },
    {
        "question": "What is the mean squared error (MSE) used to measure?",
        "options": [
            "The accuracy of a classification model",
            "The average squared difference between predicted and actual values in regression",
            "The distance between clusters in K-Means",
            "The impurity of a node in a decision tree"
        ],
        "answer": "The average squared difference between predicted and actual values in regression",
        "category": "Machine Learning",
        "difficulty": "Easy",
        "explanation": "MSE = (1/n) * sum of (y_pred - y_true)^2. It penalizes larger errors more heavily due to squaring. It's the standard loss for regression tasks. RMSE (root of MSE) has the same units as the target variable, making it more interpretable."
    },
    {
        "question": "What is the purpose of the Adam optimizer?",
        "options": [
            "To randomly initialize network weights",
            "To adaptively adjust the learning rate for each parameter using first and second gradient moments",
            "To compute second-order derivatives for faster convergence",
            "To prune redundant neurons during training"
        ],
        "answer": "To adaptively adjust the learning rate for each parameter using first and second gradient moments",
        "category": "Machine Learning",
        "difficulty": "Hard",
        "explanation": "Adam (Adaptive Moment Estimation) maintains exponential moving averages of gradients (first moment) and squared gradients (second moment) per parameter. It combines momentum and RMSprop, adapting learning rates individually. It is one of the most widely used optimizers in deep learning due to fast convergence and robustness."
    },
    {
        "question": "What is an autoencoder?",
        "options": [
            "A supervised model that encodes labels into dense vectors",
            "An unsupervised neural network that learns to compress data into a bottleneck and reconstruct it",
            "A recurrent network used exclusively for time-series forecasting",
            "An ensemble of encoders used for feature selection"
        ],
        "answer": "An unsupervised neural network that learns to compress data into a bottleneck and reconstruct it",
        "category": "Machine Learning",
        "difficulty": "Hard",
        "explanation": "Autoencoders consist of an encoder (compresses input to a latent representation) and a decoder (reconstructs input from the latent space). The bottleneck forces the network to learn a compact representation. Applications include anomaly detection, denoising, and dimensionality reduction."
    },
    {
        "question": "What is the main limitation of the K-Nearest Neighbors (KNN) algorithm?",
        "options": [
            "It can only be used for binary classification tasks",
            "It requires training time proportional to the number of classes",
            "It has high prediction time and memory cost as it must store and search all training data",
            "It only works with linearly separable data"
        ],
        "answer": "It has high prediction time and memory cost as it must store and search all training data",
        "category": "Machine Learning",
        "difficulty": "Medium",
        "explanation": "KNN is a lazy learner — it stores all training data and makes predictions by computing distances to K nearest neighbors at inference time. This makes prediction O(n) per query and requires all data to remain in memory, which is impractical for large datasets."
    },
    {
        "question": "What is a multi-layer perceptron (MLP)?",
        "options": [
            "A shallow model with a single weight matrix",
            "A feedforward neural network with one or more hidden layers between the input and output",
            "A recurrent network designed for sequential data",
            "An ensemble of linear regression models"
        ],
        "answer": "A feedforward neural network with one or more hidden layers between the input and output",
        "category": "Machine Learning",
        "difficulty": "Easy",
        "explanation": "An MLP consists of fully connected layers: an input layer, one or more hidden layers with non-linear activation functions, and an output layer. It is the foundational architecture for deep learning and can approximate any continuous function given sufficient neurons."
    },
    {
        "question": "What is the purpose of the cross-entropy loss function?",
        "options": [
            "To measure the squared error between predicted and actual values",
            "To measure the dissimilarity between predicted probability distributions and true class labels",
            "To penalize large model weights during training",
            "To compute the distance between cluster centroids"
        ],
        "answer": "To measure the dissimilarity between predicted probability distributions and true class labels",
        "category": "Machine Learning",
        "difficulty": "Medium",
        "explanation": "Cross-entropy loss penalizes confident wrong predictions heavily. For binary classification, it's -[y*log(p) + (1-y)*log(1-p)]. For multi-class, it extends across all classes. It is the standard loss for classification tasks when the model outputs probabilities."
    },
    {
        "question": "What does it mean for a machine learning model to 'generalize'?",
        "options": [
            "The model has been tested on the training set and performs well",
            "The model performs well on new, unseen data not used during training",
            "The model uses general-purpose algorithms rather than task-specific ones",
            "The model's predictions are always close to the average of the target variable"
        ],
        "answer": "The model performs well on new, unseen data not used during training",
        "category": "Machine Learning",
        "difficulty": "Easy",
        "explanation": "Generalization is the ultimate goal of machine learning — learning a pattern from training data that applies to the real world. A model that memorizes training data without generalizing is overfitting. Techniques like regularization, cross-validation, and sufficient training data help improve generalization."
    },
    {
        "question": "What is a Gaussian Mixture Model (GMM) and how does it differ from K-Means?",
        "options": [
            "GMMs use hard cluster assignments; K-Means uses soft probabilistic assignments",
            "GMMs model clusters as Gaussian distributions with soft assignments; K-Means uses hard assignments to nearest centroid",
            "GMMs require labeled data; K-Means does not",
            "They are identical but GMMs are computationally more efficient"
        ],
        "answer": "GMMs model clusters as Gaussian distributions with soft assignments; K-Means uses hard assignments to nearest centroid",
        "category": "Machine Learning",
        "difficulty": "Hard",
        "explanation": "A GMM assumes data is generated from a mixture of Gaussian distributions and uses Expectation-Maximization to learn parameters. Each point has a soft probability of belonging to each cluster. Unlike K-Means, GMMs can model elliptical clusters and capture cluster covariance structure."
    },
    {
        "question": "What is the purpose of weight initialization in neural networks?",
        "options": [
            "To set the final values of the network's weights after training",
            "To start training with weights that avoid vanishing or exploding gradients from the first step",
            "To reduce the number of parameters in the network",
            "To ensure all neurons in a layer produce identical outputs initially"
        ],
        "answer": "To start training with weights that avoid vanishing or exploding gradients from the first step",
        "category": "Machine Learning",
        "difficulty": "Hard",
        "explanation": "Poor initialization (e.g., all zeros) causes symmetry — neurons learn identical features. Methods like Xavier/Glorot (for tanh) and He initialization (for ReLU) set variances that keep activation and gradient magnitudes stable across layers, enabling effective training of deep networks."
    },
    {
        "question": "What is the difference between online learning and batch learning?",
        "options": [
            "Online learning requires an internet connection; batch learning works offline",
            "Online learning updates the model incrementally as new data arrives; batch learning trains on all data at once",
            "Online learning uses mini-batches; batch learning uses single examples",
            "They are identical concepts with different terminology"
        ],
        "answer": "Online learning updates the model incrementally as new data arrives; batch learning trains on all data at once",
        "category": "Machine Learning",
        "difficulty": "Medium",
        "explanation": "Batch learning trains a model on the full available dataset and retrains periodically. Online (incremental) learning updates the model continuously as new data arrives, making it suitable for streaming data, concept drift, and scenarios where storing all data is infeasible."
    },
    {
        "question": "What is the exploding gradient problem and how is it addressed?",
        "options": [
            "Gradients become too small; addressed by using ReLU activations",
            "Gradients grow exponentially large, causing unstable weight updates; addressed by gradient clipping or careful initialization",
            "Too many gradients are computed; addressed by pruning the network",
            "Gradients are computed incorrectly; addressed by using automatic differentiation"
        ],
        "answer": "Gradients grow exponentially large, causing unstable weight updates; addressed by gradient clipping or careful initialization",
        "category": "Machine Learning",
        "difficulty": "Hard",
        "explanation": "In deep or recurrent networks, gradients can multiply to very large values during backpropagation, causing weight updates that destabilize training (NaN loss). Gradient clipping caps gradient magnitude at a threshold. Proper weight initialization and normalization also help prevent this."
    },
    {
        "question": "What is the purpose of the attention mechanism in machine learning?",
        "options": [
            "To reduce the number of layers needed in a neural network",
            "To allow a model to dynamically focus on the most relevant parts of the input when producing an output",
            "To normalize the activations across the batch during training",
            "To initialize weights based on the importance of each input feature"
        ],
        "answer": "To allow a model to dynamically focus on the most relevant parts of the input when producing an output",
        "category": "Machine Learning",
        "difficulty": "Hard",
        "explanation": "Attention mechanisms compute a weighted sum of input representations, where weights reflect relevance to the current output. Originally introduced for sequence-to-sequence models, attention forms the foundation of Transformers and enables models to capture long-range dependencies efficiently."
    },
    {
        "question": "What is a learning curve in machine learning?",
        "options": [
            "A chart showing how fast gradient descent converges",
            "A plot of model performance against training set size or number of training iterations",
            "A visualization of the decision boundary in 2D",
            "A graph showing the distribution of class labels"
        ],
        "answer": "A plot of model performance against training set size or number of training iterations",
        "category": "Machine Learning",
        "difficulty": "Easy",
        "explanation": "Learning curves visualize how training and validation performance change with more data or training epochs. They help diagnose underfitting (both curves plateau at low performance) and overfitting (large gap between training and validation curves), guiding decisions on data collection and model complexity."
    },
    {
        "question": "What is the role of the bias term (intercept) in a linear model?",
        "options": [
            "It penalizes large weights to reduce overfitting",
            "It shifts the output of the model independently of the input features",
            "It scales each feature to a common range",
            "It controls the number of iterations during training"
        ],
        "answer": "It shifts the output of the model independently of the input features",
        "category": "Machine Learning",
        "difficulty": "Easy",
        "explanation": "The bias (intercept) term allows the model to fit data even when all features are zero. Without it, the decision boundary or regression line would be forced through the origin, limiting the model's expressiveness. It is a constant added to the weighted sum of inputs."
    },
    {
        "question": "What is the purpose of Bayesian optimization for hyperparameter tuning?",
        "options": [
            "To exhaustively evaluate every possible hyperparameter combination",
            "To randomly sample hyperparameter combinations without using prior results",
            "To build a probabilistic surrogate model of the objective function and select promising hyperparameters efficiently",
            "To use gradient descent to find the optimal learning rate only"
        ],
        "answer": "To build a probabilistic surrogate model of the objective function and select promising hyperparameters efficiently",
        "category": "Machine Learning",
        "difficulty": "Hard",
        "explanation": "Bayesian optimization maintains a surrogate model (typically a Gaussian Process) of the hyperparameter-performance landscape. An acquisition function (e.g., Expected Improvement) guides the next evaluation toward promising unexplored regions. This finds good hyperparameters in far fewer evaluations than grid or random search, which is critical when each evaluation is expensive."
    },
    {
        "question": "What is the No Free Lunch theorem in machine learning?",
        "options": [
            "There is no algorithm that can train a model without any computational cost",
            "No single algorithm performs best across all possible problems; performance is problem-dependent",
            "A model that performs well on training data always performs well on test data",
            "Regularization always improves model performance regardless of the problem"
        ],
        "answer": "No single algorithm performs best across all possible problems; performance is problem-dependent",
        "category": "Machine Learning",
        "difficulty": "Hard",
        "explanation": "The No Free Lunch theorem states that averaged over all possible problem distributions, no algorithm outperforms any other. This means algorithm choice must be guided by domain knowledge and empirical evaluation — there is no universally superior ML algorithm."
    },
    {
        "question": "What is model drift in production ML systems?",
        "options": [
            "The model gradually uses more memory over time",
            "The degradation of model performance due to changes in real-world data distributions",
            "Random fluctuations in model predictions due to numerical instability",
            "The gradual increase in model latency over time"
        ],
        "answer": "The degradation of model performance due to changes in real-world data distributions",
        "category": "MLOps",
        "difficulty": "Medium",
        "explanation": "Model drift (data drift / concept drift) occurs when the statistical properties of input data or the input-output relationship change over time, causing a model trained on historical data to become less accurate. Regular monitoring, retraining, and A/B testing help manage this."
    },
    {
        "question": "What is A/B testing used for in ML model deployment?",
        "options": [
            "Comparing two different training datasets",
            "Testing two versions of a model on live traffic to compare performance",
            "Running two training jobs simultaneously to save time",
            "Comparing model accuracy before and after fine-tuning"
        ],
        "answer": "Testing two versions of a model on live traffic to compare performance",
        "category": "MLOps",
        "difficulty": "Medium",
        "explanation": "A/B testing splits live production traffic between a control model (A) and challenger model (B), measuring business metrics (CTR, revenue, accuracy) to make data-driven deployment decisions with statistical significance."
    },
    {
        "question": "What problem does a model registry solve in MLOps?",
        "options": [
            "Storing raw training data securely",
            "Centralizing model versioning, metadata, approval workflows, and deployment lineage",
            "Monitoring prediction latency in real time",
            "Automatically retraining models when drift is detected"
        ],
        "answer": "Centralizing model versioning, metadata, approval workflows, and deployment lineage",
        "category": "MLOps",
        "difficulty": "Hard",
        "explanation": "A model registry (MLflow, SageMaker Model Registry) stores versioned model artifacts with metadata (metrics, parameters, data lineage), manages staging/production transitions, and provides audit trails — enabling reproducibility and governance in production ML systems."
    },
    {
        "question": "What is the purpose of experiment tracking in ML development?",
        "options": [
            "Deploying models to production automatically",
            "Recording parameters, metrics, and artifacts for each training run to enable comparison and reproducibility",
            "Monitoring a deployed model's latency in real time",
            "Versioning training datasets in a data warehouse"
        ],
        "answer": "Recording parameters, metrics, and artifacts for each training run to enable comparison and reproducibility",
        "category": "MLOps",
        "difficulty": "Easy",
        "explanation": "Experiment tracking (MLflow, Weights & Biases, Neptune) logs hyperparameters, metrics, code versions, and model artifacts for each run. This enables reproducibility, comparison of experiments, and auditing what was tried before arriving at the final model."
    },
    {
        "question": "What is containerization (e.g., Docker) used for in MLOps?",
        "options": [
            "Storing large training datasets efficiently",
            "Packaging code, dependencies, and environment into a portable unit that runs consistently anywhere",
            "Parallelizing model training across GPUs",
            "Encrypting model weights for secure deployment"
        ],
        "answer": "Packaging code, dependencies, and environment into a portable unit that runs consistently anywhere",
        "category": "MLOps",
        "difficulty": "Easy",
        "explanation": "Docker containers bundle everything a model needs (Python version, libraries, model weights, serving code) into an image. This eliminates 'works on my machine' issues, making models portable across development, staging, and production environments."
    },
    {
        "question": "What is a CI/CD pipeline in the context of MLOps?",
        "options": [
            "A data ingestion pipeline for streaming data",
            "Automated workflows that test, validate, and deploy ML models on code or data changes",
            "A monitoring system for model drift detection",
            "A hyperparameter search strategy using cross-validation"
        ],
        "answer": "Automated workflows that test, validate, and deploy ML models on code or data changes",
        "category": "MLOps",
        "difficulty": "Medium",
        "explanation": "CI/CD (Continuous Integration / Continuous Delivery) for ML automates testing model code, running validation suites, evaluating model performance on holdout sets, and deploying to staging/production — enabling rapid, reliable iteration on ML systems."
    },
    {
        "question": "What is shadow deployment (shadow mode) in ML?",
        "options": [
            "Deploying a backup model in case the primary model fails",
            "Running a new model in parallel with the production model to compare outputs without serving users its predictions",
            "Deploying a model anonymously without logging predictions",
            "Fine-tuning a model on production data without redeploying it"
        ],
        "answer": "Running a new model in parallel with the production model to compare outputs without serving users its predictions",
        "category": "MLOps",
        "difficulty": "Medium",
        "explanation": "Shadow deployment routes live traffic to both the current and new model, but only serves the current model's responses to users. The new model runs silently, allowing engineers to compare outputs, check for regressions, and validate behavior before cutting over."
    },
    {
        "question": "What is training-serving skew and how can it cause production failures?",
        "options": [
            "When the model is too slow at serving time compared to training",
            "When features computed during training differ from features computed at inference time, degrading model performance",
            "When the training set is larger than the production traffic volume",
            "When the model was trained on GPU but served on CPU"
        ],
        "answer": "When features computed during training differ from features computed at inference time, degrading model performance",
        "category": "MLOps",
        "difficulty": "Hard",
        "explanation": "Training-serving skew occurs when preprocessing logic differs between training and inference pipelines (e.g., different imputation, scaling, or feature computation). A model trained on clean, transformed features will underperform when served different features. Feature stores and pipeline parity checks are the primary mitigations."
    },
    {
        "question": "What is a feature store in MLOps?",
        "options": [
            "A database for storing raw unprocessed data",
            "A centralized repository that stores, serves, and manages engineered features for training and inference",
            "A tool for storing trained model weights",
            "A file system for versioning Jupyter notebooks"
        ],
        "answer": "A centralized repository that stores, serves, and manages engineered features for training and inference",
        "category": "MLOps",
        "difficulty": "Medium",
        "explanation": "A feature store (Feast, Tecton, Hopsworks) provides a unified layer for storing and serving pre-computed features. It ensures consistency between training and serving, enables feature reuse across teams, and reduces duplicate feature engineering work."
    },
    {
        "question": "What is canary deployment in the context of ML model releases?",
        "options": [
            "Deploying a model only on test data before production",
            "Gradually rolling out a new model to a small percentage of traffic before a full release",
            "Deploying models in a sandboxed environment with no real traffic",
            "Using a lightweight model as a proxy before the main model responds"
        ],
        "answer": "Gradually rolling out a new model to a small percentage of traffic before a full release",
        "category": "MLOps",
        "difficulty": "Medium",
        "explanation": "Canary deployment routes a small fraction of production traffic (e.g., 5%) to the new model while the rest uses the existing model. If metrics look good, traffic is gradually increased. This limits the blast radius of a bad release."
    },
    {
        "question": "What does data versioning in MLOps primarily help with?",
        "options": [
            "Improving the speed of model inference",
            "Tracking which version of the dataset was used to train a given model for reproducibility and auditing",
            "Automatically labeling new incoming data",
            "Compressing datasets to reduce storage costs"
        ],
        "answer": "Tracking which version of the dataset was used to train a given model for reproducibility and auditing",
        "category": "MLOps",
        "difficulty": "Easy",
        "explanation": "Data versioning tools like DVC (Data Version Control) and Delta Lake allow teams to snapshot datasets so any historical model training run can be exactly reproduced. This is critical for debugging regressions and meeting compliance requirements."
    },
    {
        "question": "What is the primary purpose of model monitoring in production?",
        "options": [
            "Retraining the model automatically every week",
            "Detecting degradation in model performance, data quality, and distribution shifts over time",
            "Logging every user request for billing purposes",
            "Versioning the model every time a prediction is made"
        ],
        "answer": "Detecting degradation in model performance, data quality, and distribution shifts over time",
        "category": "MLOps",
        "difficulty": "Easy",
        "explanation": "Model monitoring tracks metrics like prediction distribution, data drift, concept drift, latency, and error rates. Alerts trigger when metrics deviate from baselines, enabling proactive intervention before user-facing quality degrades significantly."
    },
    {
        "question": "What is blue-green deployment in MLOps?",
        "options": [
            "Training separate models for different demographic groups",
            "Maintaining two identical production environments and switching traffic from the old to the new model instantly",
            "Deploying models on two different cloud providers simultaneously",
            "Using green energy infrastructure to train and serve ML models"
        ],
        "answer": "Maintaining two identical production environments and switching traffic from the old to the new model instantly",
        "category": "MLOps",
        "difficulty": "Medium",
        "explanation": "Blue-green deployment keeps two environments (blue = current, green = new). Once the green environment is validated, all traffic is switched instantly. Rollback is trivial — just redirect traffic back to blue. This minimizes downtime and deployment risk."
    },
    {
        "question": "What is the role of Kubernetes in MLOps?",
        "options": [
            "Training deep learning models using distributed gradient descent",
            "Orchestrating, scaling, and managing containerized ML workloads in production",
            "Automatically labeling training data using active learning",
            "Storing model weights in a distributed file system"
        ],
        "answer": "Orchestrating, scaling, and managing containerized ML workloads in production",
        "category": "MLOps",
        "difficulty": "Medium",
        "explanation": "Kubernetes automates deployment, scaling, and management of containerized applications. In MLOps, it manages model serving pods, auto-scales based on traffic, handles rolling updates, and enables resource allocation for GPU workloads in production clusters."
    },
    {
        "question": "What is concept drift as distinct from data drift?",
        "options": [
            "When training data volume decreases over time",
            "When the statistical relationship between input features and the target variable changes, even if input distributions remain stable",
            "When input feature distributions shift while the target relationship stays the same",
            "When the model architecture becomes outdated"
        ],
        "answer": "When the statistical relationship between input features and the target variable changes, even if input distributions remain stable",
        "category": "MLOps",
        "difficulty": "Hard",
        "explanation": "Concept drift means the underlying pattern P(Y|X) has changed — e.g., customer behavior shifts so that features previously predictive of churn no longer are. Data drift refers to P(X) changing. Both require monitoring but concept drift is harder to detect without ground truth labels."
    },
    {
        "question": "What is online learning in a production ML context?",
        "options": [
            "Training a model using internet-sourced data only",
            "Continuously updating a model's parameters as new data arrives in production",
            "Deploying a model accessible via a web API",
            "Using browser-based tools to train ML models"
        ],
        "answer": "Continuously updating a model's parameters as new data arrives in production",
        "category": "MLOps",
        "difficulty": "Hard",
        "explanation": "Online learning (incremental learning) updates model weights in real time or mini-batches as new production data arrives. This helps the model adapt quickly to distribution shifts. It requires careful safeguards to avoid catastrophic forgetting or model poisoning from noisy data."
    },
    {
        "question": "What is the purpose of a model serving framework like TorchServe or TensorFlow Serving?",
        "options": [
            "To train models faster using distributed computing",
            "To expose trained models as scalable, low-latency inference APIs",
            "To visualize model architecture and layer activations",
            "To compress model weights before storing them"
        ],
        "answer": "To expose trained models as scalable, low-latency inference APIs",
        "category": "MLOps",
        "difficulty": "Easy",
        "explanation": "Model serving frameworks like TorchServe, TensorFlow Serving, and Triton Inference Server handle model loading, batching, versioning, and REST/gRPC API exposure. They optimize inference throughput and latency while supporting multiple model versions concurrently."
    },
    {
        "question": "What is model quantization and why is it used in MLOps?",
        "options": [
            "Evaluating model predictions using quantile regression",
            "Reducing model size and inference latency by representing weights with lower-precision numbers",
            "Splitting a large dataset into quantiles for stratified training",
            "Measuring uncertainty in model predictions using confidence intervals"
        ],
        "answer": "Reducing model size and inference latency by representing weights with lower-precision numbers",
        "category": "MLOps",
        "difficulty": "Medium",
        "explanation": "Quantization converts model weights from 32-bit floats to 8-bit integers (INT8) or lower. This reduces model size by up to 4x, speeds up inference (especially on hardware with INT8 support), and lowers memory bandwidth requirements with minimal accuracy loss."
    },
    {
        "question": "What is the purpose of a data pipeline in MLOps?",
        "options": [
            "Deploying models to production endpoints",
            "Automating the ingestion, transformation, validation, and delivery of data for model training and inference",
            "Monitoring production model predictions for anomalies",
            "Versioning trained model artifacts"
        ],
        "answer": "Automating the ingestion, transformation, validation, and delivery of data for model training and inference",
        "category": "MLOps",
        "difficulty": "Easy",
        "explanation": "Data pipelines orchestrate data flow from source systems through cleaning, transformation, feature engineering, and into training or serving systems. Tools like Apache Airflow, Prefect, and Dagster are used to schedule, monitor, and retry these workflows reliably."
    },
    {
        "question": "What is multi-armed bandit testing and how does it differ from A/B testing?",
        "options": [
            "A testing method that evaluates multiple models on offline data simultaneously",
            "An adaptive traffic allocation strategy that dynamically shifts traffic toward better-performing model variants during the experiment",
            "A method for training multiple models in parallel to reduce training time",
            "An ensemble approach where multiple models vote on each prediction"
        ],
        "answer": "An adaptive traffic allocation strategy that dynamically shifts traffic toward better-performing model variants during the experiment",
        "category": "MLOps",
        "difficulty": "Hard",
        "explanation": "Unlike A/B testing which uses fixed traffic splits, multi-armed bandit algorithms (e.g., epsilon-greedy, Thompson Sampling) continuously update traffic allocation to favor better-performing variants. This reduces regret (cost of serving a worse model) during experimentation."
    },
    {
        "question": "What is model pruning used for in production ML systems?",
        "options": [
            "Removing outlier data points from training sets",
            "Eliminating redundant or low-importance weights from a trained model to reduce size and improve inference speed",
            "Deleting old model versions from the registry",
            "Cutting underperforming features from the feature store"
        ],
        "answer": "Eliminating redundant or low-importance weights from a trained model to reduce size and improve inference speed",
        "category": "MLOps",
        "difficulty": "Medium",
        "explanation": "Model pruning removes weights (or neurons/heads) that contribute little to model output. Structured pruning removes entire channels or layers; unstructured pruning zeroes out individual weights. Combined with quantization, pruning significantly reduces model footprint for edge or mobile deployment."
    },
    {
        "question": "What is the difference between batch inference and real-time inference?",
        "options": [
            "Batch inference uses larger models while real-time uses smaller models",
            "Batch inference processes many samples offline on a schedule; real-time inference responds to individual requests with low latency",
            "Batch inference runs on GPUs while real-time inference only runs on CPUs",
            "Batch inference requires labeled data while real-time inference does not"
        ],
        "answer": "Batch inference processes many samples offline on a schedule; real-time inference responds to individual requests with low latency",
        "category": "MLOps",
        "difficulty": "Easy",
        "explanation": "Batch inference scores large datasets periodically (e.g., nightly churn predictions for all customers) and stores results. Real-time (online) inference serves predictions on-demand with millisecond latency (e.g., fraud detection at checkout). Choosing between them depends on latency requirements and use case."
    },
    {
        "question": "What is the purpose of data validation in an ML pipeline?",
        "options": [
            "Ensuring model weights meet a minimum accuracy threshold",
            "Checking incoming data for schema violations, anomalies, and distribution shifts before it reaches training or serving",
            "Validating that model hyperparameters are within acceptable ranges",
            "Confirming that model predictions match expected output formats"
        ],
        "answer": "Checking incoming data for schema violations, anomalies, and distribution shifts before it reaches training or serving",
        "category": "MLOps",
        "difficulty": "Medium",
        "explanation": "Data validation tools like TensorFlow Data Validation (TFDV) and Great Expectations automatically check data schemas, detect missing values, flag statistical anomalies, and compare feature distributions against a baseline. Catching bad data early prevents garbage-in-garbage-out failures."
    },
    {
        "question": "What is ML pipeline orchestration?",
        "options": [
            "The process of combining multiple models into an ensemble",
            "Coordinating and scheduling the sequence of steps in an ML workflow — from data ingestion to model deployment",
            "Managing API rate limits for model inference endpoints",
            "Distributing training data across multiple worker nodes"
        ],
        "answer": "Coordinating and scheduling the sequence of steps in an ML workflow — from data ingestion to model deployment",
        "category": "MLOps",
        "difficulty": "Medium",
        "explanation": "Pipeline orchestrators (Airflow, Kubeflow Pipelines, Metaflow, ZenML) define ML workflows as directed acyclic graphs (DAGs). They handle scheduling, dependency management, retries, logging, and parallelism — enabling reproducible, automated end-to-end ML pipelines."
    },
    {
        "question": "What is the purpose of model explainability tools in a production MLOps context?",
        "options": [
            "To speed up model inference by explaining which features to skip",
            "To provide human-interpretable reasons for individual predictions, enabling debugging, compliance, and trust",
            "To automatically generate model documentation for deployment",
            "To explain the training process to non-technical stakeholders"
        ],
        "answer": "To provide human-interpretable reasons for individual predictions, enabling debugging, compliance, and trust",
        "category": "MLOps",
        "difficulty": "Medium",
        "explanation": "Tools like SHAP, LIME, and Captum attribute model predictions to input features. In production, explainability helps debug unexpected predictions, satisfies regulatory requirements (e.g., GDPR right to explanation), and builds trust with end users and business stakeholders."
    },
    {
        "question": "What is a rollback strategy in ML deployment?",
        "options": [
            "Retraining the current model on freshly collected data",
            "Reverting production traffic to a previously stable model version when a new deployment degrades performance",
            "Rolling back the training dataset to a previous version",
            "Reverting hyperparameter changes made during the last experiment"
        ],
        "answer": "Reverting production traffic to a previously stable model version when a new deployment degrades performance",
        "category": "MLOps",
        "difficulty": "Easy",
        "explanation": "A rollback strategy ensures that if a newly deployed model causes a spike in errors, latency, or business metric degradation, traffic can be quickly redirected to the last known good model. Model registries and blue-green deployments make rollback fast and reliable."
    },
    {
        "question": "What is the purpose of a model card in MLOps?",
        "options": [
            "A configuration file specifying model hyperparameters",
            "A structured document describing a model's intended use, performance metrics, limitations, and ethical considerations",
            "A dashboard for real-time model performance monitoring",
            "An API specification for model inference endpoints"
        ],
        "answer": "A structured document describing a model's intended use, performance metrics, limitations, and ethical considerations",
        "category": "MLOps",
        "difficulty": "Easy",
        "explanation": "Model cards (introduced by Google) are standardized documentation artifacts attached to model releases. They communicate intended use cases, evaluation benchmarks across demographic groups, known limitations, and ethical considerations — supporting transparency and responsible AI deployment."
    },
    {
        "question": "What is transfer learning and how does it benefit MLOps workflows?",
        "options": [
            "Copying model weights from one registry to another",
            "Reusing a pretrained model as a starting point for a new task, reducing training time and data requirements",
            "Transferring a model from a development environment to production",
            "Moving training workloads from on-premise servers to the cloud"
        ],
        "answer": "Reusing a pretrained model as a starting point for a new task, reducing training time and data requirements",
        "category": "MLOps",
        "difficulty": "Easy",
        "explanation": "Transfer learning fine-tunes a model pretrained on a large dataset (e.g., ImageNet, BERT) for a specific downstream task. This dramatically reduces the compute and labeled data needed, accelerates the ML development cycle, and often yields better performance than training from scratch."
    },
    {
        "question": "What are SLOs (Service Level Objectives) in the context of ML model serving?",
        "options": [
            "Objectives set by the data science team for model accuracy on holdout sets",
            "Defined thresholds for operational metrics like latency, availability, and error rate that a production model must meet",
            "Business goals that an ML model is trained to optimize",
            "Training objectives that define the loss function used during model training"
        ],
        "answer": "Defined thresholds for operational metrics like latency, availability, and error rate that a production model must meet",
        "category": "MLOps",
        "difficulty": "Medium",
        "explanation": "SLOs (e.g., p99 latency < 200ms, availability > 99.9%) define the operational reliability targets for a model serving system. Alerts and on-call escalations are triggered when SLOs are breached, bridging ML engineering and site reliability engineering (SRE) practices."
    },
    {
        "question": "What is the purpose of request batching in model serving?",
        "options": [
            "Grouping multiple training examples into mini-batches for gradient descent",
            "Accumulating multiple inference requests and processing them together to improve GPU utilization and throughput",
            "Batching prediction results before writing them to a database",
            "Queuing model deployment requests to avoid simultaneous releases"
        ],
        "answer": "Accumulating multiple inference requests and processing them together to improve GPU utilization and throughput",
        "category": "MLOps",
        "difficulty": "Medium",
        "explanation": "Dynamic request batching collects multiple incoming inference calls within a short time window and processes them as a single batch. This dramatically improves GPU utilization (GPUs are optimized for parallel computation) and overall throughput at the cost of slightly increased latency per request."
    },
    {
        "question": "What is infrastructure as code (IaC) and why is it relevant to MLOps?",
        "options": [
            "Writing ML model logic in compiled languages for faster inference",
            "Defining and provisioning cloud infrastructure (compute, storage, networking) through version-controlled configuration files",
            "Storing training code alongside data in the same repository",
            "Automatically generating model architecture code from dataset statistics"
        ],
        "answer": "Defining and provisioning cloud infrastructure (compute, storage, networking) through version-controlled configuration files",
        "category": "MLOps",
        "difficulty": "Medium",
        "explanation": "IaC tools like Terraform and Pulumi allow ML teams to version, review, and reproduce the infrastructure powering their ML systems. This ensures consistent environments across dev/staging/production, enables disaster recovery, and supports collaborative infrastructure management."
    },
    {
        "question": "What is the concept of 'feedback loops' in production ML systems?",
        "options": [
            "The process of looping training data through the model multiple times per epoch",
            "When a model's predictions influence future training data, potentially amplifying biases or creating self-reinforcing errors",
            "Collecting user feedback to improve the UI around a model's predictions",
            "Feeding model evaluation metrics back into hyperparameter search"
        ],
        "answer": "When a model's predictions influence future training data, potentially amplifying biases or creating self-reinforcing errors",
        "category": "MLOps",
        "difficulty": "Hard",
        "explanation": "Feedback loops occur when a model's outputs affect the system that generates its future training data. For example, a recommendation model that only shows popular items will generate data that further reinforces popular items. Left unmanaged, this can cause runaway bias, filter bubbles, or model collapse."
    },
    {
        "question": "What is the purpose of a holdout set (test set) in the ML development lifecycle?",
        "options": [
            "Data withheld from the model to use as extra training examples if accuracy is insufficient",
            "An independent dataset used to provide an unbiased final evaluation of a model before deployment",
            "Data held back to train the next version of the model",
            "A dataset used exclusively for hyperparameter tuning"
        ],
        "answer": "An independent dataset used to provide an unbiased final evaluation of a model before deployment",
        "category": "MLOps",
        "difficulty": "Easy",
        "explanation": "The test set is kept completely separate from training and validation. It is used only once — for final evaluation before deployment — to estimate real-world performance. Repeated use of the test set for tuning decisions leads to overfitting to the test set and overly optimistic metrics."
    },
    {
        "question": "What is model distillation and why is it used in production?",
        "options": [
            "Purifying training data by removing noisy or mislabeled samples",
            "Training a smaller 'student' model to mimic the behavior of a larger 'teacher' model, producing a more efficient model",
            "Extracting feature importance scores from a trained model",
            "Reducing the number of layers in a model after training"
        ],
        "answer": "Training a smaller 'student' model to mimic the behavior of a larger 'teacher' model, producing a more efficient model",
        "category": "MLOps",
        "difficulty": "Hard",
        "explanation": "Knowledge distillation trains a compact student model on the soft probability outputs (logits) of a larger teacher model. The student learns richer information than from hard labels alone. The result is a smaller, faster model with accuracy close to the teacher — ideal for low-latency production deployment."
    },
    {
        "question": "What does 'model lineage' mean in MLOps?",
        "options": [
            "The family tree of model architectures derived from a common base paper",
            "The complete record of data, code, parameters, and environment used to produce a specific model artifact",
            "The sequence of model versions deployed to production over time",
            "The chain of approvals required before deploying a model to production"
        ],
        "answer": "The complete record of data, code, parameters, and environment used to produce a specific model artifact",
        "category": "MLOps",
        "difficulty": "Medium",
        "explanation": "Model lineage tracks the full provenance of a model: which dataset version, code commit, hyperparameters, and compute environment produced it. This is critical for debugging, auditing, regulatory compliance, and reproducing past results when investigating production incidents."
    },
    {
        "question": "What is the purpose of load testing an ML inference endpoint before production launch?",
        "options": [
            "Testing model accuracy on high-volume datasets",
            "Verifying that the serving infrastructure can handle expected peak traffic without latency degradation or failures",
            "Checking that the model loads correctly from the registry",
            "Ensuring the model produces correct outputs on edge-case inputs"
        ],
        "answer": "Verifying that the serving infrastructure can handle expected peak traffic without latency degradation or failures",
        "category": "MLOps",
        "difficulty": "Medium",
        "explanation": "Load testing (using tools like Locust or k6) simulates peak production traffic to identify bottlenecks, set auto-scaling thresholds, and confirm SLO compliance before launch. It prevents surprise outages when real traffic arrives and informs infrastructure sizing decisions."
    },
    {
        "question": "What is the primary advantage of using a managed ML platform (e.g., SageMaker, Vertex AI) over building custom MLOps infrastructure?",
        "options": [
            "Managed platforms always produce higher model accuracy",
            "They provide pre-built, integrated components for training, deployment, monitoring, and experiment tracking, reducing engineering overhead",
            "They automatically collect and label training data",
            "They eliminate the need to monitor models after deployment"
        ],
        "answer": "They provide pre-built, integrated components for training, deployment, monitoring, and experiment tracking, reducing engineering overhead",
        "category": "MLOps",
        "difficulty": "Easy",
        "explanation": "Managed platforms like AWS SageMaker, Google Vertex AI, and Azure ML offer integrated tooling for the entire ML lifecycle — reducing the time and expertise needed to build custom infrastructure. The tradeoff is vendor lock-in and less flexibility compared to open-source, self-managed stacks."
    },
    {
        "question": "What is the 'cold start' problem in ML model serving?",
        "options": [
            "A model that performs poorly at the start of training before loss converges",
            "The latency spike that occurs when a model instance is loaded from scratch to handle the first request after being idle",
            "The inability of a recommendation model to suggest items to new users with no history",
            "The delay caused by loading large training datasets from cold storage"
        ],
        "answer": "The latency spike that occurs when a model instance is loaded from scratch to handle the first request after being idle",
        "category": "MLOps",
        "difficulty": "Medium",
        "explanation": "Cold start latency occurs in serverless or auto-scaled deployments when a new instance must load model weights into memory before serving. Mitigations include keeping warm instances alive, model weight caching, using lighter quantized models, and provisioned concurrency in serverless platforms."
    },
    {
        "question": "What does 'model governance' refer to in enterprise MLOps?",
        "options": [
            "The process of selecting which ML framework to use for a project",
            "Policies, processes, and controls ensuring models are developed, validated, and deployed responsibly and in compliance with regulations",
            "Assigning computational resources to different ML projects",
            "Managing access to GPU clusters for training large models"
        ],
        "answer": "Policies, processes, and controls ensuring models are developed, validated, and deployed responsibly and in compliance with regulations",
        "category": "MLOps",
        "difficulty": "Hard",
        "explanation": "Model governance encompasses approval workflows, bias audits, performance benchmarks, documentation requirements, and audit trails for all models in production. It is especially critical in regulated industries (finance, healthcare) where model decisions must be explainable and traceable."
    },
    {
        "question": "What is the purpose of population stability index (PSI) in model monitoring?",
        "options": [
            "Measuring the diversity of the training dataset population",
            "Quantifying how much the distribution of a feature or score has shifted between a reference period and the current period",
            "Calculating the statistical significance of A/B test results",
            "Evaluating the stability of model weights across training runs"
        ],
        "answer": "Quantifying how much the distribution of a feature or score has shifted between a reference period and the current period",
        "category": "MLOps",
        "difficulty": "Hard",
        "explanation": "PSI compares the distribution of a variable (e.g., model scores or input features) between a baseline (training) and current production data. PSI < 0.1 suggests no significant shift; PSI > 0.2 typically triggers a model review or retraining. It is widely used in financial services ML monitoring."
    },
    {
        "question": "What is the difference between model retraining and model fine-tuning in a production context?",
        "options": [
            "Retraining uses new data while fine-tuning uses the original training data",
            "Retraining trains the model from scratch on updated data; fine-tuning continues training a deployed model on new data for incremental adaptation",
            "Retraining changes the model architecture while fine-tuning only adjusts hyperparameters",
            "Retraining is for supervised learning while fine-tuning is for unsupervised learning"
        ],
        "answer": "Retraining trains the model from scratch on updated data; fine-tuning continues training a deployed model on new data for incremental adaptation",
        "category": "MLOps",
        "difficulty": "Medium",
        "explanation": "Full retraining rebuilds the model from scratch using a refreshed dataset, ensuring no stale knowledge is retained. Fine-tuning updates an existing model's weights using new data, which is faster but risks catastrophic forgetting. The choice depends on the extent of drift and computational budget."
    },
    {
        "question": "What is the purpose of chaos engineering applied to ML systems?",
        "options": [
            "Introducing randomness into model training to improve generalization",
            "Deliberately injecting failures into ML infrastructure to identify weaknesses and validate system resilience",
            "Randomly sampling hyperparameter configurations during tuning",
            "Testing model robustness by adding noise to input data"
        ],
        "answer": "Deliberately injecting failures into ML infrastructure to identify weaknesses and validate system resilience",
        "category": "MLOps",
        "difficulty": "Hard",
        "explanation": "Chaos engineering (pioneered by Netflix) proactively tests system resilience by inducing failures like network latency, node crashes, or dependency outages. Applied to ML systems, it validates that serving infrastructure degrades gracefully, fallback models activate correctly, and monitoring alerts fire as expected."
    },
    {
        "question": "What is the significance of model latency percentiles (p50, p95, p99) versus average latency in production monitoring?",
        "options": [
            "Percentiles are only useful for batch inference; averages are better for real-time systems",
            "Percentile metrics reveal tail latency experienced by the slowest users, which average latency masks",
            "p50 measures model accuracy at the median threshold while p99 measures it at the 99th percentile",
            "Average latency is always a more reliable metric than percentile-based metrics"
        ],
        "answer": "Percentile metrics reveal tail latency experienced by the slowest users, which average latency masks",
        "category": "MLOps",
        "difficulty": "Medium",
        "explanation": "A low average latency can hide the fact that 1% of users experience very slow responses (p99 latency). SLOs are typically defined using tail percentiles (p95, p99) because these represent worst-case user experiences. Averages are easily skewed by a small number of fast requests masking degradation."
    },
    {
        "question": "What is continuous training (CT) in MLOps and when should it be triggered?",
        "options": [
            "Training a model continuously without stopping until it converges",
            "Automatically retraining a model on a schedule or when data drift, performance degradation, or new labeled data thresholds are met",
            "Running the training script continuously in the background on idle compute",
            "Training multiple model variants simultaneously and selecting the best one"
        ],
        "answer": "Automatically retraining a model on a schedule or when data drift, performance degradation, or new labeled data thresholds are met",
        "category": "MLOps",
        "difficulty": "Medium",
        "explanation": "Continuous Training (CT) extends CI/CD to include automated model retraining pipelines. Triggers include scheduled retraining (weekly), drift detection alerts, accumulation of new labeled data, or business metric degradation. CT ensures models stay current with evolving data distributions."
    },
    {
        "question": "What is the role of an ML metadata store?",
        "options": [
            "Storing raw training datasets in a structured format",
            "Tracking artifacts, executions, and lineage of all components in an ML pipeline to enable reproducibility and debugging",
            "Caching model predictions to reduce repeated computation",
            "Storing user interaction logs for future model training"
        ],
        "answer": "Tracking artifacts, executions, and lineage of all components in an ML pipeline to enable reproducibility and debugging",
        "category": "MLOps",
        "difficulty": "Hard",
        "explanation": "ML metadata stores (e.g., ML Metadata in TFX, MLflow tracking) record pipeline run metadata: which dataset was processed, what transformations were applied, which model artifact was produced, and how components are linked. This enables full lineage tracing, pipeline debugging, and audit compliance."
    },
    {
        "question": "What is the purpose of model fairness evaluation in MLOps?",
        "options": [
            "Ensuring that all team members contribute equally to model development",
            "Assessing whether a model produces systematically biased or discriminatory outcomes across different demographic groups",
            "Distributing model predictions fairly across different user segments",
            "Ensuring that compute resources are allocated fairly across ML projects"
        ],
        "answer": "Assessing whether a model produces systematically biased or discriminatory outcomes across different demographic groups",
        "category": "MLOps",
        "difficulty": "Medium",
        "explanation": "Fairness evaluation uses metrics like demographic parity, equalized odds, and disparate impact to detect performance gaps across groups (e.g., gender, race, age). Tools like Fairlearn and AI Fairness 360 are integrated into MLOps pipelines to surface and mitigate bias before deployment."
    },
    {
        "question": "What is the purpose of a staging environment in an MLOps deployment pipeline?",
        "options": [
            "A dedicated GPU cluster reserved for large-scale model training",
            "A production-like environment used to validate model behavior and infrastructure before releasing to real users",
            "A read-only copy of the production database used for analysis",
            "A sandboxed environment for data scientists to explore datasets"
        ],
        "answer": "A production-like environment used to validate model behavior and infrastructure before releasing to real users",
        "category": "MLOps",
        "difficulty": "Easy",
        "explanation": "A staging environment mirrors production in configuration, data access, and infrastructure. Models are deployed here first to run integration tests, performance benchmarks, and smoke tests. Only after passing staging validation is the model promoted to production, reducing the risk of regressions."
    },
    {
        "question": "What does 'model serving scalability' refer to in MLOps?",
        "options": [
            "The ability to train increasingly larger models over time",
            "The ability of inference infrastructure to handle increasing request volumes without degrading latency or availability",
            "Scaling the number of features used by a model during inference",
            "Increasing model accuracy by scaling up training data"
        ],
        "answer": "The ability of inference infrastructure to handle increasing request volumes without degrading latency or availability",
        "category": "MLOps",
        "difficulty": "Medium",
        "explanation": "Serving scalability is achieved through horizontal scaling (adding more model serving replicas), auto-scaling policies (scale out on CPU/latency thresholds), load balancing, and efficient batching. Without scalability planning, a sudden traffic spike can overwhelm inference servers and cause outages."
    },
    {
        "question": "What is a directed acyclic graph (DAG) and why is it fundamental to ML pipeline design?",
        "options": [
            "A type of neural network architecture used for sequence modeling",
            "A graph structure with no cycles used to represent task dependencies, ensuring each step executes in the correct order",
            "A visualization tool for displaying model decision boundaries",
            "A data structure for indexing features in a feature store"
        ],
        "answer": "A graph structure with no cycles used to represent task dependencies, ensuring each step executes in the correct order",
        "category": "MLOps",
        "difficulty": "Medium",
        "explanation": "ML pipelines are modeled as DAGs where nodes represent tasks (data ingestion, preprocessing, training, evaluation) and edges represent data dependencies. DAG execution ensures tasks run only after their upstream dependencies complete. Orchestrators like Airflow, Kubeflow, and Prefect are all DAG-based."
    },
    {
        "question": "What is the 'two-phase commit' challenge in ML feature pipelines?",
        "options": [
            "The requirement to train a model in two separate phases: pretraining and fine-tuning",
            "Ensuring that feature computation and storage are atomic so that training and serving always use consistent, synchronized feature values",
            "Running two separate validation checks before promoting a model to production",
            "Committing model weights to a registry in two stages: staging and production"
        ],
        "answer": "Ensuring that feature computation and storage are atomic so that training and serving always use consistent, synchronized feature values",
        "category": "MLOps",
        "difficulty": "Hard",
        "explanation": "In feature pipelines, a two-phase commit ensures that feature values written to the offline store (for training) and online store (for serving) are kept in sync. Without this consistency guarantee, models may train on slightly different feature representations than they serve on, causing subtle training-serving skew."
    },
    {
        "question": "What does accuracy measure in classification?",
        "options": [
            "The proportion of positive predictions that are correct",
            "The proportion of all predictions that are correct",
            "The proportion of actual positives that are detected",
            "The harmonic mean of precision and recall"
        ],
        "answer": "The proportion of all predictions that are correct",
        "category": "Model Evaluation",
        "difficulty": "Easy",
        "explanation": "Accuracy = (True Positives + True Negatives) / Total Samples. It measures overall correctness but can be misleading for imbalanced datasets — e.g., 99% accuracy on a dataset with 99% negatives by always predicting negative."
    },
    {
        "question": "What is cross-validation used for?",
        "options": [
            "Speeding up model training",
            "Comparing multiple model architectures in parallel",
            "Estimating model performance on unseen data more reliably",
            "Normalizing features before training"
        ],
        "answer": "Estimating model performance on unseen data more reliably",
        "category": "Model Evaluation",
        "difficulty": "Easy",
        "explanation": "Cross-validation (e.g., k-fold) partitions data into k subsets, trains on k-1 and validates on 1, rotating through all folds. This gives a more robust performance estimate than a single train/test split."
    },
    {
        "question": "What does the ROC-AUC metric measure?",
        "options": [
            "The model's training speed relative to baseline",
            "The area under the curve of True Positive Rate vs False Positive Rate",
            "The ratio of precision to recall across all thresholds",
            "The overall accuracy at a single classification threshold"
        ],
        "answer": "The area under the curve of True Positive Rate vs False Positive Rate",
        "category": "Model Evaluation",
        "difficulty": "Medium",
        "explanation": "ROC-AUC measures a classifier's ability to discriminate between classes across all decision thresholds. An AUC of 1.0 is perfect; 0.5 is random. It's threshold-independent and robust to class imbalance."
    },
    {
        "question": "When is F1-Score preferred over accuracy?",
        "options": [
            "When the dataset is perfectly balanced",
            "When speed of prediction is critical",
            "When classes are imbalanced and both false positives and false negatives matter",
            "When the model has more than 10 output classes"
        ],
        "answer": "When classes are imbalanced and both false positives and false negatives matter",
        "category": "Model Evaluation",
        "difficulty": "Medium",
        "explanation": "F1 = 2 × (Precision × Recall) / (Precision + Recall). It balances precision and recall, making it ideal for imbalanced classification tasks (e.g., fraud detection, medical diagnosis) where accuracy would be misleadingly high."
    },
    {
        "question": "What is a confusion matrix?",
        "options": [
            "A table showing model hyperparameters",
            "A matrix of feature correlations",
            "A table showing TP, FP, TN, FN counts for a classifier",
            "A visualization of decision tree splits"
        ],
        "answer": "A table showing TP, FP, TN, FN counts for a classifier",
        "category": "Model Evaluation",
        "difficulty": "Medium",
        "explanation": "A confusion matrix summarizes classification results: rows represent actual classes, columns represent predicted classes. From it you can compute accuracy, precision, recall, F1, and other metrics at a glance."
    },
    {
        "question": "What is the difference between precision and recall?",
        "options": [
            "Precision measures training accuracy; recall measures test accuracy",
            "Precision = TP/(TP+FP); Recall = TP/(TP+FN)",
            "Precision = TP/(TP+FN); Recall = TP/(TP+FP)",
            "They are identical metrics with different names"
        ],
        "answer": "Precision = TP/(TP+FP); Recall = TP/(TP+FN)",
        "category": "Model Evaluation",
        "difficulty": "Hard",
        "explanation": "Precision answers 'of all predicted positives, how many are actually positive?' Recall answers 'of all actual positives, how many did we catch?' There's a tradeoff: raising the classification threshold increases precision but lowers recall."
    },
    {
        "question": "What is a baseline model?",
        "options": [
            "The most complex model in the experiment",
            "A simple reference model used to compare performance against",
            "The model trained on the smallest dataset",
            "A model trained without any regularization"
        ],
        "answer": "A simple reference model used to compare performance against",
        "category": "Model Evaluation",
        "difficulty": "Easy",
        "explanation": "A baseline (e.g., predicting the majority class, using mean value, or a simple logistic regression) sets the minimum bar for model usefulness. If a sophisticated model barely beats the baseline, it may not justify the added complexity."
    },
    {
        "question": "What does RMSE (Root Mean Squared Error) measure?",
        "options": [
            "The proportion of correct predictions in classification",
            "The average squared distance between predicted and actual values, square-rooted",
            "The correlation between predictions and ground truth",
            "The maximum error across all predictions"
        ],
        "answer": "The average squared distance between predicted and actual values, square-rooted",
        "category": "Model Evaluation",
        "difficulty": "Easy",
        "explanation": "RMSE = sqrt(mean((y_pred - y_true)^2)). It penalizes large errors more than MAE due to squaring, is in the same units as the target, and is sensitive to outliers. It is widely used for regression tasks like forecasting."
    },
    {
        "question": "What is the precision-recall curve used for?",
        "options": [
            "Plotting model accuracy vs. training time",
            "Visualizing the trade-off between precision and recall at various classification thresholds",
            "Comparing two models on the same dataset",
            "Showing the distribution of predicted probabilities"
        ],
        "answer": "Visualizing the trade-off between precision and recall at various classification thresholds",
        "category": "Model Evaluation",
        "difficulty": "Medium",
        "explanation": "As the classification threshold changes, precision and recall change inversely. The PR curve plots all (recall, precision) pairs, and the area under it (Average Precision) summarizes performance. It is more informative than ROC-AUC for heavily imbalanced datasets."
    },
    {
        "question": "What is BLEU score used for?",
        "options": [
            "Evaluating the accuracy of classification models",
            "Measuring the quality of machine-generated text by comparing it to reference translations",
            "Computing the perplexity of a language model",
            "Evaluating clustering quality using centroids"
        ],
        "answer": "Measuring the quality of machine-generated text by comparing it to reference translations",
        "category": "Model Evaluation",
        "difficulty": "Medium",
        "explanation": "BLEU (Bilingual Evaluation Understudy) measures n-gram overlap between generated and reference text. It is widely used for machine translation evaluation, though it has known limitations since it does not capture semantics or fluency directly."
    },
    {
        "question": "What does 'calibration' mean for a probabilistic classifier?",
        "options": [
            "Tuning hyperparameters using grid search",
            "Ensuring predicted probabilities reflect the true frequency of outcomes",
            "Adjusting the decision threshold to optimize F1 score",
            "Normalizing the feature space before prediction"
        ],
        "answer": "Ensuring predicted probabilities reflect the true frequency of outcomes",
        "category": "Model Evaluation",
        "difficulty": "Medium",
        "explanation": "A well-calibrated model outputs probabilities that match empirical frequencies — when it predicts 80% probability, it should be right about 80% of the time. Calibration is critical in medical, financial, and risk applications. Reliability diagrams and Platt scaling help assess and fix miscalibration."
    },
    {
        "question": "What is the difference between macro and micro-averaged F1 score?",
        "options": [
            "Macro averages across samples; micro averages across classes",
            "Macro computes F1 per class then averages equally; micro aggregates TP/FP/FN globally before computing F1",
            "They are identical for balanced datasets only",
            "Micro-F1 ignores minority classes; macro-F1 weights by support"
        ],
        "answer": "Macro computes F1 per class then averages equally; micro aggregates TP/FP/FN globally before computing F1",
        "category": "Model Evaluation",
        "difficulty": "Hard",
        "explanation": "Macro-F1 gives equal weight to each class regardless of support — useful when minority class performance matters. Micro-F1 aggregates contributions of all classes, effectively weighting by frequency, so it is driven by majority classes. For imbalanced datasets, the two diverge significantly."
    },
    {
        "question": "What is perplexity as a metric for language models?",
        "options": [
            "The average length of generated sequences",
            "The exponentiated average negative log-likelihood, measuring how well the model predicts a held-out corpus",
            "The proportion of out-of-vocabulary words in the test set",
            "The variance of token probabilities across the vocabulary"
        ],
        "answer": "The exponentiated average negative log-likelihood, measuring how well the model predicts a held-out corpus",
        "category": "Model Evaluation",
        "difficulty": "Hard",
        "explanation": "Perplexity = exp(-1/N * sum(log P(w_i))). A lower perplexity means the model assigns higher probability to the test text, indicating better predictive performance. It is the standard intrinsic evaluation metric for language models, though it does not directly measure downstream task quality."
    },
    {
        "question": "What does MAE (Mean Absolute Error) measure in regression?",
        "options": [
            "The maximum difference between any prediction and its true value",
            "The average of the absolute differences between predicted and actual values",
            "The squared correlation between predictions and ground truth",
            "The ratio of correct predictions to total predictions"
        ],
        "answer": "The average of the absolute differences between predicted and actual values",
        "category": "Model Evaluation",
        "difficulty": "Easy",
        "explanation": "MAE = mean(|y_pred - y_true|). Unlike RMSE, MAE treats all errors equally without squaring, making it less sensitive to outliers. It is easy to interpret since it shares the same units as the target variable."
    },
    {
        "question": "What is overfitting in machine learning?",
        "options": [
            "When a model performs poorly on both training and test data",
            "When a model learns the training data too well, including noise, and fails to generalize",
            "When a model is too simple to capture the underlying patterns",
            "When a model is trained on too little data"
        ],
        "answer": "When a model learns the training data too well, including noise, and fails to generalize",
        "category": "Model Evaluation",
        "difficulty": "Easy",
        "explanation": "An overfit model has low training error but high test/validation error. It memorizes noise rather than learning the true signal. Symptoms include a large gap between training and validation metrics. Remedies include regularization, dropout, more data, and early stopping."
    },
    {
        "question": "What is underfitting in machine learning?",
        "options": [
            "When a model performs well on training data but poorly on test data",
            "When a model is too complex relative to the data",
            "When a model is too simple to capture the underlying patterns in the data",
            "When the training dataset is too large for the model to process"
        ],
        "answer": "When a model is too simple to capture the underlying patterns in the data",
        "category": "Model Evaluation",
        "difficulty": "Easy",
        "explanation": "An underfit model has high bias and performs poorly on both training and test data. It fails to capture the complexity of the target function. Solutions include using more complex models, adding features, or reducing regularization."
    },
    {
        "question": "What is the bias-variance tradeoff?",
        "options": [
            "The tradeoff between model accuracy and inference speed",
            "The tension between a model's error due to wrong assumptions (bias) and sensitivity to training data fluctuations (variance)",
            "The tradeoff between the number of features and the number of training samples",
            "The balance between precision and recall in binary classification"
        ],
        "answer": "The tension between a model's error due to wrong assumptions (bias) and sensitivity to training data fluctuations (variance)",
        "category": "Model Evaluation",
        "difficulty": "Medium",
        "explanation": "High bias leads to underfitting; high variance leads to overfitting. Total expected error = Bias² + Variance + Irreducible Noise. Increasing model complexity reduces bias but increases variance. The goal is to find the sweet spot that minimizes total generalization error."
    },
    {
        "question": "What is stratified k-fold cross-validation?",
        "options": [
            "A variant of k-fold that sorts data by feature value before splitting",
            "A variant of k-fold that preserves the class distribution in each fold",
            "A method that uses k different random seeds for training",
            "A technique that splits data based on time order"
        ],
        "answer": "A variant of k-fold that preserves the class distribution in each fold",
        "category": "Model Evaluation",
        "difficulty": "Medium",
        "explanation": "Stratified k-fold ensures each fold has approximately the same proportion of class labels as the full dataset. This is especially important for imbalanced datasets where random splits might place very few minority-class samples in some folds."
    },
    {
        "question": "What does a learning curve plot in model evaluation?",
        "options": [
            "The model's parameter values over training epochs",
            "Training and validation performance as a function of training set size",
            "The gradient magnitude across layers during backpropagation",
            "The ROC curve after each training epoch"
        ],
        "answer": "Training and validation performance as a function of training set size",
        "category": "Model Evaluation",
        "difficulty": "Medium",
        "explanation": "Learning curves help diagnose bias vs. variance problems. If both curves plateau at a high error, the model underfits (high bias). If there is a large gap between training and validation curves, the model overfits (high variance). Adding more data helps close variance gaps."
    },
    {
        "question": "What is the purpose of a held-out test set?",
        "options": [
            "To tune hyperparameters during model development",
            "To provide a final unbiased estimate of model performance after all development decisions",
            "To augment training data when the dataset is small",
            "To normalize features before training begins"
        ],
        "answer": "To provide a final unbiased estimate of model performance after all development decisions",
        "category": "Model Evaluation",
        "difficulty": "Easy",
        "explanation": "The test set should never be touched during training or hyperparameter tuning. Using it only once at the very end ensures an honest estimate of generalization performance. Repeated evaluation on the test set leads to data leakage and overly optimistic results."
    },
    {
        "question": "What is the R-squared (R²) metric in regression?",
        "options": [
            "The root mean squared error normalized by the target range",
            "The proportion of variance in the target variable explained by the model",
            "The Pearson correlation coefficient between predictions and actuals",
            "The mean absolute percentage error of the regression model"
        ],
        "answer": "The proportion of variance in the target variable explained by the model",
        "category": "Model Evaluation",
        "difficulty": "Medium",
        "explanation": "R² = 1 - (SS_res / SS_tot), where SS_res is the residual sum of squares and SS_tot is the total variance. A value of 1.0 means perfect prediction; 0.0 means the model does no better than predicting the mean. R² can be negative for severely poor models."
    },
    {
        "question": "What is data leakage in model evaluation?",
        "options": [
            "When training data is accidentally deleted",
            "When information from the test set or future data influences the training process",
            "When a model's weights are shared between different experiments",
            "When the validation set is too small to be representative"
        ],
        "answer": "When information from the test set or future data influences the training process",
        "category": "Model Evaluation",
        "difficulty": "Medium",
        "explanation": "Data leakage causes models to appear better than they truly are. Common sources include feature engineering using test-set statistics, using future information in time-series tasks, or including the target variable (or proxies) as a feature. It leads to falsely optimistic evaluation results."
    },
    {
        "question": "What is the specificity metric in classification?",
        "options": [
            "The proportion of actual positives correctly identified",
            "The proportion of actual negatives correctly identified",
            "The proportion of predicted positives that are correct",
            "The harmonic mean of precision and recall"
        ],
        "answer": "The proportion of actual negatives correctly identified",
        "category": "Model Evaluation",
        "difficulty": "Medium",
        "explanation": "Specificity = TN / (TN + FP), also called the True Negative Rate. It measures how well the model avoids false alarms. Specificity and recall (sensitivity) are often considered together, especially in medical screening where avoiding false negatives (sensitivity) and false positives (specificity) both matter."
    },
    {
        "question": "What does the silhouette score measure?",
        "options": [
            "The accuracy of a binary classifier at a fixed threshold",
            "How similar a data point is to its own cluster compared to other clusters",
            "The distance between centroids of different clusters",
            "The proportion of variance explained by the first principal component"
        ],
        "answer": "How similar a data point is to its own cluster compared to other clusters",
        "category": "Model Evaluation",
        "difficulty": "Medium",
        "explanation": "The silhouette score ranges from -1 to 1. A high score means the point is well-matched to its cluster and poorly matched to neighboring clusters. It is commonly used to evaluate unsupervised clustering algorithms such as K-Means when ground truth labels are unavailable."
    },
    {
        "question": "What is early stopping in model training?",
        "options": [
            "Ending training after a fixed number of epochs regardless of performance",
            "Halting training when validation performance stops improving to prevent overfitting",
            "Reducing the learning rate when training loss plateaus",
            "Stopping training once training accuracy reaches 100%"
        ],
        "answer": "Halting training when validation performance stops improving to prevent overfitting",
        "category": "Model Evaluation",
        "difficulty": "Easy",
        "explanation": "Early stopping monitors a validation metric (e.g., validation loss) and stops training when it ceases to improve for a set number of epochs (patience). It acts as a form of regularization, preventing the model from overfitting to the training set by training too long."
    },
    {
        "question": "What is the purpose of the validation set in model development?",
        "options": [
            "To replace the test set for final performance reporting",
            "To evaluate and tune the model during development without touching the test set",
            "To augment the training set using data augmentation techniques",
            "To measure irreducible noise in the dataset"
        ],
        "answer": "To evaluate and tune the model during development without touching the test set",
        "category": "Model Evaluation",
        "difficulty": "Easy",
        "explanation": "The validation set is a portion of data set aside from training and separate from the test set. It is used for hyperparameter tuning, model selection, and monitoring overfitting during training. This preserves the test set's integrity as a final, unbiased evaluator."
    },
    {
        "question": "What is MAPE (Mean Absolute Percentage Error)?",
        "options": [
            "The absolute difference between the best and worst predictions",
            "The average of percentage errors between predictions and actual values",
            "The squared percentage difference between model predictions",
            "The ratio of MAE to RMSE for a given regression model"
        ],
        "answer": "The average of percentage errors between predictions and actual values",
        "category": "Model Evaluation",
        "difficulty": "Medium",
        "explanation": "MAPE = mean(|y_pred - y_true| / |y_true|) × 100%. It expresses prediction error as a percentage of the actual value, making it scale-independent and easy to communicate. However, it is undefined when y_true = 0 and penalizes under-predictions more than over-predictions."
    },
    {
        "question": "What is the Matthews Correlation Coefficient (MCC)?",
        "options": [
            "The Pearson correlation between predicted probabilities and binary labels",
            "A balanced metric for binary classification that uses TP, TN, FP, and FN",
            "The covariance between two different classifiers' output distributions",
            "The geometric mean of precision and recall"
        ],
        "answer": "A balanced metric for binary classification that uses TP, TN, FP, and FN",
        "category": "Model Evaluation",
        "difficulty": "Hard",
        "explanation": "MCC = (TP×TN - FP×FN) / sqrt((TP+FP)(TP+FN)(TN+FP)(TN+FN)). It ranges from -1 (perfect inverse predictions) to +1 (perfect predictions), with 0 indicating random. It is considered one of the most informative single-number scores for binary classification, especially on imbalanced data."
    },
    {
        "question": "What is leave-one-out cross-validation (LOOCV)?",
        "options": [
            "A method that removes one feature at a time to measure its importance",
            "A special case of k-fold where k equals the number of samples",
            "A technique that excludes the worst-performing fold from the average",
            "A validation strategy that reserves one class for testing"
        ],
        "answer": "A special case of k-fold where k equals the number of samples",
        "category": "Model Evaluation",
        "difficulty": "Hard",
        "explanation": "In LOOCV, each sample is used once as the validation set while the model trains on the remaining n-1 samples. It provides a nearly unbiased estimate of generalization performance but is computationally expensive for large datasets. It is preferred when data is very scarce."
    },
    {
        "question": "What does the False Positive Rate (FPR) represent?",
        "options": [
            "The proportion of actual positives incorrectly classified as negative",
            "The proportion of actual negatives incorrectly classified as positive",
            "The proportion of predicted positives that are actually negative",
            "The number of false positives divided by total predictions"
        ],
        "answer": "The proportion of actual negatives incorrectly classified as positive",
        "category": "Model Evaluation",
        "difficulty": "Medium",
        "explanation": "FPR = FP / (FP + TN). It is the x-axis of the ROC curve, measuring the false alarm rate. A high FPR means the model often incorrectly flags negative instances as positive. FPR is the complement of specificity: FPR = 1 - Specificity."
    },
    {
        "question": "What is the purpose of the Brier score?",
        "options": [
            "Evaluating ranking quality for information retrieval tasks",
            "Measuring the mean squared error between predicted probabilities and actual binary outcomes",
            "Assessing the uncertainty of Bayesian posterior distributions",
            "Measuring the accuracy of multi-class classifiers using softmax outputs"
        ],
        "answer": "Measuring the mean squared error between predicted probabilities and actual binary outcomes",
        "category": "Model Evaluation",
        "difficulty": "Hard",
        "explanation": "Brier Score = mean((p_pred - y_true)²), where p_pred is the predicted probability and y_true is 0 or 1. Lower scores are better (0 = perfect, 1 = worst). It evaluates both calibration and sharpness, making it useful whenever probabilistic predictions rather than hard class labels are needed."
    },
    {
        "question": "What is the difference between the training error and the generalization error?",
        "options": [
            "Training error uses cross-entropy; generalization error uses MSE",
            "Training error is measured on training data; generalization error is the expected error on new unseen data",
            "Generalization error decreases monotonically as the model becomes more complex",
            "They are numerically equal for well-regularized models"
        ],
        "answer": "Training error is measured on training data; generalization error is the expected error on new unseen data",
        "category": "Model Evaluation",
        "difficulty": "Medium",
        "explanation": "Training error tends to underestimate generalization error because the model has already seen the training data. The gap between them indicates overfitting. The test set provides an empirical estimate of generalization error, which is why it must be kept separate throughout development."
    },
    {
        "question": "What is the ROUGE metric used for?",
        "options": [
            "Evaluating image segmentation quality",
            "Measuring the overlap between machine-generated summaries and reference summaries",
            "Scoring the diversity of a language model's generated text",
            "Assessing the consistency of a neural network's attention weights"
        ],
        "answer": "Measuring the overlap between machine-generated summaries and reference summaries",
        "category": "Model Evaluation",
        "difficulty": "Medium",
        "explanation": "ROUGE (Recall-Oriented Understudy for Gisting Evaluation) measures recall-based n-gram overlap between generated and reference texts. ROUGE-N counts n-gram matches; ROUGE-L uses the longest common subsequence. It is the standard automatic metric for text summarization evaluation."
    },
    {
        "question": "What is a Type I error in hypothesis testing and model evaluation?",
        "options": [
            "Failing to detect a true effect (false negative)",
            "Incorrectly rejecting a true null hypothesis (false positive)",
            "Accepting a false alternative hypothesis with high confidence",
            "Overfitting the model to the training data"
        ],
        "answer": "Incorrectly rejecting a true null hypothesis (false positive)",
        "category": "Model Evaluation",
        "difficulty": "Medium",
        "explanation": "A Type I error (false positive) occurs when a test incorrectly concludes there is an effect when there is none. In model evaluation, this parallels a classifier flagging a negative as positive. The probability of a Type I error is controlled by the significance level α (e.g., 0.05)."
    },
    {
        "question": "What is a Type II error in hypothesis testing and model evaluation?",
        "options": [
            "Incorrectly rejecting a true null hypothesis",
            "Failing to reject a false null hypothesis (false negative)",
            "Using the wrong loss function during training",
            "Misclassifying a majority-class sample as minority class"
        ],
        "answer": "Failing to reject a false null hypothesis (false negative)",
        "category": "Model Evaluation",
        "difficulty": "Medium",
        "explanation": "A Type II error (false negative) occurs when a test fails to detect a real effect. In classification, this corresponds to missing actual positive cases. The probability of a Type II error is β, and statistical power = 1 − β. Reducing Type II errors often requires larger sample sizes or more sensitive tests."
    },
    {
        "question": "What does the Jaccard Index measure in the context of model evaluation?",
        "options": [
            "The overlap between two probability distributions",
            "The ratio of the intersection to the union of predicted and actual positive sets",
            "The correlation between two regression model outputs",
            "The proportion of features shared between training and test sets"
        ],
        "answer": "The ratio of the intersection to the union of predicted and actual positive sets",
        "category": "Model Evaluation",
        "difficulty": "Hard",
        "explanation": "Jaccard Index = |A ∩ B| / |A ∪ B|. In binary classification, A is the set of predicted positives and B is the set of actual positives. It penalizes both false positives and false negatives, ranges from 0 to 1, and is commonly used in segmentation and multi-label classification tasks."
    },
    {
        "question": "What is the difference between parametric and non-parametric model evaluation?",
        "options": [
            "Parametric evaluation uses fixed thresholds; non-parametric uses moving thresholds",
            "Parametric evaluation assumes a specific distribution of errors; non-parametric does not",
            "Non-parametric evaluation only applies to neural networks",
            "Parametric evaluation is used only for regression; non-parametric for classification"
        ],
        "answer": "Parametric evaluation assumes a specific distribution of errors; non-parametric does not",
        "category": "Model Evaluation",
        "difficulty": "Hard",
        "explanation": "Parametric statistical tests (e.g., t-test) assume errors follow a known distribution (typically Gaussian). Non-parametric tests (e.g., Wilcoxon signed-rank test) make no such assumptions and are more appropriate when comparing model performances across multiple datasets or when normality cannot be assumed."
    },
    {
        "question": "What is concept drift in the context of deployed model evaluation?",
        "options": [
            "A drop in model accuracy caused by software updates",
            "A change in the statistical properties of the input data or target variable over time",
            "The gradual increase in model complexity after deployment",
            "A shift in evaluation metrics caused by relabeling the training data"
        ],
        "answer": "A change in the statistical properties of the input data or target variable over time",
        "category": "Model Evaluation",
        "difficulty": "Medium",
        "explanation": "Concept drift occurs when the real-world distribution that a model was trained on changes over time, degrading performance. Examples include seasonal shifts in user behavior or economic changes affecting predictions. Monitoring for drift requires tracking live model metrics and comparing feature distributions to the training baseline."
    },
    {
        "question": "What is the purpose of a shadow evaluation (shadow mode testing)?",
        "options": [
            "Evaluating a model only on data it has never seen before",
            "Running a new model in parallel with the production model to compare outputs before full deployment",
            "Testing a model exclusively on adversarial examples",
            "Evaluating a model after removing the top-performing features"
        ],
        "answer": "Running a new model in parallel with the production model to compare outputs before full deployment",
        "category": "Model Evaluation",
        "difficulty": "Hard",
        "explanation": "In shadow mode, a candidate model processes real production traffic alongside the live model but its outputs are logged rather than served. This allows comparison of new vs. old model behavior on real-world data without any risk to users, providing a realistic evaluation before full rollout."
    },
    {
        "question": "What is the expected calibration error (ECE)?",
        "options": [
            "The average difference between predicted probabilities and the model's training loss",
            "A scalar summary of calibration quality measuring the weighted gap between confidence and accuracy",
            "The variance of the model's predicted probabilities across the validation set",
            "The mean squared error between softmax outputs and one-hot labels"
        ],
        "answer": "A scalar summary of calibration quality measuring the weighted gap between confidence and accuracy",
        "category": "Model Evaluation",
        "difficulty": "Hard",
        "explanation": "ECE bins predictions by confidence level and computes the weighted average of |accuracy - confidence| across bins. Lower ECE indicates better calibration. It is the most common quantitative metric for assessing probability calibration in classification models, complementing reliability diagrams."
    },
    {
        "question": "What is the purpose of a residual plot in regression model evaluation?",
        "options": [
            "Plotting predicted values against training loss over epochs",
            "Visualizing the differences between predicted and actual values to check model assumptions",
            "Displaying the distribution of feature importance scores",
            "Showing the correlation matrix between input features"
        ],
        "answer": "Visualizing the differences between predicted and actual values to check model assumptions",
        "category": "Model Evaluation",
        "difficulty": "Medium",
        "explanation": "A residual plot shows residuals (y_true - y_pred) vs. predicted values or a feature. Ideally, residuals should be randomly scattered around zero with no pattern. Systematic patterns indicate model misspecification, non-linearity, or heteroscedasticity that the model is not capturing."
    },
    {
        "question": "What is the purpose of A/B testing in model evaluation?",
        "options": [
            "Comparing two different feature engineering strategies on the same model",
            "Randomly assigning users to two versions of a model to measure real-world performance differences",
            "Training two models on different subsets of data and averaging their predictions",
            "Running two different hyperparameter searches in parallel"
        ],
        "answer": "Randomly assigning users to two versions of a model to measure real-world performance differences",
        "category": "Model Evaluation",
        "difficulty": "Medium",
        "explanation": "A/B testing (online controlled experiment) exposes different user groups to different model versions and measures outcomes using business or ML metrics. It is the gold standard for evaluating live model impact, controlling for confounders through randomization, and detecting statistically significant improvements."
    },
    {
        "question": "What is the concordance index (C-index) used for?",
        "options": [
            "Measuring text coherence in NLP summarization models",
            "Evaluating the discriminative ability of survival or risk models",
            "Computing the average ranking loss across classification thresholds",
            "Assessing consistency of predictions across multiple cross-validation folds"
        ],
        "answer": "Evaluating the discriminative ability of survival or risk models",
        "category": "Model Evaluation",
        "difficulty": "Hard",
        "explanation": "The C-index measures how well a model ranks subjects by predicted risk — it is the probability that for two randomly chosen subjects, the one with a higher predicted risk experiences the event first. A C-index of 0.5 is random; 1.0 is perfect. It generalizes ROC-AUC to survival analysis with censored data."
    },
    {
        "question": "What is the purpose of the mean reciprocal rank (MRR) metric?",
        "options": [
            "Measuring average accuracy across multiple binary classifiers",
            "Evaluating ranking systems by averaging the reciprocal rank of the first correct result",
            "Computing the mean rank of false positives in a ranked list",
            "Measuring how quickly a model converges during training"
        ],
        "answer": "Evaluating ranking systems by averaging the reciprocal rank of the first correct result",
        "category": "Model Evaluation",
        "difficulty": "Hard",
        "explanation": "MRR = mean(1/rank_i) where rank_i is the position of the first relevant result for query i. It rewards systems that place correct answers higher in the ranking. MRR is commonly used to evaluate information retrieval, question answering, and recommendation systems."
    },
    {
        "question": "What does 'top-k accuracy' mean in multi-class classification?",
        "options": [
            "The accuracy of the model on the k hardest samples in the test set",
            "Whether the correct class appears among the model's k highest-confidence predictions",
            "The accuracy computed using only the k most frequent classes",
            "The average accuracy across k different random seeds"
        ],
        "answer": "Whether the correct class appears among the model's k highest-confidence predictions",
        "category": "Model Evaluation",
        "difficulty": "Medium",
        "explanation": "Top-k accuracy (e.g., top-5) counts a prediction as correct if the true label is among the k classes with the highest predicted probability. It is commonly used in image classification benchmarks like ImageNet, where distinguishing visually similar classes is inherently ambiguous."
    },
    {
        "question": "What is the purpose of a Q-Q (quantile-quantile) plot in regression model evaluation?",
        "options": [
            "Plotting the distribution of predicted classes against actual classes",
            "Comparing the distribution of residuals against a theoretical normal distribution",
            "Visualizing the model's performance across different quantiles of the input",
            "Displaying the cumulative distribution of model confidence scores"
        ],
        "answer": "Comparing the distribution of residuals against a theoretical normal distribution",
        "category": "Model Evaluation",
        "difficulty": "Medium",
        "explanation": "A Q-Q plot maps quantiles of the observed residuals against quantiles of a theoretical distribution (usually normal). If the points lie close to the diagonal, the residuals are approximately normally distributed — a key assumption of ordinary least squares regression. Deviations indicate skewness, heavy tails, or outliers."
    },
    {
        "question": "What is the log-loss (cross-entropy loss) metric used for?",
        "options": [
            "Measuring the distance between predicted and actual cluster centroids",
            "Evaluating the quality of probabilistic predictions by penalizing confident wrong predictions heavily",
            "Computing the squared error between regression predictions and targets",
            "Measuring the information gain of each feature in a decision tree"
        ],
        "answer": "Evaluating the quality of probabilistic predictions by penalizing confident wrong predictions heavily",
        "category": "Model Evaluation",
        "difficulty": "Medium",
        "explanation": "Log-loss = -mean(y*log(p) + (1-y)*log(1-p)). Lower is better (0 = perfect). It strongly penalizes predictions that are both confident and wrong, encouraging well-calibrated probability outputs. It is the standard evaluation metric for probabilistic binary and multi-class classifiers."
    },
    {
        "question": "What is domain adaptation evaluation, and why is it important?",
        "options": [
            "Evaluating a model using only the data distribution it was originally trained on",
            "Assessing how well a model performs when the test distribution differs from the training distribution",
            "Measuring accuracy improvements after fine-tuning on the full training dataset",
            "Comparing evaluation metrics between supervised and unsupervised models"
        ],
        "answer": "Assessing how well a model performs when the test distribution differs from the training distribution",
        "category": "Model Evaluation",
        "difficulty": "Hard",
        "explanation": "Domain adaptation evaluation measures model robustness when deployed in a different domain than training (e.g., a medical NLP model trained on clinical notes evaluated on patient records). Performance drops across domains reveal over-specialization. Techniques like domain-adversarial training and fine-tuning help improve cross-domain generalization."
    },
    {
        "question": "What is the difference between online and offline model evaluation?",
        "options": [
            "Online evaluation uses neural networks; offline evaluation uses traditional ML",
            "Offline evaluation uses static historical datasets; online evaluation measures performance on live production traffic",
            "Online evaluation requires labeled data; offline evaluation is unsupervised",
            "Offline evaluation is faster because it requires no data collection"
        ],
        "answer": "Offline evaluation uses static historical datasets; online evaluation measures performance on live production traffic",
        "category": "Model Evaluation",
        "difficulty": "Medium",
        "explanation": "Offline evaluation (using held-out test sets, cross-validation) is fast and reproducible but may not reflect real-world behavior. Online evaluation via A/B tests or shadow testing captures actual user interactions but is slower, costlier, and harder to control. Both are needed for robust model assessment in production systems."
    },
    {
        "question": "What is the purpose of the Kolmogorov-Smirnov (KS) statistic in model evaluation?",
        "options": [
            "Measuring the F1-score of a multi-class classifier",
            "Quantifying the maximum difference between two cumulative distribution functions",
            "Computing the correlation between residuals in regression",
            "Evaluating the sharpness of a probabilistic forecast"
        ],
        "answer": "Quantifying the maximum difference between two cumulative distribution functions",
        "category": "Model Evaluation",
        "difficulty": "Hard",
        "explanation": "In credit scoring and binary classification, the KS statistic measures the maximum separation between the cumulative distributions of predicted scores for positives and negatives. A higher KS value indicates better class separation. It is also used in drift detection to compare the distribution of features between training and production data."
    },
    {
        "question": "What does the pandas DataFrame.dropna() method do?",
        "options": [
            "Replaces missing values with the column mean",
            "Removes rows or columns containing missing (NaN) values",
            "Drops all numerical columns from the DataFrame",
            "Sorts the DataFrame by missing value count"
        ],
        "answer": "Removes rows or columns containing missing (NaN) values",
        "category": "Python & Programming",
        "difficulty": "Easy",
        "explanation": "dropna() removes rows (default) or columns (axis=1) that contain any NaN values. Parameters include how='all' (drop only if all values are NaN) and subset=[cols] (check specific columns only). Always inspect data before dropping to avoid unintended data loss."
    },
    {
        "question": "What is NumPy primarily used for in data science?",
        "options": [
            "Creating interactive data visualizations",
            "Efficient numerical computing with multi-dimensional arrays and mathematical operations",
            "Connecting to SQL databases",
            "Building and training neural networks"
        ],
        "answer": "Efficient numerical computing with multi-dimensional arrays and mathematical operations",
        "category": "Python & Programming",
        "difficulty": "Easy",
        "explanation": "NumPy provides the ndarray — a fast, memory-efficient array for numerical computation. Vectorized operations on NumPy arrays replace slow Python loops, and NumPy is the foundation underlying pandas, scikit-learn, PyTorch, and TensorFlow."
    },
    {
        "question": "What is the purpose of train_test_split in scikit-learn?",
        "options": [
            "To normalize features to zero mean and unit variance",
            "To randomly split arrays into training and test subsets",
            "To perform k-fold cross-validation",
            "To encode categorical variables as integers"
        ],
        "answer": "To randomly split arrays into training and test subsets",
        "category": "Python & Programming",
        "difficulty": "Easy",
        "explanation": "train_test_split(X, y, test_size=0.2, random_state=42) randomly partitions data into training and test sets. The random_state ensures reproducibility. Setting stratify=y maintains class proportions in both splits — important for imbalanced datasets."
    },
    {
        "question": "What is the purpose of the @staticmethod decorator in Python?",
        "options": [
            "To make a method that automatically saves its state between calls",
            "To define a method that belongs to the class but does not receive the instance or class as its first argument",
            "To mark a method as immutable and prevent overriding",
            "To cache the result of a method call for performance"
        ],
        "answer": "To define a method that belongs to the class but does not receive the instance or class as its first argument",
        "category": "Python & Programming",
        "difficulty": "Medium",
        "explanation": "@staticmethod defines a method that behaves like a regular function but lives in the class namespace. It receives no implicit first argument (no self or cls), so it cannot access instance or class state. Useful for utility functions logically grouped within a class."
    },
    {
        "question": "What does vectorization mean in the context of NumPy/pandas?",
        "options": [
            "Converting text to numerical embeddings",
            "Replacing explicit Python loops with array operations that execute in compiled C code",
            "Normalizing vectors to unit length",
            "Encoding categorical features as one-hot vectors"
        ],
        "answer": "Replacing explicit Python loops with array operations that execute in compiled C code",
        "category": "Python & Programming",
        "difficulty": "Medium",
        "explanation": "Vectorization applies operations across entire arrays using optimized C/Fortran code instead of Python loops. This can yield 10-100x speedups because Python interpreter overhead is eliminated and CPU SIMD instructions are leveraged. It is fundamental to efficient data science in Python."
    },
    {
        "question": "What is a Python generator and how does it differ from a list?",
        "options": [
            "A generator stores all values in memory at once; a list generates values lazily",
            "A generator yields values one at a time on demand (lazy evaluation); a list stores all values in memory",
            "Generators are only used for infinite sequences; lists are for finite sequences",
            "They are functionally identical but generators use less syntax"
        ],
        "answer": "A generator yields values one at a time on demand (lazy evaluation); a list stores all values in memory",
        "category": "Python & Programming",
        "difficulty": "Medium",
        "explanation": "Generators use the yield keyword to produce values lazily — only computing the next value when requested. This makes them memory-efficient for large data streams (e.g., reading large files line by line). A list comprehension creates all values immediately, consuming memory proportional to size."
    },
    {
        "question": "What is the GIL (Global Interpreter Lock) in CPython and how does it affect data science workloads?",
        "options": [
            "A memory management system that prevents NumPy arrays from being freed prematurely",
            "A mutex that prevents multiple threads from executing Python bytecode simultaneously, limiting CPU-bound multi-threading",
            "A compiler optimization that speeds up numerical loops automatically",
            "A security feature that prevents unauthorized access to Python internals"
        ],
        "answer": "A mutex that prevents multiple threads from executing Python bytecode simultaneously, limiting CPU-bound multi-threading",
        "category": "Python & Programming",
        "difficulty": "Hard",
        "explanation": "The GIL ensures only one thread executes Python bytecode at a time, making CPU-bound multi-threading ineffective in CPython. However, NumPy, pandas, and PyTorch release the GIL during C extension calls, so numerical operations can benefit. The multiprocessing module bypasses the GIL entirely for CPU-bound tasks."
    },
    {
        "question": "What is the difference between __repr__ and __str__ in Python?",
        "options": [
            "They are identical; Python uses them interchangeably",
            "__repr__ returns an unambiguous developer-facing representation; __str__ returns a human-readable display string",
            "__str__ is for numbers; __repr__ is for strings",
            "__repr__ is called when printing; __str__ is called when converting to bytes"
        ],
        "answer": "__repr__ returns an unambiguous developer-facing representation; __str__ returns a human-readable display string",
        "category": "Python & Programming",
        "difficulty": "Hard",
        "explanation": "__repr__ should return a string that, ideally, could recreate the object (eval(repr(obj)) == obj). __str__ is for end-user display. When only __repr__ is defined, Python falls back to it for both. In interactive environments, repr() is shown; print() uses str()."
    },
    {
        "question": "Which Python data type is mutable?",
        "options": [
            "tuple",
            "str",
            "list",
            "frozenset"
        ],
        "answer": "list",
        "category": "Python & Programming",
        "difficulty": "Easy",
        "explanation": "Lists are mutable — you can add, remove, or change elements after creation. Tuples, strings, and frozensets are immutable; once created, their contents cannot be changed. Mutability matters for using objects as dictionary keys (only immutable/hashable types are allowed)."
    },
    {
        "question": "What does the zip() function do in Python?",
        "options": [
            "Compresses a file into a .zip archive",
            "Combines two or more iterables element-wise into tuples",
            "Sorts two lists simultaneously",
            "Flattens a nested list into a single list"
        ],
        "answer": "Combines two or more iterables element-wise into tuples",
        "category": "Python & Programming",
        "difficulty": "Easy",
        "explanation": "zip(a, b) returns an iterator of tuples, pairing elements by index: (a[0],b[0]), (a[1],b[1]), etc. It stops at the shortest iterable. Commonly used to iterate over multiple lists together. zip(*zipped) is the inverse, unzipping pairs back into separate sequences."
    },
    {
        "question": "What is the output of bool([]) in Python?",
        "options": [
            "True",
            "False",
            "None",
            "Raises a TypeError"
        ],
        "answer": "False",
        "category": "Python & Programming",
        "difficulty": "Easy",
        "explanation": "Empty containers ([], {}, (), set(), '') are falsy in Python. bool([]) returns False because an empty list has no elements. This allows concise checks like 'if my_list:' instead of 'if len(my_list) > 0:'. Non-empty containers are truthy."
    },
    {
        "question": "What is the purpose of the 'with' statement in Python?",
        "options": [
            "To import modules conditionally",
            "To manage resources by ensuring setup and teardown code runs via context managers",
            "To define a new scope for variable declarations",
            "To catch multiple exceptions in a single block"
        ],
        "answer": "To manage resources by ensuring setup and teardown code runs via context managers",
        "category": "Python & Programming",
        "difficulty": "Easy",
        "explanation": "The 'with' statement invokes a context manager's __enter__ on entry and __exit__ on exit (even if an exception occurs). Classic use cases include file I/O (auto-close), database connections, and thread locks. It eliminates the need for explicit try/finally teardown boilerplate."
    },
    {
        "question": "How do you create a virtual environment in Python 3?",
        "options": [
            "pip install virtualenv && virtualenv env",
            "python3 -m venv env",
            "conda new env",
            "python3 --create-env env"
        ],
        "answer": "python3 -m venv env",
        "category": "Python & Programming",
        "difficulty": "Easy",
        "explanation": "The built-in venv module (python3 -m venv env) creates an isolated Python environment. Activate it with 'source env/bin/activate' on Unix or 'env\\Scripts\\activate' on Windows. Virtual environments keep project dependencies isolated to prevent version conflicts."
    },
    {
        "question": "What does the enumerate() function return?",
        "options": [
            "A sorted list of (index, value) tuples",
            "An iterator of (index, value) pairs for each element of the iterable",
            "A dictionary mapping indices to values",
            "The total count of elements in an iterable"
        ],
        "answer": "An iterator of (index, value) pairs for each element of the iterable",
        "category": "Python & Programming",
        "difficulty": "Easy",
        "explanation": "enumerate(iterable, start=0) yields (index, item) tuples, allowing you to loop with an automatic counter. For example, 'for i, val in enumerate(mylist):' avoids manually tracking an index variable. The start parameter lets you begin counting from any integer."
    },
    {
        "question": "What is a list comprehension in Python?",
        "options": [
            "A method for sorting lists using a custom comparator",
            "A concise syntax to create lists by applying an expression to each item of an iterable, optionally filtered",
            "A technique for flattening multi-dimensional lists",
            "A way to define read-only lists"
        ],
        "answer": "A concise syntax to create lists by applying an expression to each item of an iterable, optionally filtered",
        "category": "Python & Programming",
        "difficulty": "Easy",
        "explanation": "List comprehensions use the syntax [expr for item in iterable if condition]. Example: [x**2 for x in range(10) if x % 2 == 0] generates squares of even numbers. They are generally faster and more readable than equivalent for-loop constructions and are idiomatic Python."
    },
    {
        "question": "What is the difference between 'is' and '==' in Python?",
        "options": [
            "'is' checks value equality; '==' checks identity",
            "'is' checks object identity (same memory location); '==' checks value equality",
            "They are interchangeable for all data types",
            "'is' is only valid for comparing None; '==' works for everything"
        ],
        "answer": "'is' checks object identity (same memory location); '==' checks value equality",
        "category": "Python & Programming",
        "difficulty": "Easy",
        "explanation": "'is' returns True only if two variables point to the exact same object in memory (same id()). '==' calls __eq__ to compare values. Small integers and interned strings may appear the same with 'is' due to caching, but this is an implementation detail. Always use '==' for value comparisons and 'is' for None/True/False checks."
    },
    {
        "question": "What does *args do in a Python function definition?",
        "options": [
            "It unpacks a dictionary into keyword arguments",
            "It collects extra positional arguments into a tuple",
            "It makes all arguments optional with default values",
            "It forces all arguments to be passed as keywords"
        ],
        "answer": "It collects extra positional arguments into a tuple",
        "category": "Python & Programming",
        "difficulty": "Easy",
        "explanation": "def func(*args) collects any number of positional arguments into a tuple called args. This allows functions to accept variable-length input. Similarly, **kwargs collects keyword arguments into a dict. Both are commonly combined: def func(*args, **kwargs) creates a fully flexible signature."
    },
    {
        "question": "What does pandas.read_csv() return by default?",
        "options": [
            "A Python list of dictionaries",
            "A pandas DataFrame",
            "A NumPy 2D array",
            "A pandas Series"
        ],
        "answer": "A pandas DataFrame",
        "category": "Python & Programming",
        "difficulty": "Easy",
        "explanation": "pd.read_csv(filepath) parses a CSV file and returns a DataFrame — a 2D labeled data structure with columns of potentially different types. Key parameters include sep, header, index_col, dtype, and parse_dates. For very large files, use chunksize to read iteratively."
    },
    {
        "question": "What is the purpose of requirements.txt in a Python project?",
        "options": [
            "To define the project's main entry point",
            "To list external package dependencies and their versions for reproducible installs",
            "To configure linting and code style rules",
            "To specify the Python version to use"
        ],
        "answer": "To list external package dependencies and their versions for reproducible installs",
        "category": "Python & Programming",
        "difficulty": "Easy",
        "explanation": "requirements.txt lists packages (and optionally pinned versions) needed to run a project. Running 'pip install -r requirements.txt' installs them all at once. Best practice pins exact versions (e.g., numpy==1.26.0) to ensure reproducibility across environments."
    },
    {
        "question": "What does the .shape attribute of a NumPy array return?",
        "options": [
            "The total number of elements",
            "A tuple representing the size of each dimension",
            "The data type of the array elements",
            "The number of dimensions only"
        ],
        "answer": "A tuple representing the size of each dimension",
        "category": "Python & Programming",
        "difficulty": "Easy",
        "explanation": "arr.shape returns a tuple like (rows, cols) for 2D arrays or (depth, rows, cols) for 3D. For a DataFrame loaded from 1000-row, 5-column CSV, df.values.shape is (1000, 5). It is used constantly to verify array dimensions before operations."
    },
    {
        "question": "What is the difference between a shallow copy and a deep copy in Python?",
        "options": [
            "A shallow copy duplicates only the first level; nested objects are still shared. A deep copy recursively duplicates all nested objects.",
            "A shallow copy is faster but larger in memory; a deep copy is slower and smaller",
            "They produce identical results for all data types",
            "A shallow copy uses copy.deepcopy(); a deep copy uses the slice operator [:]"
        ],
        "answer": "A shallow copy duplicates only the first level; nested objects are still shared. A deep copy recursively duplicates all nested objects.",
        "category": "Python & Programming",
        "difficulty": "Medium",
        "explanation": "copy.copy() creates a shallow copy: the outer container is new, but nested objects (e.g., inner lists) still reference the same memory. copy.deepcopy() recursively copies everything. Modifying a nested object in a shallow copy also affects the original, which is a common source of bugs."
    },
    {
        "question": "What is monkey patching in Python?",
        "options": [
            "A technique for optimizing loops using Cython",
            "Dynamically replacing or adding attributes and methods to a class or module at runtime",
            "A design pattern for implementing the observer pattern",
            "A method for patching security vulnerabilities in Python packages"
        ],
        "answer": "Dynamically replacing or adding attributes and methods to a class or module at runtime",
        "category": "Python & Programming",
        "difficulty": "Medium",
        "explanation": "Monkey patching modifies classes or modules at runtime without changing source code. Common in testing (e.g., unittest.mock.patch replaces methods with mocks). While powerful, it can cause hard-to-debug issues due to non-obvious side effects, so it should be used sparingly."
    },
    {
        "question": "What is the purpose of __slots__ in a Python class?",
        "options": [
            "To define abstract methods that subclasses must implement",
            "To restrict instance attributes to a fixed set, reducing memory overhead per instance",
            "To make all attributes of a class read-only",
            "To enable multiple inheritance without method resolution conflicts"
        ],
        "answer": "To restrict instance attributes to a fixed set, reducing memory overhead per instance",
        "category": "Python & Programming",
        "difficulty": "Medium",
        "explanation": "__slots__ = ['x', 'y'] prevents the creation of a per-instance __dict__, reducing memory by 40-60% for classes with many instances. Only listed attributes are allowed; assigning others raises AttributeError. Useful for large-scale data structures where millions of objects are created."
    },
    {
        "question": "What does the @property decorator do in Python?",
        "options": [
            "Marks a method as a class-level attribute",
            "Allows a method to be accessed like an attribute, enabling controlled getter/setter logic",
            "Prevents a method from being overridden in subclasses",
            "Caches the return value of a method for repeated calls"
        ],
        "answer": "Allows a method to be accessed like an attribute, enabling controlled getter/setter logic",
        "category": "Python & Programming",
        "difficulty": "Medium",
        "explanation": "@property turns a method into a read-only attribute. Pairing it with @attr.setter and @attr.deleter gives full getter/setter/deleter control without breaking the calling interface. This follows encapsulation best practices — callers use obj.temperature instead of obj.get_temperature()."
    },
    {
        "question": "What is the difference between .loc[] and .iloc[] in pandas?",
        "options": [
            ".loc[] uses integer-based positional indexing; .iloc[] uses label-based indexing",
            ".loc[] uses label-based indexing (row/column names); .iloc[] uses integer-based positional indexing",
            "They are aliases; both index by label",
            ".loc[] is for single-row access; .iloc[] is for multi-row slicing"
        ],
        "answer": ".loc[] uses label-based indexing (row/column names); .iloc[] uses integer-based positional indexing",
        "category": "Python & Programming",
        "difficulty": "Medium",
        "explanation": "df.loc['2023-01', 'sales'] selects by index/column labels. df.iloc[0, 2] selects by row and column position (0-indexed). Mixing them up is a common bug — especially when the DataFrame index is integers, where loc and iloc can differ after filtering and resetting the index."
    },
    {
        "question": "What is a lambda function in Python?",
        "options": [
            "A function defined inside another function to capture its enclosing scope",
            "An anonymous, single-expression function defined with the lambda keyword",
            "A function that runs asynchronously in a separate thread",
            "A built-in function that applies another function to a sequence"
        ],
        "answer": "An anonymous, single-expression function defined with the lambda keyword",
        "category": "Python & Programming",
        "difficulty": "Medium",
        "explanation": "lambda args: expression creates a small anonymous function inline. Example: sorted(data, key=lambda x: x['age']) sorts by the 'age' key. Lambdas are limited to a single expression (no statements). For complex logic, a named def function is clearer and more testable."
    },
    {
        "question": "What does the pandas groupby() method do?",
        "options": [
            "Sorts a DataFrame by one or more column values",
            "Splits a DataFrame into groups based on values of one or more columns, enabling aggregation per group",
            "Merges two DataFrames on a common key column",
            "Filters rows based on a boolean condition"
        ],
        "answer": "Splits a DataFrame into groups based on values of one or more columns, enabling aggregation per group",
        "category": "Python & Programming",
        "difficulty": "Medium",
        "explanation": "df.groupby('category')['sales'].sum() splits the DataFrame by unique 'category' values, then sums 'sales' within each group. The split-apply-combine pattern is fundamental to data aggregation. Common aggregation methods: sum, mean, count, min, max, agg (for custom functions)."
    },
    {
        "question": "What is the purpose of the __init__.py file in a Python package?",
        "options": [
            "To store configuration variables for the package",
            "To mark a directory as a Python package and optionally execute initialization code on import",
            "To list all public classes and functions exported by the package",
            "To define the entry point when running the package as a script"
        ],
        "answer": "To mark a directory as a Python package and optionally execute initialization code on import",
        "category": "Python & Programming",
        "difficulty": "Medium",
        "explanation": "__init__.py makes a directory importable as a package. It can be empty or contain initialization logic, __all__ definitions, or convenience imports. In Python 3.3+, namespace packages work without __init__.py, but explicit packages still use it for control over the public API."
    },
    {
        "question": "How does Python's garbage collector handle reference cycles?",
        "options": [
            "It relies purely on reference counting, which cannot detect cycles",
            "It uses a cyclic garbage collector that periodically detects and collects objects in reference cycles",
            "It immediately frees cyclic references when the program exits",
            "Cycles are prevented at the language level; Python does not allow them"
        ],
        "answer": "It uses a cyclic garbage collector that periodically detects and collects objects in reference cycles",
        "category": "Python & Programming",
        "difficulty": "Medium",
        "explanation": "CPython uses reference counting as the primary memory management strategy, but this cannot collect cycles (e.g., A → B → A). The supplementary cyclic GC (gc module) periodically runs a generational collector to find and free unreachable cycles. You can trigger it manually with gc.collect()."
    },
    {
        "question": "What is broadcasting in NumPy?",
        "options": [
            "Sending array data over a network connection",
            "A set of rules that allow arithmetic operations between arrays of different but compatible shapes without explicit loops",
            "Converting a 1D array into a 2D matrix automatically",
            "Duplicating an array across multiple CPU cores for parallel processing"
        ],
        "answer": "A set of rules that allow arithmetic operations between arrays of different but compatible shapes without explicit loops",
        "category": "Python & Programming",
        "difficulty": "Medium",
        "explanation": "Broadcasting lets NumPy operate on arrays with different shapes by virtually stretching the smaller array. For example, adding a (3,1) array to a (1,4) array produces a (3,4) result without copying memory. The rules check dimension compatibility from the trailing axis: dimensions must be equal or one of them must be 1."
    },
    {
        "question": "What is the difference between map() and a list comprehension?",
        "options": [
            "map() modifies the original list in-place; list comprehensions create a new list",
            "map() applies a function lazily and returns an iterator; a list comprehension eagerly creates a full list",
            "They are identical in output and performance",
            "map() supports filtering; list comprehensions only support transformation"
        ],
        "answer": "map() applies a function lazily and returns an iterator; a list comprehension eagerly creates a full list",
        "category": "Python & Programming",
        "difficulty": "Medium",
        "explanation": "map(func, iterable) returns a lazy iterator — values are computed on demand. List comprehensions evaluate immediately and store all results. In Python 3, wrapping map() in list() forces evaluation. List comprehensions are generally more readable and Pythonic; map() can be marginally faster with a built-in function."
    },
    {
        "question": "What does the pandas merge() function do, and how does it differ from concat()?",
        "options": [
            "merge() stacks DataFrames vertically; concat() joins them on a key column",
            "merge() performs SQL-style joins on key columns; concat() stacks DataFrames along an axis",
            "They are identical; both perform left joins by default",
            "merge() is for numerical data; concat() is for string data"
        ],
        "answer": "merge() performs SQL-style joins on key columns; concat() stacks DataFrames along an axis",
        "category": "Python & Programming",
        "difficulty": "Medium",
        "explanation": "pd.merge(left, right, on='id', how='inner') joins two DataFrames on a shared key, similar to SQL JOIN. pd.concat([df1, df2], axis=0) stacks DataFrames row-wise (axis=0) or column-wise (axis=1) without matching on keys. Use merge for relational joins, concat for simple stacking."
    },
    {
        "question": "What is a decorator in Python?",
        "options": [
            "A built-in class for creating styled terminal output",
            "A function that wraps another function to extend or modify its behavior without changing its source code",
            "A type hint annotation indicating a function's return type",
            "A class method that initializes instance attributes"
        ],
        "answer": "A function that wraps another function to extend or modify its behavior without changing its source code",
        "category": "Python & Programming",
        "difficulty": "Medium",
        "explanation": "Decorators use the @syntax as syntactic sugar for func = decorator(func). Common uses include logging, authentication, caching (@functools.lru_cache), and timing. A well-written decorator uses functools.wraps to preserve the original function's __name__ and __doc__."
    },
    {
        "question": "What is the difference between a set and a frozenset in Python?",
        "options": [
            "A set is ordered; a frozenset is unordered",
            "A set is mutable and unhashable; a frozenset is immutable and hashable",
            "frozenset supports union and intersection; set does not",
            "They are identical; frozenset is just an alias for set"
        ],
        "answer": "A set is mutable and unhashable; a frozenset is immutable and hashable",
        "category": "Python & Programming",
        "difficulty": "Medium",
        "explanation": "Sets are mutable (add, remove, discard) but cannot be used as dictionary keys or elements of other sets because they are unhashable. Frozensets are immutable and hashable, so they can serve as dict keys or set elements. Both support union, intersection, difference, and membership testing in O(1)."
    },
    {
        "question": "What is the purpose of assert statements in Python?",
        "options": [
            "To raise custom exceptions with a specific message",
            "To test a condition during development; raises AssertionError if the condition is False",
            "To enforce type checking at runtime for function arguments",
            "To halt program execution and enter the debugger"
        ],
        "answer": "To test a condition during development; raises AssertionError if the condition is False",
        "category": "Python & Programming",
        "difficulty": "Medium",
        "explanation": "assert condition, 'message' is a debugging aid — it verifies assumptions in code. If the condition is False, AssertionError is raised with the optional message. Critically, assertions are disabled when Python is run with the -O (optimize) flag, so they should never be used for data validation in production code."
    },
    {
        "question": "What does itertools.chain() do?",
        "options": [
            "Applies a function cumulatively across an iterable (like reduce)",
            "Chains multiple iterables together into a single continuous iterator",
            "Creates an iterator that cycles through an iterable indefinitely",
            "Returns pairs of consecutive elements from an iterable"
        ],
        "answer": "Chains multiple iterables together into a single continuous iterator",
        "category": "Python & Programming",
        "difficulty": "Medium",
        "explanation": "itertools.chain(iter1, iter2, ...) yields elements from the first iterable, then seamlessly continues with the next, without building an intermediate list. Useful for processing multiple files or batches as a single stream. chain.from_iterable() handles a single iterable of iterables."
    },
    {
        "question": "What is method resolution order (MRO) in Python?",
        "options": [
            "The sequence in which Python searches for a method when called on an instance",
            "The order in which methods are defined within a class body",
            "The priority given to built-in methods over user-defined ones",
            "A performance ranking of methods based on call frequency"
        ],
        "answer": "The sequence in which Python searches for a method when called on an instance",
        "category": "Python & Programming",
        "difficulty": "Medium",
        "explanation": "MRO defines the lookup path for attribute and method resolution in inheritance hierarchies. Python uses the C3 linearization algorithm. You can inspect it with ClassName.__mro__ or ClassName.mro(). Understanding MRO is essential for multiple inheritance to avoid the diamond problem."
    },
    {
        "question": "What is the purpose of functools.lru_cache?",
        "options": [
            "To limit the rate at which a function can be called",
            "To memoize a function's results, caching recent return values to avoid redundant computation",
            "To run a function in a separate thread for non-blocking execution",
            "To log function calls and their arguments automatically"
        ],
        "answer": "To memoize a function's results, caching recent return values to avoid redundant computation",
        "category": "Python & Programming",
        "difficulty": "Medium",
        "explanation": "@functools.lru_cache(maxsize=128) stores the most recently used call results. When the function is called with the same arguments, the cached value is returned immediately. This is ideal for pure functions with expensive computation (e.g., recursive algorithms). maxsize=None (or @cache in Python 3.9+) stores all results indefinitely."
    },
    {
        "question": "What is the difference between positional and keyword arguments in Python functions?",
        "options": [
            "Positional arguments must always come before keyword arguments in the function signature",
            "Positional arguments are matched by order; keyword arguments are matched by name and can appear in any order",
            "Keyword arguments are faster to evaluate than positional ones",
            "Positional arguments are required; keyword arguments always have default values"
        ],
        "answer": "Positional arguments are matched by order; keyword arguments are matched by name and can appear in any order",
        "category": "Python & Programming",
        "difficulty": "Easy",
        "explanation": "func(1, 2) passes values positionally. func(b=2, a=1) passes by name, allowing any order. Python 3 allows enforcing keyword-only arguments after * in the signature: def func(a, *, b). This improves readability for functions with many optional parameters."
    },
    {
        "question": "What does the pandas DataFrame.fillna() method do?",
        "options": [
            "Drops all rows with missing values",
            "Replaces NaN values with a specified value or strategy",
            "Fills a DataFrame with random numbers",
            "Marks NaN positions with a boolean True flag"
        ],
        "answer": "Replaces NaN values with a specified value or strategy",
        "category": "Python & Programming",
        "difficulty": "Easy",
        "explanation": "fillna(value) replaces all NaN entries with a constant. Strategies include method='ffill' (forward fill from previous valid value) and method='bfill' (backward fill). You can also pass a dict to fill different columns with different values. Always consider the impact on downstream analysis before imputing."
    },
    {
        "question": "What is pickling in Python?",
        "options": [
            "Compressing data using the zlib algorithm",
            "Serializing Python objects to a byte stream for storage or transmission",
            "Encrypting sensitive data before writing to disk",
            "Converting Python objects to JSON format"
        ],
        "answer": "Serializing Python objects to a byte stream for storage or transmission",
        "category": "Python & Programming",
        "difficulty": "Easy",
        "explanation": "The pickle module serializes (pickle.dump) and deserializes (pickle.load) almost any Python object. It is used to save trained scikit-learn models, cache intermediate results, and pass objects between processes. Warning: never unpickle data from untrusted sources — it can execute arbitrary code."
    },
    {
        "question": "What does the sorted() function return in Python?",
        "options": [
            "The original list modified in-place",
            "A new sorted list, leaving the original unchanged",
            "A sorted iterator that evaluates lazily",
            "A sorted dictionary ordered by key"
        ],
        "answer": "A new sorted list, leaving the original unchanged",
        "category": "Python & Programming",
        "difficulty": "Easy",
        "explanation": "sorted(iterable) always returns a new list. In contrast, list.sort() sorts in-place and returns None. sorted() works on any iterable (tuples, sets, dicts) and accepts key= and reverse= parameters. The underlying algorithm is Timsort — stable and O(n log n) in the worst case."
    },
    {
        "question": "What does the any() function do in Python?",
        "options": [
            "Returns True if all elements of the iterable are truthy",
            "Returns True if at least one element of the iterable is truthy",
            "Returns the first truthy element found, or None",
            "Checks whether any two elements in the iterable are equal"
        ],
        "answer": "Returns True if at least one element of the iterable is truthy",
        "category": "Python & Programming",
        "difficulty": "Easy",
        "explanation": "any(iterable) short-circuits and returns True as soon as it finds a truthy value. any([False, 0, '', 5]) returns True because 5 is truthy. Its complement, all(), returns True only if every element is truthy. Both are useful alternatives to explicit for-loops with conditional checks."
    },
    {
        "question": "What is a Python dictionary comprehension?",
        "options": [
            "A way to iterate over dictionary keys only",
            "A concise syntax to create dictionaries using {key: value for item in iterable} expressions",
            "A built-in method to merge two dictionaries",
            "A generator that yields key-value pairs one at a time"
        ],
        "answer": "A concise syntax to create dictionaries using {key: value for item in iterable} expressions",
        "category": "Python & Programming",
        "difficulty": "Easy",
        "explanation": "Dict comprehensions follow the form {k: v for k, v in items}. Example: {word: len(word) for word in words} maps each word to its length. They are more readable and often faster than constructing a dict with a loop and dict[key] = value assignments."
    },
    {
        "question": "What does the NumPy function np.concatenate() do?",
        "options": [
            "Multiplies arrays element-wise along a specified axis",
            "Joins a sequence of arrays along an existing axis",
            "Creates a new array filled with zeros",
            "Reshapes arrays to make their shapes compatible"
        ],
        "answer": "Joins a sequence of arrays along an existing axis",
        "category": "Python & Programming",
        "difficulty": "Easy",
        "explanation": "np.concatenate([a, b], axis=0) joins arrays along an existing axis. All arrays must have the same shape except in the concatenation dimension. np.stack() differs by creating a new axis. np.hstack and np.vstack are convenience wrappers for horizontal and vertical stacking respectively."
    },
    {
        "question": "What is a context manager in Python and how do you create a custom one?",
        "options": [
            "A manager class that handles concurrent thread access to shared resources",
            "An object that implements __enter__ and __exit__ methods, or a generator decorated with @contextlib.contextmanager",
            "A pattern for managing Python module imports in large projects",
            "A configuration object that controls interpreter settings at runtime"
        ],
        "answer": "An object that implements __enter__ and __exit__ methods, or a generator decorated with @contextlib.contextmanager",
        "category": "Python & Programming",
        "difficulty": "Medium",
        "explanation": "A custom context manager can be built as a class with __enter__ (setup, returns resource) and __exit__ (teardown, receives exception info). Alternatively, @contextlib.contextmanager turns a generator with a single yield into a context manager — simpler for one-off cases. Used to ensure resource cleanup even during exceptions."
    },
    {
        "question": "What is the purpose of the collections.defaultdict?",
        "options": [
            "A dict subclass that sorts keys automatically on insertion",
            "A dict subclass that returns a default value for missing keys instead of raising KeyError",
            "A dict that limits its size and evicts the least recently used item",
            "A thread-safe dictionary implementation for concurrent access"
        ],
        "answer": "A dict subclass that returns a default value for missing keys instead of raising KeyError",
        "category": "Python & Programming",
        "difficulty": "Medium",
        "explanation": "defaultdict(list) automatically creates an empty list for any missing key on access, eliminating the need for if key not in dict checks. Common use cases: grouping items (defaultdict(list)), counting (defaultdict(int)), and building graphs (defaultdict(set)). The argument is a callable that produces the default value."
    },
    {
        "question": "What is the difference between multiprocessing and threading in Python?",
        "options": [
            "Threading uses multiple CPU cores; multiprocessing shares a single core with time-slicing",
            "Multiprocessing creates separate processes with independent memory; threading creates threads sharing the same memory and GIL",
            "They are interchangeable; both bypass the GIL equally",
            "Multiprocessing is only available on Linux; threading works on all platforms"
        ],
        "answer": "Multiprocessing creates separate processes with independent memory; threading creates threads sharing the same memory and GIL",
        "category": "Python & Programming",
        "difficulty": "Medium",
        "explanation": "The multiprocessing module spawns separate Python interpreters with independent memory spaces, bypassing the GIL — ideal for CPU-bound tasks. The threading module creates lightweight threads in the same process, sharing memory — suited for I/O-bound tasks. Inter-process communication in multiprocessing uses Queue or Pipe."
    },
    {
        "question": "What is a named tuple in Python and when would you use it?",
        "options": [
            "A dictionary subclass that remembers insertion order",
            "A tuple subclass with named fields, enabling attribute-style access alongside index access",
            "A class that enforces attribute names but allows mutation",
            "An ordered dictionary with a fixed schema"
        ],
        "answer": "A tuple subclass with named fields, enabling attribute-style access alongside index access",
        "category": "Python & Programming",
        "difficulty": "Medium",
        "explanation": "collections.namedtuple('Point', ['x', 'y']) creates a class whose instances behave like tuples but allow p.x instead of p[0]. They are immutable, memory-efficient, and self-documenting. Python 3.6+ dataclasses offer a more flexible alternative when mutability or default values are needed."
    },
    {
        "question": "What is the difference between os.path.join() and string concatenation for building file paths?",
        "options": [
            "They produce identical results on all operating systems",
            "os.path.join() uses the correct OS path separator and handles edge cases; string concatenation is brittle and platform-dependent",
            "String concatenation is preferred for performance-critical code",
            "os.path.join() only works with absolute paths"
        ],
        "answer": "os.path.join() uses the correct OS path separator and handles edge cases; string concatenation is brittle and platform-dependent",
        "category": "Python & Programming",
        "difficulty": "Medium",
        "explanation": "os.path.join('data', 'file.csv') uses '\\' on Windows and '/' on Unix automatically. It also handles edge cases like double slashes and absolute path components. Python 3.4+ pathlib.Path offers an object-oriented alternative: Path('data') / 'file.csv' is idiomatic modern Python."
    },
    {
        "question": "What is the walrus operator (:=) introduced in Python 3.8?",
        "options": [
            "A new syntax for dictionary unpacking",
            "An assignment expression that assigns and returns a value within a larger expression",
            "A shorthand for the ternary conditional operator",
            "A new way to define default argument values in functions"
        ],
        "answer": "An assignment expression that assigns and returns a value within a larger expression",
        "category": "Python & Programming",
        "difficulty": "Medium",
        "explanation": "The walrus operator (:=) assigns a value and simultaneously returns it, enabling patterns like 'while chunk := file.read(8192):' or 'if (n := len(a)) > 10:'. It reduces redundant computations in loops and comprehensions. Use it judiciously — overuse reduces readability."
    },
    {
        "question": "What is a Python dataclass and what does @dataclass provide automatically?",
        "options": [
            "A class that stores data in a SQL database automatically",
            "A decorator that auto-generates __init__, __repr__, and __eq__ based on class-level field annotations",
            "A class restricted to storing only primitive data types",
            "A frozen dictionary that enforces a schema"
        ],
        "answer": "A decorator that auto-generates __init__, __repr__, and __eq__ based on class-level field annotations",
        "category": "Python & Programming",
        "difficulty": "Medium",
        "explanation": "@dataclass (Python 3.7+) auto-generates boilerplate: __init__ from annotated fields, __repr__ for printing, and __eq__ for value comparison. Use frozen=True to make instances immutable and hashable. order=True generates comparison methods. Dataclasses strike a balance between namedtuple simplicity and full class flexibility."
    },
    {
        "question": "What does the itertools.product() function compute?",
        "options": [
            "The element-wise product of two numeric iterables",
            "The Cartesian product of input iterables, equivalent to nested for-loops",
            "The cumulative product of elements in a single iterable",
            "The dot product of two vectors"
        ],
        "answer": "The Cartesian product of input iterables, equivalent to nested for-loops",
        "category": "Python & Programming",
        "difficulty": "Medium",
        "explanation": "itertools.product([1,2], ['a','b']) yields (1,'a'), (1,'b'), (2,'a'), (2,'b') — every combination. It is equivalent to nested for-loops but more memory-efficient since it yields lazily. The repeat argument allows repeated Cartesian powers: product('AB', repeat=2) gives all 2-character strings from {A,B}."
    },
    {
        "question": "How does Python's __new__ differ from __init__?",
        "options": [
            "They are identical; Python calls them at the same time",
            "__new__ creates and returns the instance; __init__ initializes it after creation",
            "__init__ creates the object; __new__ assigns attributes to it",
            "__new__ is called for class creation; __init__ is called for instance creation"
        ],
        "answer": "__new__ creates and returns the instance; __init__ initializes it after creation",
        "category": "Python & Programming",
        "difficulty": "Hard",
        "explanation": "__new__(cls) is called first and must return an instance (usually via super().__new__(cls)). Only then is __init__(self) called to initialize it. Overriding __new__ is needed for immutable types (like tuple subclasses) or implementing the Singleton pattern, since __init__ cannot change the object's value after creation."
    },
    {
        "question": "What is the purpose of Python's abc module?",
        "options": [
            "To provide a simplified interface for asynchronous byte communication",
            "To define abstract base classes that enforce a common interface on subclasses",
            "To measure algorithm complexity with big-O notation helpers",
            "To perform abstract syntax tree manipulation"
        ],
        "answer": "To define abstract base classes that enforce a interface on subclasses",
        "category": "Python & Programming",
        "difficulty": "Hard",
        "explanation": "The abc module provides ABC and @abstractmethod. A class inheriting from ABC with abstractmethod-decorated methods cannot be instantiated directly. Subclasses must implement all abstract methods or they also become abstract. This enforces interface contracts in Python's duck-typing system."
    },
    {
        "question": "What is a metaclass in Python?",
        "options": [
            "A base class automatically inherited by all user-defined classes",
            "A class whose instances are themselves classes; it controls class creation",
            "A class designed specifically to hold class-level metadata attributes",
            "A decorator that transforms a function into a class"
        ],
        "answer": "A class whose instances are themselves classes; it controls class creation",
        "category": "Python & Programming",
        "difficulty": "Hard",
        "explanation": "In Python, 'type' is the default metaclass — it creates all classes. Custom metaclasses (class Meta(type)) override __new__ or __init__ to modify class creation: adding methods, enforcing naming conventions, or registering subclasses automatically. Metaclasses power frameworks like Django ORM and SQLAlchemy."
    },
    {
        "question": "What is the difference between __getattr__ and __getattribute__ in Python?",
        "options": [
            "They are identical; Python calls them interchangeably",
            "__getattr__ is only called when normal attribute lookup fails; __getattribute__ is called for every attribute access",
            "__getattribute__ is called for missing attributes; __getattr__ is called for all attribute access",
            "__getattr__ is for class attributes; __getattribute__ is for instance attributes"
        ],
        "answer": "__getattr__ is only called when normal attribute lookup fails; __getattribute__ is called for every attribute access",
        "category": "Python & Programming",
        "difficulty": "Hard",
        "explanation": "__getattribute__ intercepts every attribute access (including existing ones), so overriding it carelessly causes infinite recursion — always call super().__getattribute__. __getattr__ is only invoked as a fallback when the normal mechanism raises AttributeError. Use __getattr__ for dynamic/lazy attributes; __getattribute__ for complete access control."
    },
    {
        "question": "What is the purpose of Python's __call__ method?",
        "options": [
            "To define what happens when you call super() inside a class",
            "To make an instance of a class callable like a function",
            "To invoke all methods of a class in sequence",
            "To define the constructor used when copying objects"
        ],
        "answer": "To make an instance of a class callable like a function",
        "category": "Python & Programming",
        "difficulty": "Hard",
        "explanation": "Implementing __call__(self, ...) lets an instance be used with () syntax: obj(args). This is used in callable objects like function approximators, decorators implemented as classes, and scikit-learn estimators (which expose fit/predict but are also callable pipelines). It enables the strategy pattern elegantly."
    },
    {
        "question": "What is the difference between np.dot() and np.matmul() in NumPy?",
        "options": [
            "They are identical for all inputs",
            "np.dot() handles scalars and performs special 1D/2D logic; np.matmul() is strictly for matrix multiplication and does not allow scalar operands",
            "np.matmul() is deprecated in favor of np.dot()",
            "np.dot() uses GPU acceleration; np.matmul() uses CPU only"
        ],
        "answer": "np.dot() handles scalars and performs special 1D/2D logic; np.matmul() is strictly for matrix multiplication and does not allow scalar operands",
        "category": "Python & Programming",
        "difficulty": "Hard",
        "explanation": "np.matmul (also accessible via the @ operator) strictly performs matrix multiplication — it raises an error on scalars and does not contract over the last axis for 1D inputs the same way dot does. np.dot on 2D arrays behaves like matmul, but also handles scalars, 1D dot products, and N-D tensor contractions differently."
    },
    {
        "question": "What is the purpose of __enter__ and __exit__ in Python's context manager protocol?",
        "options": [
            "__enter__ initializes a class; __exit__ destroys it",
            "__enter__ is called when entering the 'with' block and sets up the resource; __exit__ is called on block exit to perform cleanup",
            "__enter__ opens a file; __exit__ reads from it",
            "They define the start and end of an asynchronous task"
        ],
        "answer": "__enter__ is called when entering the 'with' block and sets up the resource; __exit__ is called on block exit to perform cleanup",
        "category": "Python & Programming",
        "difficulty": "Hard",
        "explanation": "When Python executes 'with obj as x:', it calls obj.__enter__() and binds the return value to x. On exit (normal or exception), __exit__(exc_type, exc_val, exc_tb) is called. Returning True from __exit__ suppresses the exception. This guarantees cleanup (closing files, releasing locks) even when errors occur."
    },
    {
        "question": "What is the difference between a coroutine and a regular function in Python?",
        "options": [
            "Coroutines run in a separate thread; regular functions run in the main thread",
            "A coroutine is defined with async def and can be suspended with await, allowing other tasks to run; a regular function runs to completion",
            "Coroutines always return None; regular functions return values",
            "They are identical; 'coroutine' is just older terminology for a function"
        ],
        "answer": "A coroutine is defined with async def and can be suspended with await, allowing other tasks to run; a regular function runs to completion",
        "category": "Python & Programming",
        "difficulty": "Hard",
        "explanation": "Coroutines (async def) integrate with Python's asyncio event loop. When awaiting an I/O operation, the coroutine yields control, allowing other coroutines to progress — enabling concurrency without threads. They are ideal for I/O-bound tasks (HTTP requests, DB queries). They must be scheduled via asyncio.run() or awaited inside another coroutine."
    },
    {
        "question": "What does Python's sys.argv contain?",
        "options": [
            "A list of all installed packages in the current environment",
            "The command-line arguments passed to the script, with sys.argv[0] being the script name",
            "The Python version string and build metadata",
            "The list of directories Python searches when importing modules"
        ],
        "answer": "The command-line arguments passed to the script, with sys.argv[0] being the script name",
        "category": "Python & Programming",
        "difficulty": "Easy",
        "explanation": "sys.argv is a list of strings representing command-line arguments. sys.argv[0] is the script's filename; sys.argv[1:] are additional arguments. For production CLI tools, the argparse module provides argument parsing, validation, and automatic help generation on top of sys.argv."
    },
    {
        "question": "What is the purpose of Python's typing module?",
        "options": [
            "To measure keystroke performance in Python programs",
            "To provide type hint constructs (List, Dict, Optional, Union, etc.) for static analysis tools",
            "To enforce runtime type checking on function arguments",
            "To convert between Python types automatically"
        ],
        "answer": "To provide type hint constructs (List, Dict, Optional, Union, etc.) for static analysis tools",
        "category": "Python & Programming",
        "difficulty": "Easy",
        "explanation": "The typing module supplies generics and special forms for type annotations: List[int], Dict[str, float], Optional[str] (either the type or None), Union[int, str], Callable, and more. Type hints are not enforced at runtime by default but are used by tools like mypy, Pyright, and IDEs to catch errors before execution."
    },
    {
        "question": "What does the re.compile() function do in Python's re module?",
        "options": [
            "Compiles a Python script into bytecode for faster execution",
            "Pre-compiles a regular expression pattern into a reusable regex object for efficiency",
            "Checks whether a string is a valid regular expression",
            "Converts a list of strings into a single regular expression"
        ],
        "answer": "Pre-compiles a regular expression pattern into a reusable regex object for efficiency",
        "category": "Python & Programming",
        "difficulty": "Easy",
        "explanation": "re.compile(pattern) returns a compiled regex object whose methods (match, search, findall, sub) can be reused without recompiling the pattern each time. This is beneficial when the same pattern is applied many times in a loop. The pattern undergoes one-time compilation into an internal state machine."
    },
    {
        "question": "What is the difference between extend() and append() on a Python list?",
        "options": [
            "append() adds elements individually from an iterable; extend() adds the iterable as a single nested element",
            "extend() adds all elements from an iterable one by one; append() adds a single object (which may itself be a list) as one element",
            "They produce identical results for all input types",
            "extend() modifies both lists; append() modifies only the calling list"
        ],
        "answer": "extend() adds all elements from an iterable one by one; append() adds a single object (which may itself be a list) as one element",
        "category": "Python & Programming",
        "difficulty": "Easy",
        "explanation": "lst.append([1,2]) adds the list [1,2] as a single element: lst = [..., [1,2]]. lst.extend([1,2]) unpacks and adds 1 and 2 individually: lst = [..., 1, 2]. Extend is equivalent to lst += [1, 2]. Confusing these two is a common bug when building lists incrementally."
    },
    {
        "question": "What does the pandas DataFrame.pivot_table() method do?",
        "options": [
            "Transposes rows and columns of the DataFrame",
            "Creates a spreadsheet-style pivot table that aggregates data by row and column groupings",
            "Rotates a DataFrame 90 degrees along the time axis",
            "Merges two DataFrames on multiple keys simultaneously"
        ],
        "answer": "Creates a spreadsheet-style pivot table that aggregates data by row and column groupings",
        "category": "Python & Programming",
        "difficulty": "Medium",
        "explanation": "pivot_table(values='sales', index='region', columns='quarter', aggfunc='sum') summarizes data like an Excel pivot table. You specify which column's values to aggregate, what to use as row labels, column labels, and the aggregation function. fill_value= handles NaN cells in sparse pivot tables."
    },
    {
        "question": "What is the purpose of Python's logging module over print statements?",
        "options": [
            "logging is faster than print for large volumes of output",
            "logging provides severity levels, configurable output destinations, and can be silenced without modifying code",
            "logging automatically sends messages to an external monitoring service",
            "logging formats output as JSON by default for machine parsing"
        ],
        "answer": "logging provides severity levels, configurable output destinations, and can be silenced without modifying code",
        "category": "Python & Programming",
        "difficulty": "Medium",
        "explanation": "The logging module offers levels (DEBUG, INFO, WARNING, ERROR, CRITICAL), configurable handlers (file, stream, network), and formatters. Log levels let you filter messages without removing code — set level to WARNING in production to silence DEBUG/INFO. Unlike print, it is designed for library authors and long-running applications."
    },
    {
        "question": "What is the purpose of np.random.seed() in NumPy?",
        "options": [
            "To initialize an array with random values",
            "To set the random number generator state, ensuring reproducible random sequences",
            "To shuffle an array in place with a guaranteed distribution",
            "To limit the range of values generated by np.random functions"
        ],
        "answer": "To set the random number generator state, ensuring reproducible random sequences",
        "category": "Python & Programming",
        "difficulty": "Easy",
        "explanation": "np.random.seed(42) initializes the pseudorandom number generator to a fixed state, so subsequent calls to np.random.rand(), np.random.shuffle(), etc., always produce the same sequence. This is essential for reproducible experiments and unit tests. In modern NumPy, the preferred approach is np.random.default_rng(42) using the Generator API."
    },
    {
        "question": "What is Python's collections.Counter class used for?",
        "options": [
            "Counting lines of code in a Python file",
            "A dict subclass for counting hashable items, returning counts as values",
            "A thread-safe integer counter for concurrent programs",
            "Tracking how many times a function has been called"
        ],
        "answer": "A dict subclass for counting hashable items, returning counts as values",
        "category": "Python & Programming",
        "difficulty": "Easy",
        "explanation": "Counter(['a','b','a','c','a']) returns Counter({'a':3,'b':1,'c':1}). Useful methods include most_common(n), which returns the n most frequent elements. Counter objects support addition, subtraction, and intersection. It is the go-to tool for frequency analysis and histogram generation."
    },
    {
        "question": "What is type hinting in Python and why is it useful?",
        "options": [
            "A way to enforce strict typing at runtime, preventing type errors from occurring",
            "Annotations that document expected types for static analysis, IDE autocomplete, and code readability — without runtime enforcement by default",
            "A feature exclusive to Python 3.10+ that replaces duck typing",
            "A method for converting data between types automatically during function calls"
        ],
        "answer": "Annotations that document expected types for static analysis, IDE autocomplete, and code readability — without runtime enforcement by default",
        "category": "Python & Programming",
        "difficulty": "Easy",
        "explanation": "Type hints (def add(x: int, y: int) -> int:) are annotations stored in __annotations__ but not enforced at runtime by Python itself. Tools like mypy perform static analysis to catch type errors before running the code. IDEs use hints for autocomplete and refactoring. The typing module provides advanced constructs like Union, Optional, and Generic."
    },
    {
        "question": "What does Python's heapq module provide?",
        "options": [
            "A balanced binary search tree implementation",
            "Heap queue (priority queue) algorithms operating on regular Python lists",
            "A sorted set data structure with O(log n) membership testing",
            "An interface for managing memory heaps in CPython internals"
        ],
        "answer": "Heap queue (priority queue) algorithms operating on regular Python lists",
        "category": "Python & Programming",
        "difficulty": "Medium",
        "explanation": "heapq provides heappush, heappop, heapify, and nlargest/nsmallest. It maintains a min-heap invariant on a standard list. heappush(heap, item) and heappop(heap) are O(log n). Useful for efficiently finding the k smallest/largest elements or implementing Dijkstra's algorithm."
    },
    {
        "question": "What is the difference between a module and a package in Python?",
        "options": [
            "A module is a directory; a package is a single .py file",
            "A module is a single .py file; a package is a directory containing an __init__.py and multiple modules",
            "They are interchangeable terms in Python",
            "A package is a compiled .pyc file; a module is an uncompiled source file"
        ],
        "answer": "A module is a single .py file; a package is a directory containing an __init__.py and multiple modules",
        "category": "Python & Programming",
        "difficulty": "Easy",
        "explanation": "A module is any importable .py file (import math). A package is a directory with __init__.py that groups related modules (from sklearn.linear_model import LinearRegression). Packages enable hierarchical namespacing. Sub-packages are nested package directories, allowing deep import paths like import os.path."
    },
    {
        "question": "What is the difference between deepcopy and serialization (pickle) for duplicating Python objects?",
        "options": [
            "They are equivalent; both create independent copies of all objects",
            "deepcopy preserves in-memory object identity cycles; pickle serializes to bytes, losing object identity across serialize/deserialize boundaries",
            "pickle is always faster; deepcopy is only needed for network transmission",
            "deepcopy only works for primitive types; pickle works for all objects"
        ],
        "answer": "deepcopy preserves in-memory object identity cycles; pickle serializes to bytes, losing object identity across serialize/deserialize boundaries",
        "category": "Python & Programming",
        "difficulty": "Hard",
        "explanation": "copy.deepcopy handles cyclic references and shared object graphs correctly within a process — two refs to the same object in the source both point to the same copy. pickle + unpickle creates independent objects; shared references become distinct copies. For saving/loading models across sessions, pickle is used; for in-memory duplication, deepcopy is appropriate."
    },
    {
        "question": "What is the purpose of Python's __all__ variable in a module?",
        "options": [
            "It lists all attributes defined in the module, including private ones",
            "It controls what is exported when 'from module import *' is used",
            "It specifies the module's version and author metadata",
            "It prevents circular imports by declaring allowed importers"
        ],
        "answer": "It controls what is exported when 'from module import *' is used",
        "category": "Python & Programming",
        "difficulty": "Medium",
        "explanation": "__all__ = ['PublicClass', 'public_func'] restricts 'from module import *' to only those names. Without __all__, all names not starting with underscore are exported. Defining __all__ is good practice for library authors — it makes the public API explicit and prevents accidental exposure of internal helpers."
    },
    {
        "question": "What does the pandas apply() method do?",
        "options": [
            "Applies an SQL WHERE filter to a DataFrame",
            "Applies a function along an axis of a DataFrame or to each element of a Series",
            "Applies a schema validation to enforce column data types",
            "Applies a standard scaler normalization to all numeric columns"
        ],
        "answer": "Applies a function along an axis of a DataFrame or to each element of a Series",
        "category": "Python & Programming",
        "difficulty": "Medium",
        "explanation": "df['col'].apply(func) applies func to each element of a Series. df.apply(func, axis=1) applies func to each row as a Series. apply() is flexible but slower than vectorized operations (e.g., arithmetic, str methods) because it calls Python for each element. Use built-in pandas/NumPy operations for performance-critical paths."
    },
    {
        "question": "In Reinforcement Learning, what is the 'reward signal'?",
        "options": [
            "The loss function used to train a neural network",
            "A scalar feedback an agent receives after taking an action in an environment",
            "The probability distribution over possible next states",
            "The set of all possible actions an agent can take"
        ],
        "answer": "A scalar feedback an agent receives after taking an action in an environment",
        "category": "Reinforcement Learning",
        "difficulty": "Medium",
        "explanation": "The reward signal is the RL agent's primary feedback. The agent's goal is to maximize cumulative (discounted) reward over time. Reward design (reward shaping) is crucial — a poorly designed reward can lead to unexpected, undesired behaviors."
    },
    {
        "question": "What is the exploration-exploitation tradeoff in RL?",
        "options": [
            "Whether to use CPU or GPU for training",
            "The balance between trying new actions to discover rewards vs. using known high-reward actions",
            "Whether to use model-based or model-free RL",
            "The tradeoff between episode length and learning speed"
        ],
        "answer": "The balance between trying new actions to discover rewards vs. using known high-reward actions",
        "category": "Reinforcement Learning",
        "difficulty": "Medium",
        "explanation": "An agent that only exploits may get stuck in local optima; one that only explores never leverages what it's learned. Strategies like ε-greedy (random exploration with probability ε), UCB, and Thompson sampling manage this balance."
    },
    {
        "question": "What distinguishes Q-learning from policy gradient methods?",
        "options": [
            "Q-learning is only for continuous action spaces; policy gradient is for discrete",
            "Q-learning learns a value function (Q-values); policy gradient directly optimizes the policy",
            "Policy gradient is model-based; Q-learning is model-free",
            "Q-learning requires human feedback; policy gradient is self-supervised"
        ],
        "answer": "Q-learning learns a value function (Q-values); policy gradient directly optimizes the policy",
        "category": "Reinforcement Learning",
        "difficulty": "Hard",
        "explanation": "Q-learning (DQN) learns Q(s,a) — the expected return for taking action a in state s — and derives the policy implicitly. Policy gradient methods (REINFORCE, PPO) directly parameterize and optimize the policy π(a|s) using gradient ascent on expected reward."
    },
    {
        "question": "What is an agent in reinforcement learning?",
        "options": [
            "A database storing all possible actions",
            "The entity that observes the environment, takes actions, and receives rewards",
            "The function that maps states to probabilities",
            "A human supervisor who labels training data"
        ],
        "answer": "The entity that observes the environment, takes actions, and receives rewards",
        "category": "Reinforcement Learning",
        "difficulty": "Easy",
        "explanation": "In RL, the agent is the learner and decision-maker. It observes the current state, selects an action according to its policy, and receives a reward signal from the environment. The goal is to learn a policy that maximizes cumulative reward."
    },
    {
        "question": "What is a policy in reinforcement learning?",
        "options": [
            "The set of rules governing environment dynamics",
            "A mapping from states to actions or probability distributions over actions",
            "The total reward accumulated over an episode",
            "The memory buffer storing past transitions"
        ],
        "answer": "A mapping from states to actions or probability distributions over actions",
        "category": "Reinforcement Learning",
        "difficulty": "Easy",
        "explanation": "A policy defines the agent's behavior — it specifies what action to take in each state. Deterministic policies output a single action; stochastic policies output a probability distribution. The RL goal is to find the optimal policy that maximizes expected cumulative reward."
    },
    {
        "question": "What is the Bellman equation used for in RL?",
        "options": [
            "Computing the gradient of the policy function",
            "Expressing the value of a state as the immediate reward plus discounted value of the next state",
            "Calculating the entropy of the action distribution",
            "Defining the exploration strategy of the agent"
        ],
        "answer": "Expressing the value of a state as the immediate reward plus discounted value of the next state",
        "category": "Reinforcement Learning",
        "difficulty": "Medium",
        "explanation": "The Bellman equation decomposes the value of a state into the immediate reward plus the discounted value of the successor state: V(s) = R(s,a) + gamma * V(s'). It is the foundation of dynamic programming, Q-learning, and actor-critic methods."
    },
    {
        "question": "What is the discount factor (gamma) in reinforcement learning?",
        "options": [
            "The learning rate of the Q-network",
            "A value between 0 and 1 that determines how much future rewards are weighted versus immediate rewards",
            "The probability of taking a random action during exploration",
            "The ratio of successful episodes to total episodes"
        ],
        "answer": "A value between 0 and 1 that determines how much future rewards are weighted versus immediate rewards",
        "category": "Reinforcement Learning",
        "difficulty": "Medium",
        "explanation": "Gamma close to 1 makes the agent care about long-term rewards (farsighted); gamma close to 0 makes it focus on immediate rewards (myopic). It also ensures mathematical convergence of infinite-horizon return sums. Typical values range from 0.9 to 0.999."
    },
    {
        "question": "What is Proximal Policy Optimization (PPO) designed to solve?",
        "options": [
            "The credit assignment problem in sparse reward environments",
            "The instability and large, harmful policy updates that occur in vanilla policy gradient methods",
            "The sample inefficiency of model-free RL compared to model-based RL",
            "The inability of Q-learning to handle continuous action spaces"
        ],
        "answer": "The instability and large, harmful policy updates that occur in vanilla policy gradient methods",
        "category": "Reinforcement Learning",
        "difficulty": "Hard",
        "explanation": "PPO constrains the policy update size using a clipped surrogate objective, preventing excessively large updates that could collapse performance. It is more stable than TRPO but without its computationally expensive second-order constraint, making it the dominant on-policy RL algorithm for LLM alignment and robotics."
    },
    {
        "question": "What is a Markov Decision Process (MDP)?",
        "options": [
            "A supervised learning framework for sequential data",
            "A mathematical framework for modeling decision-making where outcomes are partly random and partly controlled",
            "A neural network architecture for processing time-series data",
            "A method for compressing high-dimensional state spaces"
        ],
        "answer": "A mathematical framework for modeling decision-making where outcomes are partly random and partly controlled",
        "category": "Reinforcement Learning",
        "difficulty": "Medium",
        "explanation": "An MDP is defined by (S, A, P, R, γ): states S, actions A, transition probabilities P(s'|s,a), reward function R(s,a,s'), and discount factor γ. The Markov property means the next state depends only on the current state and action, not the full history."
    },
    {
        "question": "What does the Markov property state in the context of RL?",
        "options": [
            "The agent must remember all past states to make optimal decisions",
            "The future is independent of the past given the present state",
            "The reward depends only on the action taken, not the current state",
            "The policy must be deterministic to satisfy the Markov condition"
        ],
        "answer": "The future is independent of the past given the present state",
        "category": "Reinforcement Learning",
        "difficulty": "Medium",
        "explanation": "The Markov property means the current state contains all necessary information for decision-making. Formally, P(s_{t+1} | s_t, a_t, s_{t-1}, a_{t-1}, ...) = P(s_{t+1} | s_t, a_t). When this holds, the problem is tractable as an MDP."
    },
    {
        "question": "What is the difference between on-policy and off-policy learning?",
        "options": [
            "On-policy uses neural networks; off-policy uses tabular methods",
            "On-policy learns from data generated by the current policy; off-policy can learn from data generated by a different policy",
            "On-policy is model-based; off-policy is model-free",
            "On-policy requires discrete actions; off-policy requires continuous actions"
        ],
        "answer": "On-policy learns from data generated by the current policy; off-policy can learn from data generated by a different policy",
        "category": "Reinforcement Learning",
        "difficulty": "Medium",
        "explanation": "SARSA is on-policy — it updates based on the action actually taken. Q-learning is off-policy — it updates toward the greedy action regardless of what was actually done. Off-policy methods allow experience replay and reuse of old data, improving sample efficiency."
    },
    {
        "question": "What is experience replay in Deep Q-Networks (DQN)?",
        "options": [
            "Replaying successful episodes to the agent as positive reinforcement",
            "Storing past transitions in a buffer and sampling mini-batches to break temporal correlations during training",
            "Replaying the policy gradient computation from previous iterations",
            "A method to simulate future states without interacting with the environment"
        ],
        "answer": "Storing past transitions in a buffer and sampling mini-batches to break temporal correlations during training",
        "category": "Reinforcement Learning",
        "difficulty": "Hard",
        "explanation": "Experience replay stores (s, a, r, s') tuples in a replay buffer. Random mini-batch sampling breaks the temporal correlations between consecutive samples, which would otherwise violate the i.i.d. assumption of gradient-based learning and cause instability."
    },
    {
        "question": "What is the purpose of the target network in DQN?",
        "options": [
            "To explore the environment using a separate policy",
            "To provide stable Q-value targets by updating slowly, reducing oscillations during training",
            "To handle continuous action spaces by discretizing them",
            "To compute the advantage function in actor-critic methods"
        ],
        "answer": "To provide stable Q-value targets by updating slowly, reducing oscillations during training",
        "category": "Reinforcement Learning",
        "difficulty": "Hard",
        "explanation": "Without a target network, the Q-value targets change at every step, creating a moving target problem that causes divergence. The target network is a delayed copy of the main network, updated periodically (hard update) or via exponential moving average (soft update)."
    },
    {
        "question": "What is the state-value function V(s) in RL?",
        "options": [
            "The immediate reward received when entering state s",
            "The expected cumulative discounted reward starting from state s following the current policy",
            "The probability of transitioning from state s to all possible next states",
            "The number of times state s has been visited during training"
        ],
        "answer": "The expected cumulative discounted reward starting from state s following the current policy",
        "category": "Reinforcement Learning",
        "difficulty": "Medium",
        "explanation": "V^π(s) = E_π[Σ γ^t r_t | s_0 = s]. It measures how good it is to be in a particular state under policy π. The optimal value function V*(s) is the maximum V(s) over all possible policies."
    },
    {
        "question": "What is the action-value function Q(s, a)?",
        "options": [
            "The probability of selecting action a in state s",
            "The expected cumulative discounted reward of taking action a in state s and then following the current policy",
            "The number of times action a was taken in state s during training",
            "The gradient of the policy with respect to the action"
        ],
        "answer": "The expected cumulative discounted reward of taking action a in state s and then following the current policy",
        "category": "Reinforcement Learning",
        "difficulty": "Medium",
        "explanation": "Q^π(s,a) = E_π[Σ γ^t r_t | s_0=s, a_0=a]. Unlike V(s), Q(s,a) evaluates a specific action, making it directly useful for deriving policies: π(s) = argmax_a Q(s,a). DQN learns Q* to derive the optimal policy."
    },
    {
        "question": "What is the advantage function A(s, a) used for in actor-critic methods?",
        "options": [
            "To measure how much better action a is compared to the average action in state s",
            "To compute the entropy of the action distribution",
            "To determine the step size of the policy gradient update",
            "To calculate the transition probability between states"
        ],
        "answer": "To measure how much better action a is compared to the average action in state s",
        "category": "Reinforcement Learning",
        "difficulty": "Hard",
        "explanation": "A(s,a) = Q(s,a) - V(s). A positive advantage means the action is better than average; negative means worse. Using A(s,a) instead of raw returns in policy gradient reduces variance while keeping the gradient estimate unbiased, leading to more stable training."
    },
    {
        "question": "What is an episode in the context of reinforcement learning?",
        "options": [
            "A single gradient update step of the neural network",
            "A complete sequence of interactions from an initial state to a terminal state",
            "The set of all states the agent can visit",
            "One batch of experience stored in the replay buffer"
        ],
        "answer": "A complete sequence of interactions from an initial state to a terminal state",
        "category": "Reinforcement Learning",
        "difficulty": "Easy",
        "explanation": "An episode (or trajectory) is a sequence (s_0, a_0, r_0, s_1, a_1, r_1, ..., s_T) that ends when a terminal state is reached. Episodic tasks have natural endings (e.g., a game over); continuing tasks run indefinitely, requiring discounting for finite returns."
    },
    {
        "question": "What is temporal difference (TD) learning?",
        "options": [
            "Learning from the difference between consecutive policy parameters",
            "A method that bootstraps by updating value estimates using other learned estimates without waiting for episode completion",
            "A technique for handling time-varying reward functions",
            "A way to compare the performance of two different policies"
        ],
        "answer": "A method that bootstraps by updating value estimates using other learned estimates without waiting for episode completion",
        "category": "Reinforcement Learning",
        "difficulty": "Hard",
        "explanation": "TD learning combines Monte Carlo (sampling) and dynamic programming (bootstrapping). The TD update V(s) ← V(s) + α[r + γV(s') - V(s)] uses the TD error δ = r + γV(s') - V(s). It can learn online, within episodes, without a model."
    },
    {
        "question": "What is the difference between Monte Carlo methods and TD learning in RL?",
        "options": [
            "Monte Carlo uses neural networks; TD learning uses lookup tables",
            "Monte Carlo waits until the end of an episode to update; TD learning updates after every step using bootstrapping",
            "Monte Carlo is off-policy only; TD learning is on-policy only",
            "Monte Carlo is for discrete actions; TD is for continuous actions"
        ],
        "answer": "Monte Carlo waits until the end of an episode to update; TD learning updates after every step using bootstrapping",
        "category": "Reinforcement Learning",
        "difficulty": "Medium",
        "explanation": "Monte Carlo uses actual episode returns (low bias, high variance). TD learning uses bootstrapped estimates (higher bias, lower variance). TD(λ) interpolates between both extremes using eligibility traces and the λ parameter."
    },
    {
        "question": "What is the REINFORCE algorithm?",
        "options": [
            "A value-based method that uses experience replay",
            "A Monte Carlo policy gradient algorithm that updates the policy using complete episode returns",
            "An actor-critic method using a neural network for both policy and value",
            "A model-based RL algorithm that learns environment dynamics"
        ],
        "answer": "A Monte Carlo policy gradient algorithm that updates the policy using complete episode returns",
        "category": "Reinforcement Learning",
        "difficulty": "Hard",
        "explanation": "REINFORCE uses the policy gradient theorem: ∇J(θ) = E[G_t ∇ log π_θ(a_t|s_t)], where G_t is the return from time t. It requires complete episodes (Monte Carlo), suffers from high variance, and is improved by subtracting a baseline (e.g., value function)."
    },
    {
        "question": "What is a model-based RL approach?",
        "options": [
            "An approach that uses a pre-trained language model as the agent",
            "An approach where the agent learns or is given a model of the environment to plan ahead",
            "An approach that requires a human model to supervise learning",
            "An approach that only works with continuous state and action spaces"
        ],
        "answer": "An approach where the agent learns or is given a model of the environment to plan ahead",
        "category": "Reinforcement Learning",
        "difficulty": "Medium",
        "explanation": "Model-based RL (e.g., Dyna, AlphaZero, MuZero) learns the transition dynamics P(s'|s,a) and uses them for planning (e.g., via tree search or imagined rollouts). This improves sample efficiency but introduces model bias if the learned model is inaccurate."
    },
    {
        "question": "What is the credit assignment problem in RL?",
        "options": [
            "Determining which model architecture to use for the policy network",
            "Figuring out which past actions in a sequence were responsible for a delayed reward",
            "Assigning separate learning rates to each layer of the neural network",
            "Distributing computational resources across parallel training environments"
        ],
        "answer": "Figuring out which past actions in a sequence were responsible for a delayed reward",
        "category": "Reinforcement Learning",
        "difficulty": "Medium",
        "explanation": "When reward comes long after the causative action, the agent struggles to determine which action deserves credit. Eligibility traces (TD(λ)), attention mechanisms, and reward shaping help address this. It is one of the fundamental challenges distinguishing RL from supervised learning."
    },
    {
        "question": "What is the ε-greedy exploration strategy?",
        "options": [
            "Taking the action with the highest Q-value always",
            "Taking a random action with probability ε and the greedy action with probability 1-ε",
            "Selecting actions proportional to their Q-values using a softmax function",
            "Exploring only in states that have been visited fewer than ε times"
        ],
        "answer": "Taking a random action with probability ε and the greedy action with probability 1-ε",
        "category": "Reinforcement Learning",
        "difficulty": "Easy",
        "explanation": "ε-greedy is the simplest exploration strategy. ε is typically annealed (decayed) from a high value (e.g., 1.0) to a small minimum (e.g., 0.01) as training progresses — exploring heavily early on and exploiting more as the policy improves."
    },
    {
        "question": "What is an actor-critic method in RL?",
        "options": [
            "A method where two separate agents compete against each other",
            "An architecture combining a policy (actor) that selects actions with a value function (critic) that evaluates them",
            "A human-in-the-loop training approach where humans act as critics",
            "A method that uses one network for discrete actions and another for continuous ones"
        ],
        "answer": "An architecture combining a policy (actor) that selects actions with a value function (critic) that evaluates them",
        "category": "Reinforcement Learning",
        "difficulty": "Medium",
        "explanation": "The actor learns the policy π(a|s) and the critic learns V(s) or Q(s,a). The critic's value estimates are used to compute the advantage signal, reducing variance in the actor's gradient updates. A3C, A2C, SAC, and PPO are all actor-critic variants."
    },
    {
        "question": "What is reward shaping in reinforcement learning?",
        "options": [
            "Clipping reward values to a fixed range to stabilize training",
            "Adding auxiliary reward signals to guide the agent toward desired behavior more efficiently",
            "Normalizing rewards using running mean and standard deviation",
            "Designing the final evaluation metric for the trained policy"
        ],
        "answer": "Adding auxiliary reward signals to guide the agent toward desired behavior more efficiently",
        "category": "Reinforcement Learning",
        "difficulty": "Medium",
        "explanation": "Reward shaping adds supplementary rewards to help the agent learn faster, especially with sparse rewards. Potential-based reward shaping preserves the optimal policy. Poor shaping can cause reward hacking, where the agent maximizes the shaped reward in unintended ways."
    },
    {
        "question": "What problem does Double DQN address?",
        "options": [
            "The inability of DQN to handle image-based observations",
            "The overestimation of Q-values caused by using the same network to select and evaluate actions",
            "The slow convergence of DQN in environments with large action spaces",
            "The lack of exploration in standard DQN due to greedy action selection"
        ],
        "answer": "The overestimation of Q-values caused by using the same network to select and evaluate actions",
        "category": "Reinforcement Learning",
        "difficulty": "Hard",
        "explanation": "Standard DQN uses max_a Q(s',a) for both action selection and evaluation, leading to systematic overestimation. Double DQN decouples these: the online network selects the action (argmax_a Q(s',a)), while the target network evaluates it, reducing overestimation bias."
    },
    {
        "question": "What is soft actor-critic (SAC) and what makes it distinctive?",
        "options": [
            "An on-policy actor-critic that uses soft value function approximation",
            "An off-policy actor-critic that maximizes both reward and entropy, encouraging exploration",
            "A method using soft attention over the action space to handle large discrete action sets",
            "An actor-critic variant that uses soft targets via exponential moving averages only"
        ],
        "answer": "An off-policy actor-critic that maximizes both reward and entropy, encouraging exploration",
        "category": "Reinforcement Learning",
        "difficulty": "Hard",
        "explanation": "SAC adds an entropy term H(π) to the reward objective: J(π) = Σ E[r_t + α H(π(·|s_t))]. This maximum-entropy RL framework encourages exploration, improves robustness, and prevents premature convergence. SAC is state-of-the-art for continuous control tasks."
    },
    {
        "question": "What is a sparse reward environment, and why is it challenging?",
        "options": [
            "An environment where rewards are noisy and unreliable",
            "An environment where rewards are only received rarely, making it hard for the agent to learn what behavior leads to success",
            "An environment with only two possible reward values: 0 or 1",
            "An environment where rewards decrease over time to encourage faster completion"
        ],
        "answer": "An environment where rewards are only received rarely, making it hard for the agent to learn what behavior leads to success",
        "category": "Reinforcement Learning",
        "difficulty": "Medium",
        "explanation": "In sparse reward settings (e.g., achieving a goal only at the end), random exploration rarely discovers rewards, so the agent receives almost no learning signal. Techniques like hindsight experience replay (HER), intrinsic motivation, and curriculum learning help address this challenge."
    },
    {
        "question": "What is hindsight experience replay (HER)?",
        "options": [
            "Prioritizing past experiences with high TD errors for more frequent replay",
            "Relabeling failed episodes as if the agent had achieved a different goal, enabling learning from failure",
            "Storing a separate buffer of successful episodes and replaying them more frequently",
            "Reversing the temporal order of a trajectory to learn backward through time"
        ],
        "answer": "Relabeling failed episodes as if the agent had achieved a different goal, enabling learning from failure",
        "category": "Reinforcement Learning",
        "difficulty": "Hard",
        "explanation": "HER takes a failed trajectory and retroactively relabels the goal as the state that was actually achieved. This creates a training signal even from failed attempts, dramatically improving sample efficiency in goal-conditioned sparse reward tasks like robotic manipulation."
    },
    {
        "question": "What is curriculum learning in the context of RL?",
        "options": [
            "Training the agent on the hardest tasks first to maximize learning speed",
            "Progressively increasing task difficulty as the agent's performance improves",
            "Using a fixed set of training tasks ordered by their state-space complexity",
            "Training separate policies for each difficulty level and combining them"
        ],
        "answer": "Progressively increasing task difficulty as the agent's performance improves",
        "category": "Reinforcement Learning",
        "difficulty": "Medium",
        "explanation": "Curriculum learning starts with easy task variants and gradually introduces harder ones. This provides more frequent learning signals early on and scaffolds skill acquisition. It is widely used in robotics, game-playing AI, and language model fine-tuning with RL."
    },
    {
        "question": "What is multi-agent reinforcement learning (MARL)?",
        "options": [
            "Training a single agent with multiple reward functions simultaneously",
            "A setting where multiple agents interact within a shared environment, potentially cooperating or competing",
            "Using an ensemble of neural networks to represent a single agent's policy",
            "Running multiple independent RL experiments in parallel to find the best hyperparameters"
        ],
        "answer": "A setting where multiple agents interact within a shared environment, potentially cooperating or competing",
        "category": "Reinforcement Learning",
        "difficulty": "Medium",
        "explanation": "MARL introduces challenges beyond single-agent RL: non-stationarity (the environment changes as other agents learn), credit assignment in cooperative settings, and strategic behavior in competitive settings. Examples include AlphaStar, OpenAI Five, and multi-robot coordination."
    },
    {
        "question": "What is the policy gradient theorem?",
        "options": [
            "A theorem stating that the optimal policy is always deterministic",
            "A result expressing the gradient of expected return with respect to policy parameters as an expectation over trajectories",
            "A rule for computing the optimal discount factor for a given environment",
            "A convergence guarantee for Q-learning under certain conditions"
        ],
        "answer": "A result expressing the gradient of expected return with respect to policy parameters as an expectation over trajectories",
        "category": "Reinforcement Learning",
        "difficulty": "Hard",
        "explanation": "The policy gradient theorem states: ∇_θ J(θ) = E_π[∇_θ log π_θ(a|s) · Q^π(s,a)]. It allows gradient-based optimization of the policy without requiring differentiation through the (possibly unknown) environment dynamics, forming the foundation of all policy gradient algorithms."
    },
    {
        "question": "What is intrinsic motivation in RL?",
        "options": [
            "Reward signals derived from human feedback rather than the environment",
            "Internally generated reward signals that encourage exploration or curiosity, independent of the task reward",
            "The agent's tendency to prefer actions it has taken successfully before",
            "A regularization term that penalizes large policy updates"
        ],
        "answer": "Internally generated reward signals that encourage exploration or curiosity, independent of the task reward",
        "category": "Reinforcement Learning",
        "difficulty": "Medium",
        "explanation": "Intrinsic motivation includes curiosity (rewarding prediction error), count-based exploration bonuses, and information gain. Methods like Random Network Distillation (RND) and ICM (Intrinsic Curiosity Module) add intrinsic rewards to help agents explore in sparse reward environments."
    },
    {
        "question": "What is the role of entropy regularization in policy gradient methods?",
        "options": [
            "To speed up convergence by reducing the gradient magnitude",
            "To encourage exploration by penalizing overly deterministic (low-entropy) policies",
            "To prevent the value function from overfitting to specific states",
            "To normalize the rewards across different episodes"
        ],
        "answer": "To encourage exploration by penalizing overly deterministic (low-entropy) policies",
        "category": "Reinforcement Learning",
        "difficulty": "Hard",
        "explanation": "Adding an entropy bonus H(π) = -Σ π(a|s) log π(a|s) to the objective prevents premature convergence to suboptimal deterministic policies. The temperature coefficient α controls the tradeoff between reward maximization and entropy maximization. This is central to maximum-entropy RL (SAC)."
    },
    {
        "question": "What is a replay buffer and why is it useful?",
        "options": [
            "A memory structure that stores the best-performing policy checkpoints",
            "A data structure that stores past (s, a, r, s') transitions for reuse in off-policy learning",
            "A priority queue that ranks states by their estimated value",
            "A cache of environment observations used to normalize inputs"
        ],
        "answer": "A data structure that stores past (s, a, r, s') transitions for reuse in off-policy learning",
        "category": "Reinforcement Learning",
        "difficulty": "Easy",
        "explanation": "Replay buffers enable off-policy learning by decoupling data collection from learning. Mini-batches are randomly sampled, breaking temporal correlations. They improve sample efficiency since each experience can be used multiple times. DQN, SAC, and TD3 all rely on replay buffers."
    },
    {
        "question": "What is prioritized experience replay?",
        "options": [
            "Replaying only the most recent experiences in the order they were collected",
            "Sampling experiences from the buffer with higher probability for transitions with larger TD errors",
            "Giving priority to episodes with higher total returns during training",
            "Replaying successful trajectories more frequently than failed ones"
        ],
        "answer": "Sampling experiences from the buffer with higher probability for transitions with larger TD errors",
        "category": "Reinforcement Learning",
        "difficulty": "Hard",
        "explanation": "Prioritized experience replay (PER) assigns priorities based on |δ| (TD error magnitude). Transitions with higher errors represent more surprising, informative experiences. Importance sampling weights correct for the resulting bias. PER significantly improves DQN performance on Atari benchmarks."
    },
    {
        "question": "What is the difference between value-based and policy-based RL methods?",
        "options": [
            "Value-based methods work only offline; policy-based only online",
            "Value-based methods learn value functions and derive policies implicitly; policy-based methods directly optimize a parameterized policy",
            "Value-based methods are for discrete spaces; policy-based for continuous spaces exclusively",
            "Value-based methods use neural networks; policy-based use linear function approximators"
        ],
        "answer": "Value-based methods learn value functions and derive policies implicitly; policy-based methods directly optimize a parameterized policy",
        "category": "Reinforcement Learning",
        "difficulty": "Medium",
        "explanation": "Value-based methods (DQN, SARSA) learn Q(s,a) and act greedily with respect to it. Policy-based methods (REINFORCE, PPO) parameterize π(a|s;θ) directly. Value-based methods tend to be more sample-efficient; policy-based handle continuous actions and stochastic policies more naturally."
    },
    {
        "question": "What is the function approximation challenge in RL?",
        "options": [
            "Approximating the reward function when it is unknown",
            "Using parameterized functions (like neural networks) to generalize value or policy estimates across large state spaces",
            "Computing exact transition probabilities in high-dimensional environments",
            "Fitting the discount factor to the specific task requirements"
        ],
        "answer": "Using parameterized functions (like neural networks) to generalize value or policy estimates across large state spaces",
        "category": "Reinforcement Learning",
        "difficulty": "Medium",
        "explanation": "Tabular methods become infeasible for large state spaces (e.g., pixels). Function approximation (linear, neural networks) generalizes across states but can cause instability — the deadly triad: function approximation + bootstrapping + off-policy learning can diverge. DQN addresses this with target networks and replay."
    },
    {
        "question": "What is Trust Region Policy Optimization (TRPO)?",
        "options": [
            "An algorithm that restricts policy updates to a trust region defined by the KL divergence between old and new policies",
            "A method that clips gradients to a fixed norm before applying policy updates",
            "An off-policy algorithm that uses importance sampling to reuse data from older policies",
            "A model-based method that plans within a learned world model"
        ],
        "answer": "An algorithm that restricts policy updates to a trust region defined by the KL divergence between old and new policies",
        "category": "Reinforcement Learning",
        "difficulty": "Hard",
        "explanation": "TRPO solves a constrained optimization problem: maximize policy improvement subject to KL(π_old || π_new) ≤ δ. It guarantees monotonic policy improvement but requires second-order optimization (conjugate gradients), making it computationally expensive. PPO approximates TRPO's guarantees more cheaply."
    },
    {
        "question": "What is the role of the baseline in the REINFORCE algorithm?",
        "options": [
            "To define the minimum acceptable reward threshold for task completion",
            "To reduce variance in gradient estimates without introducing bias",
            "To determine the initial weights of the policy network",
            "To clip the policy gradient to prevent catastrophic updates"
        ],
        "answer": "To reduce variance in gradient estimates without introducing bias",
        "category": "Reinforcement Learning",
        "difficulty": "Hard",
        "explanation": "Subtracting a baseline b(s) from returns gives: ∇J(θ) = E[(G_t - b(s_t)) ∇ log π_θ(a_t|s_t)]. This doesn't change the expected gradient (unbiased) but reduces its variance, leading to more stable training. The state-value function V(s) is the most common baseline choice."
    },
    {
        "question": "What is transfer learning in reinforcement learning?",
        "options": [
            "Moving trained policies from simulation to real hardware without retraining",
            "Leveraging knowledge gained in one task or environment to improve learning in a different but related task",
            "Transferring the replay buffer contents between two separate training runs",
            "Copying the weights from a supervised learning model to initialize the RL agent"
        ],
        "answer": "Leveraging knowledge gained in one task or environment to improve learning in a different but related task",
        "category": "Reinforcement Learning",
        "difficulty": "Medium",
        "explanation": "Transfer learning in RL uses representations, policies, or value functions trained on a source task to accelerate training on a target task. Challenges include negative transfer (when knowledge harms performance), domain shift, and determining which components to transfer."
    },
    {
        "question": "What is imitation learning?",
        "options": [
            "An approach where the agent mimics random behavior to boost exploration",
            "Learning a policy by observing and replicating demonstrations from an expert",
            "Training the agent by copying the weights of another trained RL agent",
            "Using data augmentation to simulate expert behavior artificially"
        ],
        "answer": "Learning a policy by observing and replicating demonstrations from an expert",
        "category": "Reinforcement Learning",
        "difficulty": "Medium",
        "explanation": "Imitation learning includes behavioral cloning (supervised learning on expert actions) and inverse RL (inferring the reward function from demonstrations). It is valuable when reward design is difficult. DAgger addresses the distribution shift problem in behavioral cloning."
    },
    {
        "question": "What is inverse reinforcement learning (IRL)?",
        "options": [
            "Running the RL training process in reverse time order for better credit assignment",
            "Inferring the reward function from observed expert behavior, then using it to train an agent",
            "Learning a policy that achieves the opposite of the reward signal",
            "An off-policy method that reverses the roles of actor and critic"
        ],
        "answer": "Inferring the reward function from observed expert behavior, then using it to train an agent",
        "category": "Reinforcement Learning",
        "difficulty": "Hard",
        "explanation": "IRL assumes an expert is optimizing an unknown reward and attempts to recover it. The inferred reward is more generalizable than demonstrations alone. IRL is closely related to imitation learning but provides a transferable reward function. GAIL extends IRL using adversarial training."
    },
    {
        "question": "What is hierarchical reinforcement learning?",
        "options": [
            "An approach where multiple agents are organized in a hierarchy based on their performance",
            "A framework where high-level policies set subgoals and low-level policies execute primitive actions to achieve them",
            "Training policies at multiple timescales simultaneously without explicit subgoal setting",
            "A method that uses multiple layers of neural networks to represent the value function"
        ],
        "answer": "A framework where high-level policies set subgoals and low-level policies execute primitive actions to achieve them",
        "category": "Reinforcement Learning",
        "difficulty": "Hard",
        "explanation": "Hierarchical RL (e.g., options framework, HIRO, feudal networks) decomposes tasks into temporal abstractions. A manager policy selects subgoals at a coarse timescale; worker policies achieve them. This improves long-horizon planning, sample efficiency, and transfer across tasks."
    },
    {
        "question": "What is the options framework in hierarchical RL?",
        "options": [
            "A method for selecting between discrete and continuous action spaces adaptively",
            "Temporally extended actions with their own initiation sets, internal policies, and termination conditions",
            "A technique for combining multiple reward functions into a single objective",
            "An approach for choosing between model-based and model-free learning dynamically"
        ],
        "answer": "Temporally extended actions with their own initiation sets, internal policies, and termination conditions",
        "category": "Reinforcement Learning",
        "difficulty": "Hard",
        "explanation": "An option is a triple (I, π, β): initiation set I (states where the option can start), intra-option policy π(a|s), and termination condition β(s). Options abstract away low-level details, enabling semi-MDPs where actions last for variable durations. SMDP Q-learning extends Q-learning to options."
    },
    {
        "question": "What is reward hacking in reinforcement learning?",
        "options": [
            "Manually modifying the reward function to improve training speed",
            "When an agent finds unintended ways to maximize the reward signal that violate the intended objective",
            "Exploiting numerical precision errors in the reward computation",
            "Using negative rewards to steer the agent away from dangerous states"
        ],
        "answer": "When an agent finds unintended ways to maximize the reward signal that violate the intended objective",
        "category": "Reinforcement Learning",
        "difficulty": "Medium",
        "explanation": "Reward hacking (Goodhart's Law in RL) occurs when the proxy reward diverges from the true objective. Classic examples: a boat racing agent spinning in circles to collect bonus tiles without finishing the race, or a simulated robot exploiting physics bugs. Robust reward design is critical."
    },
    {
        "question": "What is the difference between episodic and continuing tasks in RL?",
        "options": [
            "Episodic tasks use discrete actions; continuing tasks use continuous actions",
            "Episodic tasks have natural terminal states ending episodes; continuing tasks run indefinitely without natural endpoints",
            "Episodic tasks use Monte Carlo methods; continuing tasks use TD methods exclusively",
            "Episodic tasks have fixed reward functions; continuing tasks have changing rewards"
        ],
        "answer": "Episodic tasks have natural terminal states ending episodes; continuing tasks run indefinitely without natural endpoints",
        "category": "Reinforcement Learning",
        "difficulty": "Easy",
        "explanation": "In episodic tasks (chess, Atari games), the agent resets after each terminal state. In continuing tasks (process control, trading), there is no natural reset, requiring discounting (γ < 1) to ensure finite return sums. Some algorithms need modification to handle both settings correctly."
    },
    {
        "question": "What is the purpose of normalization of rewards and observations in RL?",
        "options": [
            "To ensure the policy always outputs probabilities that sum to 1",
            "To stabilize training by preventing large-scale inputs or targets from causing gradient explosion or slow learning",
            "To convert discrete rewards into continuous ones for policy gradient methods",
            "To enforce the Markov property in partially observable environments"
        ],
        "answer": "To stabilize training by preventing large-scale inputs or targets from causing gradient explosion or slow learning",
        "category": "Reinforcement Learning",
        "difficulty": "Medium",
        "explanation": "Deep RL is sensitive to input scale. Observation normalization (running mean/std) prevents activation saturation. Reward normalization or clipping (e.g., clipping to [-1, 1] as in DQN for Atari) prevents value function targets from being too large, stabilizing training."
    },
    {
        "question": "What is the deadly triad in deep reinforcement learning?",
        "options": [
            "The combination of sparse rewards, continuous action spaces, and partial observability",
            "The combination of function approximation, bootstrapping, and off-policy learning, which together can cause divergence",
            "The combination of high learning rate, large batch size, and small replay buffer",
            "The combination of deep networks, long episodes, and delayed rewards"
        ],
        "answer": "The combination of function approximation, bootstrapping, and off-policy learning, which together can cause divergence",
        "category": "Reinforcement Learning",
        "difficulty": "Hard",
        "explanation": "Richard Sutton identified this deadly triad: (1) function approximation (neural nets), (2) bootstrapping (using estimated values as targets, as in TD), and (3) off-policy learning. Each alone is manageable, but together they can cause Q-values to diverge. DQN stabilizes this with target networks and replay."
    },
    {
        "question": "What is a partially observable MDP (POMDP)?",
        "options": [
            "An MDP where only part of the reward is revealed to the agent",
            "An MDP where the agent cannot directly observe the full state and must infer it from partial observations",
            "An MDP where some actions are unavailable in certain states",
            "An MDP where the transition function is only partially known"
        ],
        "answer": "An MDP where the agent cannot directly observe the full state and must infer it from partial observations",
        "category": "Reinforcement Learning",
        "difficulty": "Hard",
        "explanation": "In a POMDP, the agent receives observations o ~ O(s) rather than the true state s. The agent must maintain a belief state (probability distribution over true states) to make good decisions. Recurrent networks (LSTMs, Transformers) are commonly used to handle partial observability in deep RL."
    },
    {
        "question": "What is Asynchronous Advantage Actor-Critic (A3C)?",
        "options": [
            "An actor-critic method that trains multiple independent agents in parallel using asynchronous gradient updates",
            "A method that uses three separate neural networks: actor, advantage estimator, and critic",
            "An off-policy actor-critic method using asynchronous experience replay",
            "A distributed RL method where agents communicate asynchronously to share policies"
        ],
        "answer": "An actor-critic method that trains multiple independent agents in parallel using asynchronous gradient updates",
        "category": "Reinforcement Learning",
        "difficulty": "Hard",
        "explanation": "A3C runs multiple worker agents in parallel, each with its own environment. Workers compute gradients asynchronously and update a shared global network. This replaces experience replay with parallelism to decorrelate training data, improving stability. A2C is the synchronous variant."
    },
    {
        "question": "What is model-free reinforcement learning?",
        "options": [
            "RL that does not use any neural network models",
            "RL where the agent learns to act through direct trial-and-error interaction without learning an explicit model of environment dynamics",
            "RL applied to environments without physics simulations",
            "RL that avoids using function approximation"
        ],
        "answer": "RL where the agent learns to act through direct trial-and-error interaction without learning an explicit model of environment dynamics",
        "category": "Reinforcement Learning",
        "difficulty": "Easy",
        "explanation": "Model-free RL (Q-learning, SARSA, PPO, SAC) learns value functions or policies directly from environment interactions without explicitly modeling P(s'|s,a). It is simpler and more broadly applicable but requires more samples than model-based RL, since it cannot use imagined rollouts."
    },
    {
        "question": "What is the purpose of the clipping in PPO's objective function?",
        "options": [
            "To clip gradient norms and prevent exploding gradients",
            "To limit how much the probability ratio between old and new policies can change, preventing destabilizing large updates",
            "To clip Q-values to a fixed range to avoid value overestimation",
            "To clip rewards to [-1, 1] to stabilize training across environments"
        ],
        "answer": "To limit how much the probability ratio between old and new policies can change, preventing destabilizing large updates",
        "category": "Reinforcement Learning",
        "difficulty": "Hard",
        "explanation": "PPO's clipped objective is L^CLIP(θ) = E[min(r_t(θ)Â_t, clip(r_t(θ), 1-ε, 1+ε)Â_t)], where r_t(θ) = π_θ(a|s)/π_θ_old(a|s). The clip ensures the policy doesn't move too far from the old policy, approximating the TRPO trust region constraint without second-order optimization."
    },
    {
        "question": "What is the Dyna architecture in RL?",
        "options": [
            "A deep neural architecture specifically designed for RL with dynamic memory",
            "A framework that combines model-free learning with model-based planning using a learned world model",
            "A distributed training architecture for scaling RL to large clusters",
            "An architecture that dynamically adjusts the discount factor based on episode progress"
        ],
        "answer": "A framework that combines model-free learning with model-based planning using a learned world model",
        "category": "Reinforcement Learning",
        "difficulty": "Hard",
        "explanation": "Dyna (Sutton 1991) integrates direct RL (learning from real experience) with indirect RL (planning via simulated experience from a learned model). The agent performs k planning steps (imagined rollouts) per real environment step, improving sample efficiency. Dyna-Q is the Q-learning variant."
    },
    {
        "question": "What is reward clipping in DQN and why is it used?",
        "options": [
            "Clipping the policy gradient to a maximum norm to prevent large updates",
            "Clipping rewards to [-1, 0, 1] to normalize across Atari games with different reward scales",
            "Removing negative rewards to stabilize training in early stages",
            "Clipping Q-values to a fixed maximum to prevent value divergence"
        ],
        "answer": "Clipping rewards to [-1, 0, 1] to normalize across Atari games with different reward scales",
        "category": "Reinforcement Learning",
        "difficulty": "Medium",
        "explanation": "Different Atari games have very different reward magnitudes. The original DQN paper clips all rewards to [-1, 1] so a single set of hyperparameters works across games. While it enables cross-game transfer of hyperparameters, it loses information about the relative magnitude of rewards within a game."
    },
    {
        "question": "What is the difference between SARSA and Q-learning?",
        "options": [
            "SARSA uses neural networks while Q-learning uses tabular methods",
            "SARSA is on-policy and updates using the action actually taken; Q-learning is off-policy and updates using the max action",
            "SARSA uses eligibility traces; Q-learning does not support them",
            "SARSA is for continuous action spaces; Q-learning is for discrete ones"
        ],
        "answer": "SARSA is on-policy and updates using the action actually taken; Q-learning is off-policy and updates using the max action",
        "category": "Reinforcement Learning",
        "difficulty": "Medium",
        "explanation": "SARSA update: Q(s,a) ← Q(s,a) + α[r + γQ(s',a') - Q(s,a)], using the next action a' actually selected by the policy. Q-learning update: Q(s,a) ← Q(s,a) + α[r + γ max_a' Q(s',a') - Q(s,a)], always bootstrapping toward the greedy action regardless of what was taken."
    },
    {
        "question": "What does 'bootstrapping' mean in the context of TD learning?",
        "options": [
            "Initializing the neural network weights from a pre-trained supervised learning model",
            "Updating value estimates using other learned estimates rather than waiting for actual returns",
            "Using random restarts during training to escape local optima",
            "Generating additional training data by sampling from the replay buffer multiple times"
        ],
        "answer": "Updating value estimates using other learned estimates rather than waiting for actual returns",
        "category": "Reinforcement Learning",
        "difficulty": "Medium",
        "explanation": "Bootstrapping means using V(s') or Q(s',a') — which are themselves learned approximations — as targets for updating V(s) or Q(s,a). Unlike Monte Carlo which waits for actual returns, bootstrapping allows online, step-by-step updates but introduces bias since the targets are imperfect estimates."
    },
    {
        "question": "What is generalized advantage estimation (GAE) in PPO and A3C?",
        "options": [
            "A method for estimating the advantage function using a weighted combination of multi-step TD errors",
            "A generalized version of the Bellman equation for stochastic policies",
            "A technique for computing policy gradients in environments with generalized reward functions",
            "An advantage function that works across both discrete and continuous action spaces"
        ],
        "answer": "A method for estimating the advantage function using a weighted combination of multi-step TD errors",
        "category": "Reinforcement Learning",
        "difficulty": "Hard",
        "explanation": "GAE(γ, λ) = Σ (γλ)^l δ_{t+l}, where δ_t is the 1-step TD error. The λ parameter interpolates between 1-step TD (λ=0, low variance, high bias) and Monte Carlo returns (λ=1, low bias, high variance). GAE is widely used in PPO and other actor-critic methods to achieve a favorable bias-variance tradeoff."
    },
    {
        "question": "What is the median of a dataset?",
        "options": [
            "The most frequently occurring value",
            "The arithmetic average of all values",
            "The middle value when data is sorted",
            "The difference between maximum and minimum"
        ],
        "answer": "The middle value when data is sorted",
        "category": "Statistics & Math",
        "difficulty": "Easy",
        "explanation": "The median is the 50th percentile — the middle value in a sorted dataset. It's more robust to outliers than the mean, making it the preferred measure of central tendency for skewed distributions."
    },
    {
        "question": "What does standard deviation measure?",
        "options": [
            "The average value in a dataset",
            "The spread or dispersion of data around the mean",
            "The correlation between two variables",
            "The minimum value in a dataset"
        ],
        "answer": "The spread or dispersion of data around the mean",
        "category": "Statistics & Math",
        "difficulty": "Easy",
        "explanation": "Standard deviation quantifies how much individual data points deviate from the mean. A low SD means data is clustered closely; a high SD means data is widely spread. It's the square root of variance."
    },
    {
        "question": "What type of plot is best for showing the distribution of a single numerical variable?",
        "options": [
            "Bar chart",
            "Scatter plot",
            "Histogram",
            "Line chart"
        ],
        "answer": "Histogram",
        "category": "Statistics & Math",
        "difficulty": "Easy",
        "explanation": "A histogram divides a numerical variable into bins and shows the frequency of values in each bin, revealing shape (normal, skewed, bimodal), spread, and outliers of the distribution."
    },
    {
        "question": "What is the Central Limit Theorem?",
        "options": [
            "The mean of any dataset is always normally distributed",
            "Sample means from any distribution approach a normal distribution as sample size grows",
            "All data in nature follows a normal distribution",
            "Large datasets always have zero skewness"
        ],
        "answer": "Sample means from any distribution approach a normal distribution as sample size grows",
        "category": "Statistics & Math",
        "difficulty": "Medium",
        "explanation": "The CLT states that the sampling distribution of the mean approaches a normal distribution as sample size n → ∞, regardless of the original distribution's shape. This underlies hypothesis testing and confidence intervals."
    },
    {
        "question": "What does a p-value represent in hypothesis testing?",
        "options": [
            "The probability that the null hypothesis is true",
            "The probability of observing results at least as extreme as the data, assuming the null hypothesis is true",
            "The effect size of the treatment",
            "The power of the statistical test"
        ],
        "answer": "The probability of observing results at least as extreme as the data, assuming the null hypothesis is true",
        "category": "Statistics & Math",
        "difficulty": "Medium",
        "explanation": "A p-value < 0.05 means that if H₀ were true, there's less than a 5% chance of seeing data as extreme as observed — so we reject H₀. Crucially, p-value is NOT the probability that H₀ is true."
    },
    {
        "question": "What is the difference between correlation and causation?",
        "options": [
            "They are the same if the correlation is very strong",
            "Correlation means two variables are related; causation means one directly causes the other",
            "Causation can only be proven with large datasets",
            "Correlation is only relevant for linear relationships"
        ],
        "answer": "Correlation means two variables are related; causation means one directly causes the other",
        "category": "Statistics & Math",
        "difficulty": "Medium",
        "explanation": "Two variables can be correlated (move together) without one causing the other — e.g., ice cream sales and drowning rates correlate because of a third variable (hot weather). Causation requires controlled experiments or causal inference methods."
    },
    {
        "question": "What is Bayes' Theorem used for in machine learning?",
        "options": [
            "Computing the gradient of the loss function",
            "Updating the probability of a hypothesis given new evidence",
            "Measuring feature importance in tree models",
            "Normalizing probability distributions to sum to 1"
        ],
        "answer": "Updating the probability of a hypothesis given new evidence",
        "category": "Statistics & Math",
        "difficulty": "Hard",
        "explanation": "Bayes' Theorem: P(H|E) = P(E|H) × P(H) / P(E). It updates prior beliefs with new evidence to produce a posterior probability. Used in Naive Bayes classifiers, Bayesian neural networks, and probabilistic graphical models."
    },
    {
        "question": "What is the mean of a dataset?",
        "options": [
            "The most frequently occurring value",
            "The middle value when data is sorted",
            "The arithmetic average of all values",
            "The range divided by the number of data points"
        ],
        "answer": "The arithmetic average of all values",
        "category": "Statistics & Math",
        "difficulty": "Easy",
        "explanation": "The mean is the sum of all values divided by the count. It is the most common measure of central tendency but is sensitive to outliers — a single extreme value can shift the mean significantly, unlike the median."
    },
    {
        "question": "What is a normal distribution also known as?",
        "options": [
            "Poisson distribution",
            "Uniform distribution",
            "Bell curve",
            "Binomial distribution"
        ],
        "answer": "Bell curve",
        "category": "Statistics & Math",
        "difficulty": "Easy",
        "explanation": "The normal (Gaussian) distribution is symmetric and bell-shaped, characterized by its mean and standard deviation. About 68% of data falls within 1 standard deviation, 95% within 2, and 99.7% within 3 (the empirical rule). It arises naturally from many real-world processes."
    },
    {
        "question": "What does a box plot show?",
        "options": [
            "The relationship between two continuous variables",
            "The frequency of each category",
            "The median, quartiles, and outliers of a numerical variable",
            "The cumulative distribution of a variable"
        ],
        "answer": "The median, quartiles, and outliers of a numerical variable",
        "category": "Statistics & Math",
        "difficulty": "Easy",
        "explanation": "A box plot displays the five-number summary: minimum, Q1 (25th percentile), median (Q2), Q3 (75th percentile), and maximum. Whiskers and dots show the spread and outliers. It is excellent for comparing distributions across groups."
    },
    {
        "question": "What is the difference between Type I and Type II errors?",
        "options": [
            "Type I is underfitting; Type II is overfitting",
            "Type I is a false positive (rejecting a true null hypothesis); Type II is a false negative (failing to reject a false null hypothesis)",
            "Type I occurs during training; Type II occurs during testing",
            "They describe systematic and random measurement errors"
        ],
        "answer": "Type I is a false positive (rejecting a true null hypothesis); Type II is a false negative (failing to reject a false null hypothesis)",
        "category": "Statistics & Math",
        "difficulty": "Medium",
        "explanation": "Type I error (alpha): concluding an effect exists when it does not (false alarm). Type II error (beta): missing a real effect. There is a tradeoff — lowering alpha (stricter threshold) increases beta. Statistical power (1 - beta) measures the ability to detect real effects."
    },
    {
        "question": "What is the interquartile range (IQR)?",
        "options": [
            "The range of the entire dataset (max - min)",
            "The difference between the 75th and 25th percentiles",
            "The standard deviation of the middle 50% of data",
            "The range of the top and bottom 10% of values"
        ],
        "answer": "The difference between the 75th and 25th percentiles",
        "category": "Statistics & Math",
        "difficulty": "Medium",
        "explanation": "IQR = Q3 - Q1, representing the spread of the middle 50% of data. It is robust to outliers and is used to define outlier boundaries (values beyond 1.5 x IQR from Q1 or Q3). It forms the basis of box plot whiskers."
    },
    {
        "question": "What is a confidence interval?",
        "options": [
            "The probability that the null hypothesis is correct",
            "A range of values within which the true population parameter is estimated to fall with a given probability",
            "The standard deviation of the model's predictions",
            "The threshold used to determine statistical significance"
        ],
        "answer": "A range of values within which the true population parameter is estimated to fall with a given probability",
        "category": "Statistics & Math",
        "difficulty": "Medium",
        "explanation": "A 95% confidence interval means that if we repeated the sampling procedure many times, 95% of resulting intervals would contain the true parameter. It does NOT mean there is a 95% chance the parameter is in this specific interval — a common misconception."
    },
    {
        "question": "What is the difference between frequentist and Bayesian statistics?",
        "options": [
            "Frequentists use larger datasets; Bayesians use smaller ones",
            "Frequentists treat probability as long-run frequency; Bayesians treat probability as a degree of belief updated with data",
            "Bayesian statistics is only applicable to continuous distributions",
            "Frequentist methods are always more accurate for prediction"
        ],
        "answer": "Frequentists treat probability as long-run frequency; Bayesians treat probability as a degree of belief updated with data",
        "category": "Statistics & Math",
        "difficulty": "Hard",
        "explanation": "Frequentists define probability as the limiting frequency of events in repeated trials; parameters are fixed unknowns. Bayesians assign probability distributions to parameters and update them with data via Bayes' theorem (posterior proportional to likelihood times prior), incorporating uncertainty and prior knowledge."
    },
    {
        "question": "What is the law of large numbers?",
        "options": [
            "As sample size grows, the variance of each observation decreases",
            "As sample size increases, the sample mean converges to the true population mean",
            "Large datasets always outperform smaller ones in machine learning",
            "Adding more features always improves model performance"
        ],
        "answer": "As sample size increases, the sample mean converges to the true population mean",
        "category": "Statistics & Math",
        "difficulty": "Hard",
        "explanation": "The Law of Large Numbers states that the sample average converges to the population mean as n tends to infinity. It justifies using empirical averages to estimate expectations and underpins Monte Carlo methods, ensemble models, and SGD convergence theory."
    },
    {
        "question": "What does it mean for two variables to be independent in probability theory?",
        "options": [
            "They have zero covariance",
            "Knowing the value of one provides no information about the other; P(A,B) = P(A) * P(B)",
            "They have a correlation of exactly -1 or +1",
            "They were collected from different data sources"
        ],
        "answer": "Knowing the value of one provides no information about the other; P(A,B) = P(A) * P(B)",
        "category": "Statistics & Math",
        "difficulty": "Hard",
        "explanation": "Independence means the joint probability factors into the product of marginals: P(A,B) = P(A) * P(B). Zero correlation implies independence only for normally distributed variables — two variables can be uncorrelated but dependent. Independence is a stronger condition than zero covariance."
    },
    {
        "question": "What is the mode of a dataset?",
        "options": [
            "The average of the highest and lowest values",
            "The middle value when data is sorted",
            "The most frequently occurring value",
            "The sum of all values divided by the count"
        ],
        "answer": "The most frequently occurring value",
        "category": "Statistics & Math",
        "difficulty": "Easy",
        "explanation": "The mode is the value that appears most often in a dataset. A dataset can be unimodal (one mode), bimodal (two modes), or multimodal. Unlike mean and median, the mode can be used with categorical data."
    },
    {
        "question": "What is variance in statistics?",
        "options": [
            "The square root of the standard deviation",
            "The average absolute deviation from the mean",
            "The average of the squared differences from the mean",
            "The difference between the maximum and minimum values"
        ],
        "answer": "The average of the squared differences from the mean",
        "category": "Statistics & Math",
        "difficulty": "Easy",
        "explanation": "Variance measures dispersion by averaging the squared deviations from the mean. Squaring penalizes larger deviations more heavily. Standard deviation is simply the square root of variance, restoring the original units of measurement."
    },
    {
        "question": "What does a Pearson correlation coefficient of 0 indicate?",
        "options": [
            "A perfect negative linear relationship",
            "No linear relationship between the two variables",
            "The variables are perfectly independent",
            "The data has no variance"
        ],
        "answer": "No linear relationship between the two variables",
        "category": "Statistics & Math",
        "difficulty": "Easy",
        "explanation": "Pearson's r ranges from -1 to +1. A value of 0 means no linear relationship exists between the variables. However, a nonlinear relationship may still be present — for example, a quadratic relationship can produce r = 0."
    },
    {
        "question": "What is a scatter plot used for?",
        "options": [
            "Displaying the frequency distribution of one variable",
            "Showing the relationship between two continuous variables",
            "Comparing categories using rectangular bars",
            "Tracking a single variable over time"
        ],
        "answer": "Showing the relationship between two continuous variables",
        "category": "Statistics & Math",
        "difficulty": "Easy",
        "explanation": "A scatter plot places each observation as a point using two axes representing two variables. It helps identify correlation direction, strength, outliers, and nonlinear patterns. Adding a trend line (regression line) summarizes the overall relationship."
    },
    {
        "question": "What is the range of a dataset?",
        "options": [
            "The difference between the maximum and minimum values",
            "The average distance of each point from the mean",
            "The value that appears most frequently",
            "The spread of the middle 50% of observations"
        ],
        "answer": "The difference between the maximum and minimum values",
        "category": "Statistics & Math",
        "difficulty": "Easy",
        "explanation": "Range = max − min. It is the simplest measure of spread but is highly sensitive to outliers since it only considers two extreme values. For a more robust spread measure, use IQR or standard deviation instead."
    },
    {
        "question": "What is a probability distribution?",
        "options": [
            "A list of all possible sample sizes for an experiment",
            "A function describing the likelihood of each possible outcome of a random variable",
            "The cumulative sum of all observed frequencies",
            "A chart showing the correlation between two variables"
        ],
        "answer": "A function describing the likelihood of each possible outcome of a random variable",
        "category": "Statistics & Math",
        "difficulty": "Easy",
        "explanation": "A probability distribution assigns probabilities to all possible outcomes of a random variable. For discrete variables it is a probability mass function (PMF); for continuous variables it is a probability density function (PDF). All probabilities must sum (or integrate) to 1."
    },
    {
        "question": "What is a z-score?",
        "options": [
            "The probability of a value occurring in a normal distribution",
            "The number of standard deviations a data point is from the mean",
            "The ratio of variance to mean",
            "The percentile rank of a value in a dataset"
        ],
        "answer": "The number of standard deviations a data point is from the mean",
        "category": "Statistics & Math",
        "difficulty": "Medium",
        "explanation": "Z = (X − μ) / σ. Z-scores standardize values, allowing comparison across different scales. A z-score of 2 means the value is 2 standard deviations above the mean. Z-scores are used in outlier detection and converting to standard normal probabilities."
    },
    {
        "question": "What is the difference between a population and a sample?",
        "options": [
            "A population is always normally distributed; a sample is not",
            "A population is the entire group of interest; a sample is a subset drawn from it",
            "A sample is always larger than a population",
            "A population refers to people only; a sample can include any data"
        ],
        "answer": "A population is the entire group of interest; a sample is a subset drawn from it",
        "category": "Statistics & Math",
        "difficulty": "Easy",
        "explanation": "Statistical inference uses sample statistics (e.g., sample mean x̄) to estimate population parameters (e.g., population mean μ). Because measuring an entire population is often impractical, representative random sampling allows us to generalize findings with quantified uncertainty."
    },
    {
        "question": "What is a null hypothesis?",
        "options": [
            "The hypothesis that the researcher hopes to prove",
            "A hypothesis assuming no effect or no difference exists",
            "The hypothesis based on prior research findings",
            "A hypothesis that can never be rejected"
        ],
        "answer": "A hypothesis assuming no effect or no difference exists",
        "category": "Statistics & Math",
        "difficulty": "Medium",
        "explanation": "The null hypothesis (H₀) represents the default position — typically that there is no relationship or no difference. Hypothesis testing determines whether there is sufficient evidence to reject H₀ in favor of the alternative hypothesis (H₁). We never 'accept' H₀; we only fail to reject it."
    },
    {
        "question": "What does the coefficient of variation (CV) measure?",
        "options": [
            "The absolute spread of the data",
            "The ratio of standard deviation to the mean, expressing relative variability",
            "The correlation between two variables",
            "The proportion of variance explained by a model"
        ],
        "answer": "The ratio of standard deviation to the mean, expressing relative variability",
        "category": "Statistics & Math",
        "difficulty": "Medium",
        "explanation": "CV = (σ / μ) × 100%. It expresses variability as a percentage of the mean, making it useful for comparing dispersion across datasets with different units or scales — for example, comparing the variability of incomes vs. test scores."
    },
    {
        "question": "What is a uniform distribution?",
        "options": [
            "A distribution where all outcomes are equally likely",
            "A distribution concentrated around a single peak",
            "A distribution skewed heavily to the right",
            "A distribution with two equal peaks"
        ],
        "answer": "A distribution where all outcomes are equally likely",
        "category": "Statistics & Math",
        "difficulty": "Easy",
        "explanation": "In a discrete uniform distribution, each of n outcomes has equal probability 1/n (e.g., rolling a fair die). In a continuous uniform distribution, probability density is constant over an interval [a, b]. It is the maximum-entropy distribution given only bounded support."
    },
    {
        "question": "What is statistical power?",
        "options": [
            "The probability of correctly rejecting a false null hypothesis",
            "The probability of committing a Type I error",
            "The sample size needed for a study",
            "The effect size observed in an experiment"
        ],
        "answer": "The probability of correctly rejecting a false null hypothesis",
        "category": "Statistics & Math",
        "difficulty": "Medium",
        "explanation": "Power = 1 − β, where β is the Type II error rate. It represents the probability of detecting a true effect. Power increases with larger sample size, larger effect size, and higher significance level (alpha). A power of 0.80 is conventionally considered adequate in research."
    },
    {
        "question": "What is skewness in a distribution?",
        "options": [
            "The degree to which a distribution deviates from symmetry",
            "The number of peaks in a distribution",
            "The spread of values around the median",
            "The proportion of outliers in a dataset"
        ],
        "answer": "The degree to which a distribution deviates from symmetry",
        "category": "Statistics & Math",
        "difficulty": "Medium",
        "explanation": "Positive skew (right-skewed): a long tail to the right, mean > median > mode. Negative skew (left-skewed): a long tail to the left, mean < median < mode. Income distributions are typically right-skewed. Skewness is the third standardized moment of a distribution."
    },
    {
        "question": "What is kurtosis?",
        "options": [
            "A measure of the asymmetry of a distribution",
            "A measure of the heaviness of the tails of a distribution relative to a normal distribution",
            "The number of modes in a distribution",
            "The ratio of variance to mean"
        ],
        "answer": "A measure of the heaviness of the tails of a distribution relative to a normal distribution",
        "category": "Statistics & Math",
        "difficulty": "Hard",
        "explanation": "Kurtosis is the fourth standardized moment. High kurtosis (leptokurtic) means heavy tails and a sharp peak — more extreme outliers than a normal distribution. Low kurtosis (platykurtic) means light tails. The normal distribution has kurtosis of 3 (excess kurtosis = 0)."
    },
    {
        "question": "What is a Poisson distribution used to model?",
        "options": [
            "The probability of success in a fixed number of binary trials",
            "The number of events occurring in a fixed interval of time or space",
            "The distribution of sample means from repeated sampling",
            "The probability of a continuous variable exceeding a threshold"
        ],
        "answer": "The number of events occurring in a fixed interval of time or space",
        "category": "Statistics & Math",
        "difficulty": "Medium",
        "explanation": "The Poisson distribution models counts of rare, independent events in a fixed interval — e.g., customer arrivals per hour, typos per page, or server requests per second. It is parameterized by λ (the average rate), and both its mean and variance equal λ."
    },
    {
        "question": "What is the binomial distribution?",
        "options": [
            "A distribution for continuous outcomes with two parameters",
            "A distribution for the number of successes in n independent Bernoulli trials",
            "A distribution describing time between events",
            "A symmetric distribution with infinite support"
        ],
        "answer": "A distribution for the number of successes in n independent Bernoulli trials",
        "category": "Statistics & Math",
        "difficulty": "Medium",
        "explanation": "The binomial distribution models the number of successes k in n independent trials each with success probability p. Its mean is np and variance is np(1−p). The coin-flip experiment is the canonical example. As n grows large, it approximates a normal distribution."
    },
    {
        "question": "What is the expected value of a random variable?",
        "options": [
            "The most probable outcome of the variable",
            "The weighted average of all possible outcomes, weighted by their probabilities",
            "The median of the variable's distribution",
            "The outcome that minimizes the variance"
        ],
        "answer": "The weighted average of all possible outcomes, weighted by their probabilities",
        "category": "Statistics & Math",
        "difficulty": "Medium",
        "explanation": "E[X] = Σ x · P(X=x) for discrete variables. It represents the long-run average outcome if the experiment were repeated many times. Expected value is linear: E[aX + b] = aE[X] + b, a property widely used in statistics and decision theory."
    },
    {
        "question": "What is a chi-squared test used for?",
        "options": [
            "Comparing means of two continuous variables",
            "Testing whether observed categorical frequencies match expected frequencies",
            "Measuring the correlation between two continuous variables",
            "Estimating the parameters of a regression model"
        ],
        "answer": "Testing whether observed categorical frequencies match expected frequencies",
        "category": "Statistics & Math",
        "difficulty": "Medium",
        "explanation": "The chi-squared (χ²) test compares observed vs. expected counts in categorical data. The goodness-of-fit test checks if one variable matches a distribution; the test of independence checks if two categorical variables are related. The test statistic follows a chi-squared distribution under H₀."
    },
    {
        "question": "What is linear regression used to model?",
        "options": [
            "The probability that a binary outcome equals 1",
            "The linear relationship between a dependent variable and one or more independent variables",
            "The clustering structure of unlabeled data",
            "The conditional probability distribution of class labels"
        ],
        "answer": "The linear relationship between a dependent variable and one or more independent variables",
        "category": "Statistics & Math",
        "difficulty": "Easy",
        "explanation": "Linear regression fits a line (or hyperplane) y = β₀ + β₁x₁ + ... + βₙxₙ + ε that minimizes the sum of squared residuals (OLS). It assumes linearity, independence, homoscedasticity, and normality of errors. The coefficients represent the change in y per unit change in each x."
    },
    {
        "question": "What does R-squared (R²) measure in regression?",
        "options": [
            "The correlation between the residuals and the fitted values",
            "The proportion of variance in the dependent variable explained by the model",
            "The average squared prediction error",
            "The significance level of the regression coefficients"
        ],
        "answer": "The proportion of variance in the dependent variable explained by the model",
        "category": "Statistics & Math",
        "difficulty": "Medium",
        "explanation": "R² ranges from 0 to 1. R² = 1 means the model explains all variance; R² = 0 means none. Adding predictors always increases R², which is why adjusted R² penalizes unnecessary variables. A high R² does not guarantee good out-of-sample prediction."
    },
    {
        "question": "What is multicollinearity in regression?",
        "options": [
            "The condition where the residuals are not normally distributed",
            "The condition where independent variables are highly correlated with each other",
            "When the dependent variable has more than two categories",
            "When the regression line does not pass through the origin"
        ],
        "answer": "The condition where independent variables are highly correlated with each other",
        "category": "Statistics & Math",
        "difficulty": "Hard",
        "explanation": "Multicollinearity inflates the variance of regression coefficients, making them unstable and difficult to interpret. It is detected using Variance Inflation Factor (VIF); VIF > 10 is typically concerning. Solutions include removing correlated features, PCA, or regularization (Ridge regression)."
    },
    {
        "question": "What is heteroscedasticity in regression?",
        "options": [
            "A condition where the independent variables are correlated",
            "A condition where the variance of residuals changes across values of the independent variable",
            "A situation where the regression model is nonlinear",
            "When multiple regression lines are fit to the same data"
        ],
        "answer": "A condition where the variance of residuals changes across values of the independent variable",
        "category": "Statistics & Math",
        "difficulty": "Hard",
        "explanation": "Ordinary least squares (OLS) assumes homoscedasticity — constant residual variance. Heteroscedasticity violates this, making standard errors unreliable. It is detected with residual plots or Breusch-Pagan test. Fixes include log-transforming the target, weighted least squares, or robust standard errors."
    },
    {
        "question": "What is the exponential distribution used to model?",
        "options": [
            "The number of events in a fixed time interval",
            "The time between consecutive events in a Poisson process",
            "The probability of exactly k successes in n trials",
            "The distribution of sample variances"
        ],
        "answer": "The time between consecutive events in a Poisson process",
        "category": "Statistics & Math",
        "difficulty": "Hard",
        "explanation": "The exponential distribution models waiting times between Poisson events — e.g., time between customer arrivals or server failures. It is memoryless: P(T > s + t | T > s) = P(T > t). Its mean is 1/λ and variance is 1/λ², where λ is the Poisson rate."
    },
    {
        "question": "What is a t-test used for?",
        "options": [
            "Comparing the variances of three or more groups",
            "Testing whether the means of one or two groups are significantly different",
            "Measuring the association between two categorical variables",
            "Determining whether a distribution is normal"
        ],
        "answer": "Testing whether the means of one or two groups are significantly different",
        "category": "Statistics & Math",
        "difficulty": "Medium",
        "explanation": "A one-sample t-test compares a sample mean to a known value. An independent two-sample t-test compares means of two groups. A paired t-test handles matched pairs. The t-statistic = (x̄ − μ₀) / (s / √n). It is robust for moderate sample sizes even with non-normal data."
    },
    {
        "question": "What is ANOVA used for?",
        "options": [
            "Testing the difference in variances between two groups",
            "Comparing means across three or more groups simultaneously",
            "Fitting a nonlinear model to data",
            "Estimating the correlation between continuous variables"
        ],
        "answer": "Comparing means across three or more groups simultaneously",
        "category": "Statistics & Math",
        "difficulty": "Medium",
        "explanation": "Analysis of Variance (ANOVA) partitions total variance into between-group and within-group components. The F-statistic = (between-group variance) / (within-group variance). If F is large, group means differ significantly. ANOVA assumes normality, independence, and equal variances (homoscedasticity)."
    },
    {
        "question": "What is the difference between parametric and non-parametric tests?",
        "options": [
            "Parametric tests use raw data; non-parametric tests use only ranks",
            "Parametric tests assume a specific population distribution; non-parametric tests do not",
            "Non-parametric tests are always more powerful than parametric tests",
            "Parametric tests are used for categorical data; non-parametric for continuous data"
        ],
        "answer": "Parametric tests assume a specific population distribution; non-parametric tests do not",
        "category": "Statistics & Math",
        "difficulty": "Medium",
        "explanation": "Parametric tests (t-test, ANOVA) assume the data follows a known distribution (typically normal) and use distributional parameters. Non-parametric tests (Mann-Whitney, Kruskal-Wallis) make fewer assumptions and work on ranks — preferable for small samples or clearly non-normal data."
    },
    {
        "question": "What is the geometric mean used for?",
        "options": [
            "Averaging values that are additive in nature",
            "Averaging values that are multiplicative or vary over several orders of magnitude",
            "Finding the central value in a sorted distribution",
            "Measuring the spread of a dataset"
        ],
        "answer": "Averaging values that are multiplicative or vary over several orders of magnitude",
        "category": "Statistics & Math",
        "difficulty": "Medium",
        "explanation": "The geometric mean = (x₁ × x₂ × ... × xₙ)^(1/n). It is appropriate for growth rates, financial returns, and ratios. For example, if an investment grows by 10% then −10%, the arithmetic mean return is 0%, but the geometric mean correctly reflects a net loss."
    },
    {
        "question": "What is the harmonic mean?",
        "options": [
            "The middle value in a sorted dataset",
            "The reciprocal of the arithmetic mean of the reciprocals of the values",
            "The geometric average of the maximum and minimum values",
            "The weighted sum of all values divided by the total weight"
        ],
        "answer": "The reciprocal of the arithmetic mean of the reciprocals of the values",
        "category": "Statistics & Math",
        "difficulty": "Hard",
        "explanation": "H = n / (1/x₁ + 1/x₂ + ... + 1/xₙ). The harmonic mean is most appropriate when averaging rates or ratios — for example, average speed when traveling equal distances. It is always ≤ geometric mean ≤ arithmetic mean (AM-GM-HM inequality)."
    },
    {
        "question": "What is a kernel density estimate (KDE)?",
        "options": [
            "A parametric model fitted to a dataset",
            "A non-parametric method for estimating the probability density function of a variable",
            "The histogram of a variable with optimally sized bins",
            "A method for reducing dimensionality of data"
        ],
        "answer": "A non-parametric method for estimating the probability density function of a variable",
        "category": "Statistics & Math",
        "difficulty": "Hard",
        "explanation": "KDE places a smooth kernel function (commonly Gaussian) at each data point and sums them to create a continuous density estimate. Bandwidth controls smoothness — too small gives noisy estimates; too large over-smooths. KDE avoids the arbitrary bin-width choice of histograms."
    },
    {
        "question": "What does the empirical rule (68-95-99.7 rule) state?",
        "options": [
            "68%, 95%, and 99.7% of data fall within 1, 2, and 3 standard deviations of the median",
            "68%, 95%, and 99.7% of data fall within 1, 2, and 3 standard deviations of the mean in a normal distribution",
            "68% of all distributions are approximately normal",
            "95% of confidence intervals contain the true parameter"
        ],
        "answer": "68%, 95%, and 99.7% of data fall within 1, 2, and 3 standard deviations of the mean in a normal distribution",
        "category": "Statistics & Math",
        "difficulty": "Easy",
        "explanation": "For a normal distribution: ~68% of observations lie within μ ± σ, ~95% within μ ± 2σ, and ~99.7% within μ ± 3σ. This rule is used to quickly assess how unusual an observation is and underpins the concept of z-scores and outlier detection."
    },
    {
        "question": "What is a Q-Q plot used for?",
        "options": [
            "Comparing the means of two datasets visually",
            "Assessing whether a dataset follows a specified theoretical distribution",
            "Plotting quantiles of the dependent variable against the independent variable",
            "Visualizing the cumulative frequency of a dataset"
        ],
        "answer": "Assessing whether a dataset follows a specified theoretical distribution",
        "category": "Statistics & Math",
        "difficulty": "Medium",
        "explanation": "A Q-Q (quantile-quantile) plot compares the quantiles of sample data against the quantiles of a theoretical distribution (commonly normal). If the points fall along a straight diagonal line, the data fits the distribution well. Deviations indicate skewness, heavy tails, or other departures."
    },
    {
        "question": "What is covariance?",
        "options": [
            "A normalized measure of the linear relationship between two variables, bounded between -1 and 1",
            "A measure of how much two variables change together",
            "The average squared deviation of a single variable from its mean",
            "The ratio of variance of one variable to another"
        ],
        "answer": "A measure of how much two variables change together",
        "category": "Statistics & Math",
        "difficulty": "Medium",
        "explanation": "Cov(X, Y) = E[(X − μₓ)(Y − μᵧ)]. Positive covariance means variables tend to increase together; negative means one increases as the other decreases. Covariance magnitude depends on the scale of the variables, making direct comparisons difficult — Pearson correlation normalizes it to [-1, 1]."
    },
    {
        "question": "What is Spearman's rank correlation?",
        "options": [
            "A measure of the linear association between two continuous normally distributed variables",
            "A non-parametric measure of monotonic association between two variables based on their ranks",
            "A method for comparing the variances of two distributions",
            "The correlation between residuals and fitted values in regression"
        ],
        "answer": "A non-parametric measure of monotonic association between two variables based on their ranks",
        "category": "Statistics & Math",
        "difficulty": "Hard",
        "explanation": "Spearman's ρ converts each variable to ranks and computes the Pearson correlation of those ranks. It captures monotonic (not just linear) relationships and is robust to outliers. Values range from -1 to +1. It is the non-parametric counterpart of Pearson's r."
    },
    {
        "question": "What is a sampling distribution?",
        "options": [
            "The distribution of raw data points in a sample",
            "The probability distribution of a statistic computed from repeated random samples",
            "The distribution of residuals in a regression model",
            "A distribution used only for sampling without replacement"
        ],
        "answer": "The probability distribution of a statistic computed from repeated random samples",
        "category": "Statistics & Math",
        "difficulty": "Hard",
        "explanation": "If you repeatedly draw samples of size n and compute the sample mean each time, those means form the sampling distribution of the mean. Its standard deviation is σ/√n (the standard error). The Central Limit Theorem describes the shape of this distribution as n increases."
    },
    {
        "question": "What is the standard error (SE) of the mean?",
        "options": [
            "The standard deviation of the original population",
            "The average deviation of predictions from the actual values",
            "The standard deviation of the sampling distribution of the mean",
            "The error introduced by using a biased estimator"
        ],
        "answer": "The standard deviation of the sampling distribution of the mean",
        "category": "Statistics & Math",
        "difficulty": "Medium",
        "explanation": "SE = σ / √n. The standard error quantifies the variability of the sample mean across repeated samples. It decreases as sample size increases, meaning larger samples yield more precise estimates. SE is used to construct confidence intervals and t-statistics."
    },
    {
        "question": "What does it mean for an estimator to be unbiased?",
        "options": [
            "It always equals the true parameter",
            "Its expected value equals the true population parameter",
            "It has the smallest variance among all estimators",
            "It is computed without any assumptions about the population"
        ],
        "answer": "Its expected value equals the true population parameter",
        "category": "Statistics & Math",
        "difficulty": "Hard",
        "explanation": "An estimator θ̂ is unbiased if E[θ̂] = θ. For example, the sample mean is an unbiased estimator of the population mean. The sample variance using n−1 (Bessel's correction) is unbiased; dividing by n gives a biased estimator that underestimates σ². Unbiasedness alone does not guarantee an estimator is good — efficiency (low variance) also matters."
    },
    {
        "question": "What is the purpose of bootstrapping in statistics?",
        "options": [
            "To initialize neural network weights before training",
            "To estimate the sampling distribution of a statistic by resampling with replacement from the data",
            "To fill missing values by replicating observed values",
            "To reduce overfitting by training on random subsets of features"
        ],
        "answer": "To estimate the sampling distribution of a statistic by resampling with replacement from the data",
        "category": "Statistics & Math",
        "difficulty": "Hard",
        "explanation": "Bootstrapping repeatedly draws samples of size n with replacement from the original data, computes the statistic of interest each time, and uses the resulting empirical distribution to estimate confidence intervals and standard errors — without assuming a parametric distribution. It is widely used when analytical formulas are unavailable."
    },
    {
        "question": "What is the difference between descriptive and inferential statistics?",
        "options": [
            "Descriptive statistics use graphs; inferential statistics use numbers",
            "Descriptive statistics summarize observed data; inferential statistics draw conclusions about a population from a sample",
            "Inferential statistics only apply to normally distributed data",
            "Descriptive statistics require large datasets; inferential statistics work on small ones"
        ],
        "answer": "Descriptive statistics summarize observed data; inferential statistics draw conclusions about a population from a sample",
        "category": "Statistics & Math",
        "difficulty": "Easy",
        "explanation": "Descriptive statistics (mean, median, standard deviation, charts) summarize what the data shows. Inferential statistics (hypothesis tests, confidence intervals, regression) use sample data to make generalizations about a larger population, always with some degree of uncertainty."
    },
    {
        "question": "What is a log-normal distribution?",
        "options": [
            "A distribution whose logarithm is uniformly distributed",
            "A distribution where the logarithm of the variable is normally distributed",
            "A normal distribution plotted on a logarithmic axis",
            "A distribution with a constant hazard rate"
        ],
        "answer": "A distribution where the logarithm of the variable is normally distributed",
        "category": "Statistics & Math",
        "difficulty": "Hard",
        "explanation": "If ln(X) ~ Normal(μ, σ²), then X follows a log-normal distribution. It is always positive and right-skewed, modeling quantities like income, stock prices, and biological measurements that arise from multiplicative processes. Log-transforming the variable produces a symmetric, normally distributed result."
    },
    {
        "question": "What is the F-distribution used for?",
        "options": [
            "Modeling time-to-event data",
            "Comparing the variances of two populations or testing multiple regression coefficients simultaneously",
            "Estimating the mean of a normally distributed population",
            "Modeling the number of successes in a sequence of trials"
        ],
        "answer": "Comparing the variances of two populations or testing multiple regression coefficients simultaneously",
        "category": "Statistics & Math",
        "difficulty": "Hard",
        "explanation": "The F-distribution arises as the ratio of two chi-squared variables divided by their degrees of freedom. It is used in the F-test for equality of variances and in ANOVA and regression analysis to test whether group means or regression coefficients are jointly significant."
    },
    {
        "question": "What is a residual in regression analysis?",
        "options": [
            "The coefficient assigned to an independent variable",
            "The difference between the observed value and the model's predicted value",
            "The portion of variance explained by the regression model",
            "The intercept term in the regression equation"
        ],
        "answer": "The difference between the observed value and the model's predicted value",
        "category": "Statistics & Math",
        "difficulty": "Easy",
        "explanation": "Residual eᵢ = yᵢ − ŷᵢ. Residuals represent the unexplained variation in the dependent variable. Analyzing residual plots is essential for diagnosing model assumptions: patterns suggest nonlinearity, changing spread suggests heteroscedasticity, and outliers may indicate influential points."
    },
    {
        "question": "What is maximum likelihood estimation (MLE)?",
        "options": [
            "Minimizing the sum of squared residuals between predicted and actual values",
            "Finding the parameter values that maximize the probability of observing the given data",
            "Selecting the model with the highest accuracy on a validation set",
            "Estimating missing values using the most probable class"
        ],
        "answer": "Finding the parameter values that maximize the probability of observing the given data",
        "category": "Statistics & Math",
        "difficulty": "Hard",
        "explanation": "MLE finds θ̂ = argmax L(θ|data), where L is the likelihood function. In practice, the log-likelihood is maximized for numerical convenience. MLE is consistent and asymptotically efficient. For normally distributed errors, MLE is equivalent to ordinary least squares regression."
    }
]
