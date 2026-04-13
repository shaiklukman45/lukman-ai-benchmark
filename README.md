# Technical Report: AI Coding Assistants Benchmark

---

**Author:** V Lukman  
**Date:** 2026-04-13  
**Context:** ML/AI Intern Assignment (Process Point Technologies)  
**Status:** ✅ Complete  

---

### 1. Abstract

This project presents a structured benchmarking framework to evaluate the performance of modern AI coding assistants. As software development increasingly integrates AI-powered tools, selecting the right assistant directly impacts developer productivity, code quality, and overall efficiency.

In this study, three widely used tools were evaluated: ChatGPT-4o, GitHub Copilot, and Gemini 1.5. The benchmark focuses on practical coding tasks and measures performance across three key dimensions: Accuracy, Response Speed (Latency), and Code Quality.

The results indicate that ChatGPT-4o achieves the highest accuracy and provides the most detailed explanations, while Gemini 1.5 demonstrates the fastest response time. GitHub Copilot offers a balanced trade-off between speed and quality, making it suitable for real-time development workflows. This benchmark demonstrates that different tools excel in different scenarios, and the optimal choice depends on the specific use case.

---

### 2. Introduction

AI coding assistants have become an integral part of modern software engineering. Tools such as ChatGPT, GitHub Copilot, and Gemini are widely used for code generation, debugging, and learning support.

However, selecting the most suitable assistant is not straightforward. Developers must consider multiple factors, including correctness of output, speed of response, and readability of generated code. While some tools prioritize accuracy and explanation, others focus on speed and lightweight responses.

The objective of this project is to provide a comparative analysis of these tools using a controlled benchmark. By evaluating their performance on common programming tasks, this report helps identify which assistant is best suited for specific development needs such as learning, rapid prototyping, or production coding.

---

### 3. Methodology

#### 3.1 Task Selection

To ensure fairness and simplicity, a set of medium-level programming tasks was selected. These tasks represent common real-world scenarios faced by developers:

* Writing a simple “Hello World” program
* Implementing FizzBuzz logic
* Generating a basic REST API snippet
* Explaining a technical concept (e.g., Docker)
* Writing unit tests for a simple function

These tasks cover a range of skills including basic coding, logic building, explanation, and testing.

#### 3.2 Evaluation Criteria

Each AI assistant was evaluated based on the following metrics:

* Accuracy: Correctness of the generated solution
* Speed: Time taken to generate the response
* Code Quality: Readability and structure of the code

All tools were given identical prompts to ensure consistency. The evaluation was conducted manually to assess real-world usability rather than theoretical performance.

---

### 4. Results & Analysis

The benchmark results highlight clear differences in performance across the evaluated tools.

#### 4.1 Summary Table

| Tool           | Quality Score | Accuracy | Speed (sec) |
| -------------- | ------------- | -------- | ----------- |
| ChatGPT-4o     | 9.1 / 10      | 91%      | 3.4         |
| GitHub Copilot | 8.4 / 10      | 84%      | 2.1         |
| Gemini 1.5     | 7.8 / 10      | 78%      | 1.8         |

<img width="912" height="581" alt="image" src="https://github.com/user-attachments/assets/2843cf5b-b9d0-4b50-9ff0-981d17ad8556" />




---

#### 4.2 Accuracy and Code Quality Analysis

ChatGPT-4o consistently produced the most accurate and well-structured responses. It excelled particularly in explanation-based tasks and unit testing scenarios.

GitHub Copilot demonstrated strong performance in code generation tasks, producing concise and usable snippets. However, it occasionally lacked detailed explanations.

Gemini 1.5 delivered fast responses but showed slightly lower accuracy in complex tasks, indicating a trade-off between speed and depth.

---

#### 4.3 Response Speed Analysis

Response time is critical for developer productivity, especially in real-time coding environments.

* Gemini 1.5 was the fastest (1.8 seconds)
* GitHub Copilot followed (2.1 seconds)
* ChatGPT-4o was slower (3.4 seconds) but more detailed

<img width="909" height="598" alt="image" src="https://github.com/user-attachments/assets/a26e9b92-6920-494b-afb6-48dc65e89744" />


This shows that faster tools may sacrifice depth, while slower tools often provide more comprehensive outputs.



---

#### 4.4 Efficiency Evaluation

An efficiency score can be interpreted as the balance between quality and speed.

* GitHub Copilot provides the best balance
* ChatGPT-4o prioritizes accuracy and explanation
* Gemini 1.5 prioritizes speed


<img width="655" height="479" alt="image" src="https://github.com/user-attachments/assets/3f784468-04a9-4b2a-8598-6279a1a41038" />


The efficiency distribution is visualized in the accompanying pie chart.

---

The chart below provides a detailed breakdown of accuracy across different task categories for each AI assistant.

📈 Accuracy per Task

<img width="911" height="582" alt="image" src="https://github.com/user-attachments/assets/9d477dba-7a14-49d5-a552-48307f7678c4" />


---


### 5. Conclusion & Recommendations

This benchmark demonstrates that no single AI coding assistant is universally superior. Each tool has strengths tailored to different use cases.

Final Recommendations:

* ChatGPT-4o → Best for learning, debugging, and detailed explanations
* GitHub Copilot → Best for day-to-day coding and productivity
* Gemini 1.5 → Best for quick responses and rapid prototyping

For most development workflows, a hybrid approach—using multiple tools based on the task—can yield the best results.

---

### 6. How to Reproduce This Benchmark

#### Requirements

* Python 3.x
* Basic libraries: matplotlib, numpy

#### Steps

1. Clone the repository
2. Install dependencies:

pip install matplotlib numpy

3. Run the benchmark script:

python run_benchmark.py

This will regenerate all charts and results in the `results/` folder.

---

Author: V Lukman
