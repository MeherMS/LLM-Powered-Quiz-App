QUESTIONS = [
    # ─────────────────────────────────────────
    # MACHINE LEARNING — Easy
    # ─────────────────────────────────────────
    {
        "question": "Which algorithm is best suited for binary classification?",
        "options": ["K-Means", "Linear Regression", "Logistic Regression", "PCA"],
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
        "options": ["Decision Tree", "K-Means Clustering", "Random Forest", "Support Vector Machine"],
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

    # MACHINE LEARNING — Medium
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
        "options": ["Boosting", "Regularization", "Normalization", "Bootstrapping"],
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

    # MACHINE LEARNING — Hard
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

    # ─────────────────────────────────────────
    # DEEP LEARNING — Easy
    # ─────────────────────────────────────────
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
        "options": ["Underfitting", "Slow training", "Overfitting", "Vanishing gradients"],
        "answer": "Overfitting",
        "category": "Deep Learning",
        "difficulty": "Easy",
        "explanation": "Dropout randomly sets a fraction of neurons to zero during each training step, preventing neurons from co-adapting and forcing the network to learn more robust, redundant representations — acting as an ensemble of many sub-networks."
    },

    # DEEP LEARNING — Medium
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

    # DEEP LEARNING — Hard
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

    # ─────────────────────────────────────────
    # AI & NLP — Easy
    # ─────────────────────────────────────────
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

    # AI & NLP — Medium
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

    # AI & NLP — Hard
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
        "explanation": "In self-attention, the input is projected into Queries (what we're looking for), Keys (what each position offers), and Values (what to return). Attention scores are computed as softmax(QK^T / √d_k) × V, allowing dynamic focus on relevant positions."
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

    # ─────────────────────────────────────────
    # MODEL EVALUATION — Easy
    # ─────────────────────────────────────────
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

    # MODEL EVALUATION — Medium
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

    # MODEL EVALUATION — Hard
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

    # ─────────────────────────────────────────
    # DATA SCIENCE & STATISTICS — Easy
    # ─────────────────────────────────────────
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
        "options": ["Bar chart", "Scatter plot", "Histogram", "Line chart"],
        "answer": "Histogram",
        "category": "Statistics & Math",
        "difficulty": "Easy",
        "explanation": "A histogram divides a numerical variable into bins and shows the frequency of values in each bin, revealing shape (normal, skewed, bimodal), spread, and outliers of the distribution."
    },

    # DATA SCIENCE & STATISTICS — Medium
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

    # DATA SCIENCE & STATISTICS — Hard
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

    # ─────────────────────────────────────────
    # DATA ENGINEERING — Easy
    # ─────────────────────────────────────────
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

    # DATA ENGINEERING — Medium
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

    # DATA ENGINEERING — Hard
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

    # ─────────────────────────────────────────
    # GENERATIVE AI — Medium
    # ─────────────────────────────────────────
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

    # GENERATIVE AI — Hard
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

    # ─────────────────────────────────────────
    # MLOPS — Medium
    # ─────────────────────────────────────────
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

    # MLOps — Hard
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

    # ─────────────────────────────────────────
    # COMPUTER VISION — Medium
    # ─────────────────────────────────────────
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

    # ─────────────────────────────────────────
    # REINFORCEMENT LEARNING — Medium / Hard
    # ─────────────────────────────────────────
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
]
