# Processed Datasets

This directory contains the processed datasets used in the experiments comparing normal prompting vs test-driven prompting approaches.

## Dataset Structure

Each dataset contains specific columns used for the experimental evaluation:

### Code Contests Dataset

| Prompting Type | Columns Used |
|---|---|
| **Normal Prompt** | `task_id`, `test`, `context`, `prompt` |
| **Test-Driven Prompt** | `task_id`, `test`, `context`, `test_public` |

### HumanEval Dataset

| Prompting Type | Columns Used |
|---|---|
| **Normal Prompt** | `task_id`, `test`, `prompt` |
| **Test-Driven Prompt** | `task_id`, `test`, `prompt`, `test_public` |

### MBPP Dataset

| Prompting Type | Columns Used |
|---|---|
| **Normal Prompt** | `task_id`, `test`, `prompt` |
| **Test-Driven Prompt** | `task_id`, `test`, `prompt`, `test_public` |

## Column Descriptions

- **`task_id`**: Unique identifier for each programming task
- **`test`**: Complete test suite for evaluation
- **`prompt`**: Problem description and requirements
- **`context`**: Additional context information (Code Contests only)
- **`test_public`**: Subset of test cases provided to the model in test-driven prompting