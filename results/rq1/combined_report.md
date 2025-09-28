# Combined Analysis Report

Generated: 2025-09-21 09:48:06

**LLMs:** Multiple (8 models) | **Research Question:** rq2

## Summary (First Attempt Only)

Total comparisons: 16

* Test-driven (TD) results were better in 16 out of 16 comparisons (100.0%)
* Test-driven (TD) results were same in 0 out of 16 comparisons (0.0%)
* Test-driven (TD) results were worse in 0 out of 16 comparisons (0.0%)

### Accuracy Statistics

* Total increase: 123.80
* Average increase: 7.74 (95% CI: [6.30, 9.18])
* Median increase: 8.18
* Standard deviation: 2.70
* Range: 3.05 to 13.35
* Interquartile range: 6.10 to 9.37
* Benchmarks improved: 16 (100.0%)
* Benchmarks worsened: 0 (0.0%)
* Benchmarks unchanged: 0 (0.0%)
* Average improvement percentage: 10.63%

#### Statistical Tests

* **Normality Test (Shapiro-Wilk)**: statistic=0.9772, p-value=0.9372, Normal=Yes
* **Paired t-test**: statistic=11.4529, p-value=0.0000
* **Effect Size (Cohen's d)**: 1.8349 (large effect)
* **Interpretation**: Results are highly significant (p < 0.001)

#### Top 5 Increases

* mbpp_sanitized_chatgpt4o_combined: 72.83 → 86.18 (change: +13.35)
* mbpp_sanitized_claude35sonnet_combined: 75.41 → 85.95 (change: +10.54)
* mbpp_sanitized_qwen25coder32b_combined: 73.07 → 83.37 (change: +10.30)
* mbpp_sanitized_claude35haiku_combined: 75.64 → 85.01 (change: +9.37)
* mbpp_sanitized_qwen25coder14b_combined: 73.07 → 82.44 (change: +9.37)

#### Top 5 Regressions

* human_eval_qwen25coder7b_combined: 71.34 → 74.39 (change: +3.05)
* human_eval_qwen25coder3b_combined: 69.51 → 73.17 (change: +3.66)
* human_eval_chatgpt4omini_combined: 73.17 → 78.05 (change: +4.88)
* human_eval_chatgpt4o_combined: 74.39 → 80.49 (change: +6.10)
* human_eval_claude35sonnet_combined: 78.66 → 84.76 (change: +6.10)

## Summary (With Remediation)

Total comparisons: 16

* Test-driven (TD) results were better in 15 out of 16 comparisons (93.8%)
* Test-driven (TD) results were same in 1 out of 16 comparisons (6.2%)
* Test-driven (TD) results were worse in 0 out of 16 comparisons (0.0%)

### Accuracy Statistics (With Remediation)

* Total increase: 68.11
* Average increase: 4.26 (95% CI: [2.76, 5.75])
* Median increase: 3.35
* Standard deviation: 2.81
* Range: 0.00 to 9.61
* Interquartile range: 2.72 to 6.09
* Benchmarks improved: 15 (93.8%)
* Benchmarks worsened: 0 (0.0%)
* Benchmarks unchanged: 1 (6.2%)
* Average improvement percentage: 5.99%

#### Statistical Tests

* **Normality Test (Shapiro-Wilk)**: statistic=0.9358, p-value=0.3005, Normal=Yes
* **Paired t-test**: statistic=6.0609, p-value=0.0000
* **Effect Size (Cohen's d)**: 0.5205 (medium effect)
* **Interpretation**: Results are highly significant (p < 0.001)

#### Top 5 Increases (With Remediation)

* mbpp_sanitized_qwen25coder7b_combined: 68.38 → 77.99 (change: +9.61)
* human_eval_qwen25coder14b_combined: 74.39 → 82.93 (change: +8.54)
* mbpp_sanitized_qwen25coder14b_combined: 74.94 → 83.37 (change: +8.43)
* human_eval_qwen25coder32b_combined: 80.49 → 86.59 (change: +6.10)
* mbpp_sanitized_qwen25coder3b_combined: 63.47 → 69.56 (change: +6.09)

#### Top 5 Regressions (With Remediation)

* mbpp_sanitized_claude35haiku_combined: 91.10 → 91.10 (change: +0.00)
* human_eval_chatgpt4omini_combined: 81.71 → 82.93 (change: +1.22)
* mbpp_sanitized_claude35sonnet_combined: 92.74 → 94.15 (change: +1.41)
* human_eval_claude35sonnet_combined: 89.63 → 92.07 (change: +2.44)
* mbpp_sanitized_chatgpt4o_combined: 88.29 → 91.10 (change: +2.81)

## Detailed Comparisons (First Attempt Only)

### human_eval_chatgpt4o_combined vs human_eval_chatgpt4o_combined_td

Accuracy comparison: **TD is better** - 80.49 vs 74.39

Test counts:
* Base: {'success': 122, 'fail': 38, 'error': 4, 'generation_errors': 0, 'test_errors': 4}
* TD: {'success': 132, 'fail': 29, 'error': 3, 'generation_errors': 0, 'test_errors': 3}
* Difference: {'success': 10, 'fail': -9, 'error': -1, 'generation_errors': 0, 'test_errors': -1}

**Improvements** - Tests that passed in TD but failed/errored in Base:
* task_id: 3
* task_id: 6
* task_id: 14
* task_id: 26
* task_id: 41
* task_id: 68
* task_id: 70
* task_id: 71
* task_id: 72
* task_id: 77
* task_id: 79
* task_id: 81
* task_id: 102
* task_id: 113
* task_id: 120
* task_id: 135

**Regressions** - Tests that passed in Base but failed/errored in TD:
* task_id: 1
* task_id: 10
* task_id: 91
* task_id: 101
* task_id: 109
* task_id: 140

---

### human_eval_chatgpt4omini_combined vs human_eval_chatgpt4omini_combined_td

Accuracy comparison: **TD is better** - 78.05 vs 73.17

Test counts:
* Base: {'success': 120, 'fail': 37, 'error': 7, 'generation_errors': 0, 'test_errors': 7}
* TD: {'success': 128, 'fail': 33, 'error': 3, 'generation_errors': 0, 'test_errors': 3}
* Difference: {'success': 8, 'fail': -4, 'error': -4, 'generation_errors': 0, 'test_errors': -4}

**Improvements** - Tests that passed in TD but failed/errored in Base:
* task_id: 2
* task_id: 41
* task_id: 68
* task_id: 70
* task_id: 71
* task_id: 76
* task_id: 77
* task_id: 79
* task_id: 83
* task_id: 101
* task_id: 109
* task_id: 113

**Regressions** - Tests that passed in Base but failed/errored in TD:
* task_id: 10
* task_id: 105
* task_id: 137
* task_id: 140

---

### human_eval_claude35haiku_combined vs human_eval_claude35haiku_combined_td

Accuracy comparison: **TD is better** - 81.71 vs 73.78

Test counts:
* Base: {'success': 121, 'fail': 37, 'error': 6, 'generation_errors': 0, 'test_errors': 6}
* TD: {'success': 134, 'fail': 28, 'error': 2, 'generation_errors': 0, 'test_errors': 2}
* Difference: {'success': 13, 'fail': -9, 'error': -4, 'generation_errors': 0, 'test_errors': -4}

**Improvements** - Tests that passed in TD but failed/errored in Base:
* task_id: 46
* task_id: 54
* task_id: 65
* task_id: 68
* task_id: 71
* task_id: 75
* task_id: 77
* task_id: 79
* task_id: 88
* task_id: 108
* task_id: 113
* task_id: 115
* task_id: 120
* task_id: 136
* task_id: 138
* task_id: 151
* task_id: 154

**Regressions** - Tests that passed in Base but failed/errored in TD:
* task_id: 116
* task_id: 118
* task_id: 130
* task_id: 153

---

### human_eval_claude35sonnet_combined vs human_eval_claude35sonnet_combined_td

Accuracy comparison: **TD is better** - 84.76 vs 78.66

Test counts:
* Base: {'success': 129, 'fail': 32, 'error': 3, 'generation_errors': 0, 'test_errors': 3}
* TD: {'success': 139, 'fail': 23, 'error': 2, 'generation_errors': 0, 'test_errors': 2}
* Difference: {'success': 10, 'fail': -9, 'error': -1, 'generation_errors': 0, 'test_errors': -1}

**Improvements** - Tests that passed in TD but failed/errored in Base:
* task_id: 3
* task_id: 68
* task_id: 70
* task_id: 71
* task_id: 77
* task_id: 79
* task_id: 83
* task_id: 93
* task_id: 113
* task_id: 115
* task_id: 136
* task_id: 137
* task_id: 140
* task_id: 163

**Regressions** - Tests that passed in Base but failed/errored in TD:
* task_id: 103
* task_id: 111
* task_id: 135
* task_id: 160

---

### human_eval_qwen25coder14b_combined vs human_eval_qwen25coder14b_combined_td

Accuracy comparison: **TD is better** - 82.32 vs 73.78

Test counts:
* Base: {'success': 121, 'fail': 34, 'error': 9, 'generation_errors': 0, 'test_errors': 9}
* TD: {'success': 135, 'fail': 26, 'error': 3, 'generation_errors': 0, 'test_errors': 3}
* Difference: {'success': 14, 'fail': -8, 'error': -6, 'generation_errors': 0, 'test_errors': -6}

**Improvements** - Tests that passed in TD but failed/errored in Base:
* task_id: 2
* task_id: 10
* task_id: 54
* task_id: 65
* task_id: 68
* task_id: 70
* task_id: 71
* task_id: 77
* task_id: 79
* task_id: 83
* task_id: 93
* task_id: 113
* task_id: 118
* task_id: 120
* task_id: 124

**Regressions** - Tests that passed in Base but failed/errored in TD:
* task_id: 89

---

### human_eval_qwen25coder32b_combined vs human_eval_qwen25coder32b_combined_td

Accuracy comparison: **TD is better** - 82.32 vs 75.61

Test counts:
* Base: {'success': 124, 'fail': 35, 'error': 5, 'generation_errors': 0, 'test_errors': 5}
* TD: {'success': 135, 'fail': 26, 'error': 3, 'generation_errors': 0, 'test_errors': 3}
* Difference: {'success': 11, 'fail': -9, 'error': -2, 'generation_errors': 0, 'test_errors': -2}

**Improvements** - Tests that passed in TD but failed/errored in Base:
* task_id: 2
* task_id: 38
* task_id: 65
* task_id: 68
* task_id: 70
* task_id: 71
* task_id: 79
* task_id: 93
* task_id: 100
* task_id: 102
* task_id: 115
* task_id: 118
* task_id: 121

**Regressions** - Tests that passed in Base but failed/errored in TD:
* task_id: 101
* task_id: 111

---

### human_eval_qwen25coder3b_combined vs human_eval_qwen25coder3b_combined_td

Accuracy comparison: **TD is better** - 73.17 vs 69.51

Test counts:
* Base: {'success': 114, 'fail': 41, 'error': 9, 'generation_errors': 0, 'test_errors': 9}
* TD: {'success': 120, 'fail': 38, 'error': 6, 'generation_errors': 0, 'test_errors': 6}
* Difference: {'success': 6, 'fail': -3, 'error': -3, 'generation_errors': 0, 'test_errors': -3}

**Improvements** - Tests that passed in TD but failed/errored in Base:
* task_id: 2
* task_id: 19
* task_id: 68
* task_id: 77
* task_id: 79
* task_id: 80
* task_id: 83
* task_id: 102
* task_id: 113
* task_id: 118
* task_id: 132
* task_id: 134
* task_id: 140
* task_id: 141

**Regressions** - Tests that passed in Base but failed/errored in TD:
* task_id: 8
* task_id: 65
* task_id: 76
* task_id: 87
* task_id: 89
* task_id: 111
* task_id: 135
* task_id: 137

---

### human_eval_qwen25coder7b_combined vs human_eval_qwen25coder7b_combined_td

Accuracy comparison: **TD is better** - 74.39 vs 71.34

Test counts:
* Base: {'success': 117, 'fail': 39, 'error': 8, 'generation_errors': 0, 'test_errors': 8}
* TD: {'success': 122, 'fail': 38, 'error': 4, 'generation_errors': 0, 'test_errors': 4}
* Difference: {'success': 5, 'fail': -1, 'error': -4, 'generation_errors': 0, 'test_errors': -4}

**Improvements** - Tests that passed in TD but failed/errored in Base:
* task_id: 2
* task_id: 54
* task_id: 68
* task_id: 71
* task_id: 77
* task_id: 79
* task_id: 81
* task_id: 83
* task_id: 86
* task_id: 113
* task_id: 118
* task_id: 141
* task_id: 147

**Regressions** - Tests that passed in Base but failed/errored in TD:
* task_id: 65
* task_id: 91
* task_id: 120
* task_id: 121
* task_id: 128
* task_id: 134
* task_id: 137
* task_id: 155

---

### mbpp_sanitized_chatgpt4o_combined vs mbpp_sanitized_chatgpt4o_combined_td

Accuracy comparison: **TD is better** - 86.18 vs 72.83

Test counts:
* Base: {'success': 311, 'fail': 97, 'error': 19, 'generation_errors': 0, 'test_errors': 19}
* TD: {'success': 368, 'fail': 46, 'error': 13, 'generation_errors': 0, 'test_errors': 13}
* Difference: {'success': 57, 'fail': -51, 'error': -6, 'generation_errors': 0, 'test_errors': -6}

**Improvements** - Tests that passed in TD but failed/errored in Base:
* task_id: 6
* task_id: 20
* task_id: 57
* task_id: 59
* task_id: 67
* task_id: 92
* task_id: 102
* task_id: 106
* task_id: 117
* task_id: 120
* task_id: 128
* task_id: 160
* task_id: 237
* task_id: 249
* task_id: 252
* task_id: 259
* task_id: 265
* task_id: 268
* task_id: 290
* task_id: 293
* task_id: 295
* task_id: 299
* task_id: 305
* task_id: 306
* task_id: 307
* task_id: 391
* task_id: 393
* task_id: 396
* task_id: 400
* task_id: 411
* task_id: 417
* task_id: 421
* task_id: 426
* task_id: 432
* task_id: 437
* task_id: 440
* task_id: 445
* task_id: 446
* task_id: 448
* task_id: 454
* task_id: 470
* task_id: 473
* task_id: 475
* task_id: 560
* task_id: 572
* task_id: 580
* task_id: 584
* task_id: 585
* task_id: 630
* task_id: 640
* task_id: 644
* task_id: 738
* task_id: 749
* task_id: 750
* task_id: 755
* task_id: 769
* task_id: 773
* task_id: 780
* task_id: 788
* task_id: 797
* task_id: 802

**Regressions** - Tests that passed in Base but failed/errored in TD:
* task_id: 126
* task_id: 745
* task_id: 783
* task_id: 787

---

### mbpp_sanitized_chatgpt4omini_combined vs mbpp_sanitized_chatgpt4omini_combined_td

Accuracy comparison: **TD is better** - 80.09 vs 71.66

Test counts:
* Base: {'success': 306, 'fail': 96, 'error': 25, 'generation_errors': 0, 'test_errors': 25}
* TD: {'success': 342, 'fail': 72, 'error': 13, 'generation_errors': 0, 'test_errors': 13}
* Difference: {'success': 36, 'fail': -24, 'error': -12, 'generation_errors': 0, 'test_errors': -12}

**Improvements** - Tests that passed in TD but failed/errored in Base:
* task_id: 6
* task_id: 63
* task_id: 100
* task_id: 102
* task_id: 117
* task_id: 160
* task_id: 228
* task_id: 237
* task_id: 240
* task_id: 251
* task_id: 264
* task_id: 265
* task_id: 278
* task_id: 290
* task_id: 295
* task_id: 296
* task_id: 299
* task_id: 305
* task_id: 391
* task_id: 393
* task_id: 396
* task_id: 411
* task_id: 417
* task_id: 421
* task_id: 426
* task_id: 429
* task_id: 434
* task_id: 437
* task_id: 443
* task_id: 446
* task_id: 454
* task_id: 457
* task_id: 472
* task_id: 473
* task_id: 475
* task_id: 560
* task_id: 572
* task_id: 585
* task_id: 627
* task_id: 734
* task_id: 749
* task_id: 750
* task_id: 756
* task_id: 763
* task_id: 797

**Regressions** - Tests that passed in Base but failed/errored in TD:
* task_id: 71
* task_id: 239
* task_id: 247
* task_id: 279
* task_id: 300
* task_id: 301
* task_id: 392
* task_id: 448
* task_id: 735

---

### mbpp_sanitized_claude35haiku_combined vs mbpp_sanitized_claude35haiku_combined_td

Accuracy comparison: **TD is better** - 85.01 vs 75.64

Test counts:
* Base: {'success': 323, 'fail': 82, 'error': 22, 'generation_errors': 0, 'test_errors': 22}
* TD: {'success': 363, 'fail': 54, 'error': 10, 'generation_errors': 0, 'test_errors': 10}
* Difference: {'success': 40, 'fail': -28, 'error': -12, 'generation_errors': 0, 'test_errors': -12}

**Improvements** - Tests that passed in TD but failed/errored in Base:
* task_id: 6
* task_id: 9
* task_id: 63
* task_id: 84
* task_id: 92
* task_id: 102
* task_id: 106
* task_id: 109
* task_id: 115
* task_id: 117
* task_id: 120
* task_id: 128
* task_id: 132
* task_id: 138
* task_id: 160
* task_id: 249
* task_id: 252
* task_id: 265
* task_id: 278
* task_id: 290
* task_id: 294
* task_id: 295
* task_id: 299
* task_id: 300
* task_id: 391
* task_id: 392
* task_id: 393
* task_id: 396
* task_id: 421
* task_id: 424
* task_id: 440
* task_id: 442
* task_id: 445
* task_id: 446
* task_id: 464
* task_id: 473
* task_id: 475
* task_id: 560
* task_id: 584
* task_id: 592
* task_id: 627
* task_id: 630
* task_id: 640
* task_id: 644
* task_id: 723
* task_id: 735
* task_id: 749
* task_id: 753
* task_id: 763
* task_id: 773
* task_id: 780

**Regressions** - Tests that passed in Base but failed/errored in TD:
* task_id: 18
* task_id: 72
* task_id: 125
* task_id: 137
* task_id: 247
* task_id: 284
* task_id: 581
* task_id: 603
* task_id: 629
* task_id: 745
* task_id: 802

---

### mbpp_sanitized_claude35sonnet_combined vs mbpp_sanitized_claude35sonnet_combined_td

Accuracy comparison: **TD is better** - 85.95 vs 75.41

Test counts:
* Base: {'success': 322, 'fail': 85, 'error': 20, 'generation_errors': 0, 'test_errors': 20}
* TD: {'success': 367, 'fail': 47, 'error': 13, 'generation_errors': 0, 'test_errors': 13}
* Difference: {'success': 45, 'fail': -38, 'error': -7, 'generation_errors': 0, 'test_errors': -7}

**Improvements** - Tests that passed in TD but failed/errored in Base:
* task_id: 6
* task_id: 57
* task_id: 63
* task_id: 102
* task_id: 117
* task_id: 123
* task_id: 125
* task_id: 132
* task_id: 228
* task_id: 237
* task_id: 249
* task_id: 255
* task_id: 259
* task_id: 265
* task_id: 290
* task_id: 295
* task_id: 299
* task_id: 305
* task_id: 306
* task_id: 308
* task_id: 310
* task_id: 391
* task_id: 393
* task_id: 396
* task_id: 400
* task_id: 405
* task_id: 411
* task_id: 417
* task_id: 424
* task_id: 429
* task_id: 437
* task_id: 442
* task_id: 444
* task_id: 445
* task_id: 446
* task_id: 464
* task_id: 475
* task_id: 572
* task_id: 584
* task_id: 597
* task_id: 603
* task_id: 610
* task_id: 614
* task_id: 630
* task_id: 640
* task_id: 644
* task_id: 722
* task_id: 742
* task_id: 745
* task_id: 749
* task_id: 750
* task_id: 763
* task_id: 773
* task_id: 788
* task_id: 797

**Regressions** - Tests that passed in Base but failed/errored in TD:
* task_id: 103
* task_id: 126
* task_id: 244
* task_id: 301
* task_id: 434
* task_id: 450
* task_id: 581
* task_id: 627
* task_id: 629
* task_id: 631

---

### mbpp_sanitized_qwen25coder14b_combined vs mbpp_sanitized_qwen25coder14b_combined_td

Accuracy comparison: **TD is better** - 82.44 vs 73.07

Test counts:
* Base: {'success': 312, 'fail': 94, 'error': 21, 'generation_errors': 0, 'test_errors': 21}
* TD: {'success': 352, 'fail': 62, 'error': 11, 'generation_errors': 0, 'test_errors': 11}
* Difference: {'success': 40, 'fail': -32, 'error': -10, 'generation_errors': 0, 'test_errors': -10}

**Improvements** - Tests that passed in TD but failed/errored in Base:
* task_id: 59
* task_id: 63
* task_id: 91
* task_id: 117
* task_id: 120
* task_id: 249
* task_id: 265
* task_id: 279
* task_id: 299
* task_id: 305
* task_id: 390
* task_id: 391
* task_id: 393
* task_id: 396
* task_id: 417
* task_id: 421
* task_id: 429
* task_id: 437
* task_id: 440
* task_id: 445
* task_id: 446
* task_id: 448
* task_id: 453
* task_id: 454
* task_id: 464
* task_id: 473
* task_id: 475
* task_id: 560
* task_id: 584
* task_id: 597
* task_id: 610
* task_id: 614
* task_id: 622
* task_id: 627
* task_id: 721
* task_id: 740
* task_id: 750
* task_id: 753
* task_id: 763
* task_id: 773
* task_id: 780
* task_id: 802

**Regressions** - Tests that passed in Base but failed/errored in TD:
* task_id: 472
* task_id: 805

---

### mbpp_sanitized_qwen25coder32b_combined vs mbpp_sanitized_qwen25coder32b_combined_td

Accuracy comparison: **TD is better** - 83.37 vs 73.07

Test counts:
* Base: {'success': 312, 'fail': 89, 'error': 26, 'generation_errors': 0, 'test_errors': 26}
* TD: {'success': 356, 'fail': 56, 'error': 15, 'generation_errors': 0, 'test_errors': 15}
* Difference: {'success': 44, 'fail': -33, 'error': -11, 'generation_errors': 0, 'test_errors': -11}

**Improvements** - Tests that passed in TD but failed/errored in Base:
* task_id: 57
* task_id: 91
* task_id: 102
* task_id: 111
* task_id: 117
* task_id: 120
* task_id: 128
* task_id: 160
* task_id: 237
* task_id: 252
* task_id: 259
* task_id: 265
* task_id: 290
* task_id: 295
* task_id: 299
* task_id: 301
* task_id: 304
* task_id: 305
* task_id: 390
* task_id: 391
* task_id: 396
* task_id: 411
* task_id: 417
* task_id: 419
* task_id: 424
* task_id: 437
* task_id: 440
* task_id: 442
* task_id: 443
* task_id: 445
* task_id: 446
* task_id: 454
* task_id: 464
* task_id: 473
* task_id: 475
* task_id: 572
* task_id: 611
* task_id: 614
* task_id: 620
* task_id: 622
* task_id: 630
* task_id: 643
* task_id: 644
* task_id: 750
* task_id: 753
* task_id: 763
* task_id: 773
* task_id: 780
* task_id: 797

**Regressions** - Tests that passed in Base but failed/errored in TD:
* task_id: 92
* task_id: 306
* task_id: 607
* task_id: 776
* task_id: 788

---

### mbpp_sanitized_qwen25coder3b_combined vs mbpp_sanitized_qwen25coder3b_combined_td

Accuracy comparison: **TD is better** - 69.56 vs 63.23

Test counts:
* Base: {'success': 270, 'fail': 125, 'error': 31, 'generation_errors': 0, 'test_errors': 31}
* TD: {'success': 297, 'fail': 108, 'error': 22, 'generation_errors': 0, 'test_errors': 22}
* Difference: {'success': 27, 'fail': -17, 'error': -9, 'generation_errors': 0, 'test_errors': -9}

**Improvements** - Tests that passed in TD but failed/errored in Base:
* task_id: 61
* task_id: 84
* task_id: 89
* task_id: 94
* task_id: 103
* task_id: 117
* task_id: 130
* task_id: 132
* task_id: 162
* task_id: 265
* task_id: 279
* task_id: 290
* task_id: 390
* task_id: 391
* task_id: 393
* task_id: 396
* task_id: 401
* task_id: 406
* task_id: 410
* task_id: 420
* task_id: 421
* task_id: 429
* task_id: 433
* task_id: 440
* task_id: 446
* task_id: 450
* task_id: 454
* task_id: 477
* task_id: 577
* task_id: 585
* task_id: 608
* task_id: 619
* task_id: 624
* task_id: 626
* task_id: 627
* task_id: 725
* task_id: 738
* task_id: 739
* task_id: 746
* task_id: 747
* task_id: 753
* task_id: 756
* task_id: 757
* task_id: 773
* task_id: 782
* task_id: 783
* task_id: 785
* task_id: 788
* task_id: 791
* task_id: 808

**Regressions** - Tests that passed in Base but failed/errored in TD:
* task_id: 14
* task_id: 69
* task_id: 100
* task_id: 111
* task_id: 125
* task_id: 129
* task_id: 239
* task_id: 244
* task_id: 268
* task_id: 283
* task_id: 286
* task_id: 295
* task_id: 581
* task_id: 589
* task_id: 593
* task_id: 620
* task_id: 629
* task_id: 732
* task_id: 742
* task_id: 754
* task_id: 767
* task_id: 771
* task_id: 802

---

### mbpp_sanitized_qwen25coder7b_combined vs mbpp_sanitized_qwen25coder7b_combined_td

Accuracy comparison: **TD is better** - 77.52 vs 68.38

Test counts:
* Base: {'success': 292, 'fail': 102, 'error': 33, 'generation_errors': 0, 'test_errors': 33}
* TD: {'success': 331, 'fail': 75, 'error': 21, 'generation_errors': 0, 'test_errors': 21}
* Difference: {'success': 39, 'fail': -27, 'error': -12, 'generation_errors': 0, 'test_errors': -12}

**Improvements** - Tests that passed in TD but failed/errored in Base:
* task_id: 59
* task_id: 67
* task_id: 91
* task_id: 100
* task_id: 123
* task_id: 130
* task_id: 133
* task_id: 160
* task_id: 167
* task_id: 228
* task_id: 252
* task_id: 259
* task_id: 265
* task_id: 279
* task_id: 290
* task_id: 299
* task_id: 391
* task_id: 393
* task_id: 396
* task_id: 418
* task_id: 421
* task_id: 424
* task_id: 429
* task_id: 439
* task_id: 440
* task_id: 445
* task_id: 446
* task_id: 448
* task_id: 452
* task_id: 464
* task_id: 475
* task_id: 477
* task_id: 562
* task_id: 584
* task_id: 585
* task_id: 604
* task_id: 614
* task_id: 624
* task_id: 627
* task_id: 633
* task_id: 641
* task_id: 644
* task_id: 740
* task_id: 745
* task_id: 749
* task_id: 750
* task_id: 756
* task_id: 772
* task_id: 773
* task_id: 784
* task_id: 788

**Regressions** - Tests that passed in Base but failed/errored in TD:
* task_id: 63
* task_id: 69
* task_id: 72
* task_id: 74
* task_id: 87
* task_id: 453
* task_id: 573
* task_id: 610
* task_id: 622
* task_id: 735
* task_id: 755
* task_id: 786

---

## Detailed Comparisons (With Remediation)

### human_eval_chatgpt4o_combined vs human_eval_chatgpt4o_combined_td

Accuracy comparison (with remediation): **TD is better** - 89.02 vs 84.15

Test counts (with remediation):
* Base: {'success': 138, 'fail': 26, 'error': 0, 'generation_errors': 0, 'test_errors': 0}
* TD: {'success': 146, 'fail': 17, 'error': 1, 'generation_errors': 0, 'test_errors': 1}
* Difference: {'success': 8, 'fail': -9, 'error': 1, 'generation_errors': 0, 'test_errors': 1}

**Improvements with Remediation** - Tests that passed in TD but failed/errored in Base:
* task_id: 17
* task_id: 70
* task_id: 81
* task_id: 99
* task_id: 110
* task_id: 119
* task_id: 130
* task_id: 148
* task_id: 163

**Regressions with Remediation** - Tests that passed in Base but failed/errored in TD:
* task_id: 10

---

### human_eval_chatgpt4omini_combined vs human_eval_chatgpt4omini_combined_td

Accuracy comparison (with remediation): **TD is better** - 82.93 vs 81.71

Test counts (with remediation):
* Base: {'success': 134, 'fail': 29, 'error': 1, 'generation_errors': 0, 'test_errors': 1}
* TD: {'success': 136, 'fail': 27, 'error': 1, 'generation_errors': 0, 'test_errors': 1}
* Difference: {'success': 2, 'fail': -2, 'error': 0, 'generation_errors': 0, 'test_errors': 0}

**Improvements with Remediation** - Tests that passed in TD but failed/errored in Base:
* task_id: 70
* task_id: 77
* task_id: 79
* task_id: 83
* task_id: 113
* task_id: 148

**Regressions with Remediation** - Tests that passed in Base but failed/errored in TD:
* task_id: 10
* task_id: 91
* task_id: 105
* task_id: 137

---

### human_eval_claude35haiku_combined vs human_eval_claude35haiku_combined_td

Accuracy comparison (with remediation): **TD is better** - 90.85 vs 86.59

Test counts (with remediation):
* Base: {'success': 142, 'fail': 22, 'error': 0, 'generation_errors': 0, 'test_errors': 0}
* TD: {'success': 149, 'fail': 14, 'error': 1, 'generation_errors': 0, 'test_errors': 1}
* Difference: {'success': 7, 'fail': -8, 'error': 1, 'generation_errors': 0, 'test_errors': 1}

**Improvements with Remediation** - Tests that passed in TD but failed/errored in Base:
* task_id: 50
* task_id: 65
* task_id: 75
* task_id: 76
* task_id: 84
* task_id: 113
* task_id: 129
* task_id: 140
* task_id: 148

**Regressions with Remediation** - Tests that passed in Base but failed/errored in TD:
* task_id: 130
* task_id: 163

---

### human_eval_claude35sonnet_combined vs human_eval_claude35sonnet_combined_td

Accuracy comparison (with remediation): **TD is better** - 92.07 vs 89.63

Test counts (with remediation):
* Base: {'success': 147, 'fail': 16, 'error': 1, 'generation_errors': 0, 'test_errors': 1}
* TD: {'success': 151, 'fail': 11, 'error': 2, 'generation_errors': 0, 'test_errors': 2}
* Difference: {'success': 4, 'fail': -5, 'error': 1, 'generation_errors': 0, 'test_errors': 1}

**Improvements with Remediation** - Tests that passed in TD but failed/errored in Base:
* task_id: 17
* task_id: 50
* task_id: 93
* task_id: 148
* task_id: 151

**Regressions with Remediation** - Tests that passed in Base but failed/errored in TD:
* task_id: 132

---

### human_eval_qwen25coder14b_combined vs human_eval_qwen25coder14b_combined_td

Accuracy comparison (with remediation): **TD is better** - 82.93 vs 74.39

Test counts (with remediation):
* Base: {'success': 122, 'fail': 41, 'error': 1, 'generation_errors': 0, 'test_errors': 1}
* TD: {'success': 136, 'fail': 27, 'error': 1, 'generation_errors': 0, 'test_errors': 1}
* Difference: {'success': 14, 'fail': -14, 'error': 0, 'generation_errors': 0, 'test_errors': 0}

**Improvements with Remediation** - Tests that passed in TD but failed/errored in Base:
* task_id: 2
* task_id: 10
* task_id: 54
* task_id: 65
* task_id: 68
* task_id: 70
* task_id: 71
* task_id: 77
* task_id: 79
* task_id: 83
* task_id: 93
* task_id: 113
* task_id: 118
* task_id: 120
* task_id: 148

**Regressions with Remediation** - Tests that passed in Base but failed/errored in TD:
* task_id: 89

---

### human_eval_qwen25coder32b_combined vs human_eval_qwen25coder32b_combined_td

Accuracy comparison (with remediation): **TD is better** - 86.59 vs 80.49

Test counts (with remediation):
* Base: {'success': 132, 'fail': 31, 'error': 1, 'generation_errors': 0, 'test_errors': 1}
* TD: {'success': 142, 'fail': 21, 'error': 1, 'generation_errors': 0, 'test_errors': 1}
* Difference: {'success': 10, 'fail': -10, 'error': 0, 'generation_errors': 0, 'test_errors': 0}

**Improvements with Remediation** - Tests that passed in TD but failed/errored in Base:
* task_id: 17
* task_id: 38
* task_id: 65
* task_id: 70
* task_id: 72
* task_id: 93
* task_id: 99
* task_id: 100
* task_id: 102
* task_id: 115
* task_id: 148

**Regressions with Remediation** - Tests that passed in Base but failed/errored in TD:
* task_id: 10

---

### human_eval_qwen25coder3b_combined vs human_eval_qwen25coder3b_combined_td

Accuracy comparison (with remediation): **TD is better** - 73.17 vs 69.51

Test counts (with remediation):
* Base: {'success': 114, 'fail': 50, 'error': 0, 'generation_errors': 0, 'test_errors': 0}
* TD: {'success': 120, 'fail': 44, 'error': 0, 'generation_errors': 0, 'test_errors': 0}
* Difference: {'success': 6, 'fail': -6, 'error': 0, 'generation_errors': 0, 'test_errors': 0}

**Improvements with Remediation** - Tests that passed in TD but failed/errored in Base:
* task_id: 2
* task_id: 19
* task_id: 68
* task_id: 77
* task_id: 79
* task_id: 80
* task_id: 83
* task_id: 102
* task_id: 113
* task_id: 118
* task_id: 132
* task_id: 134
* task_id: 140
* task_id: 141

**Regressions with Remediation** - Tests that passed in Base but failed/errored in TD:
* task_id: 8
* task_id: 65
* task_id: 76
* task_id: 87
* task_id: 89
* task_id: 111
* task_id: 135
* task_id: 137

---

### human_eval_qwen25coder7b_combined vs human_eval_qwen25coder7b_combined_td

Accuracy comparison (with remediation): **TD is better** - 74.39 vs 71.34

Test counts (with remediation):
* Base: {'success': 117, 'fail': 47, 'error': 0, 'generation_errors': 0, 'test_errors': 0}
* TD: {'success': 122, 'fail': 42, 'error': 0, 'generation_errors': 0, 'test_errors': 0}
* Difference: {'success': 5, 'fail': -5, 'error': 0, 'generation_errors': 0, 'test_errors': 0}

**Improvements with Remediation** - Tests that passed in TD but failed/errored in Base:
* task_id: 2
* task_id: 54
* task_id: 68
* task_id: 71
* task_id: 77
* task_id: 79
* task_id: 81
* task_id: 83
* task_id: 86
* task_id: 113
* task_id: 118
* task_id: 141
* task_id: 147

**Regressions with Remediation** - Tests that passed in Base but failed/errored in TD:
* task_id: 65
* task_id: 91
* task_id: 120
* task_id: 121
* task_id: 128
* task_id: 134
* task_id: 137
* task_id: 155

---

### mbpp_sanitized_chatgpt4o_combined vs mbpp_sanitized_chatgpt4o_combined_td

Accuracy comparison (with remediation): **TD is better** - 91.10 vs 88.29

Test counts (with remediation):
* Base: {'success': 377, 'fail': 43, 'error': 7, 'generation_errors': 0, 'test_errors': 7}
* TD: {'success': 389, 'fail': 29, 'error': 9, 'generation_errors': 0, 'test_errors': 9}
* Difference: {'success': 12, 'fail': -14, 'error': 2, 'generation_errors': 0, 'test_errors': 2}

**Improvements with Remediation** - Tests that passed in TD but failed/errored in Base:
* task_id: 87
* task_id: 120
* task_id: 160
* task_id: 248
* task_id: 301
* task_id: 307
* task_id: 398
* task_id: 415
* task_id: 421
* task_id: 444
* task_id: 448
* task_id: 580
* task_id: 626
* task_id: 644
* task_id: 756
* task_id: 769
* task_id: 780
* task_id: 802

**Regressions with Remediation** - Tests that passed in Base but failed/errored in TD:
* task_id: 126
* task_id: 164
* task_id: 434
* task_id: 592
* task_id: 610
* task_id: 745

---

### mbpp_sanitized_chatgpt4omini_combined vs mbpp_sanitized_chatgpt4omini_combined_td

Accuracy comparison (with remediation): **TD is better** - 85.01 vs 82.20

Test counts (with remediation):
* Base: {'success': 351, 'fail': 66, 'error': 10, 'generation_errors': 0, 'test_errors': 10}
* TD: {'success': 363, 'fail': 57, 'error': 7, 'generation_errors': 0, 'test_errors': 7}
* Difference: {'success': 12, 'fail': -9, 'error': -3, 'generation_errors': 0, 'test_errors': -3}

**Improvements with Remediation** - Tests that passed in TD but failed/errored in Base:
* task_id: 63
* task_id: 117
* task_id: 124
* task_id: 160
* task_id: 228
* task_id: 237
* task_id: 264
* task_id: 278
* task_id: 296
* task_id: 307
* task_id: 429
* task_id: 434
* task_id: 440
* task_id: 442
* task_id: 464
* task_id: 472
* task_id: 473
* task_id: 627
* task_id: 638
* task_id: 734
* task_id: 749
* task_id: 765
* task_id: 773

**Regressions with Remediation** - Tests that passed in Base but failed/errored in TD:
* task_id: 71
* task_id: 239
* task_id: 247
* task_id: 279
* task_id: 300
* task_id: 398
* task_id: 448
* task_id: 584
* task_id: 630
* task_id: 735
* task_id: 745

---

### mbpp_sanitized_claude35haiku_combined vs mbpp_sanitized_claude35haiku_combined_td

Accuracy comparison (with remediation): **TD is same** - 91.10 vs 91.10

Test counts (with remediation):
* Base: {'success': 389, 'fail': 31, 'error': 7, 'generation_errors': 0, 'test_errors': 7}
* TD: {'success': 389, 'fail': 32, 'error': 6, 'generation_errors': 0, 'test_errors': 6}
* Difference: {'success': 0, 'fail': 1, 'error': -1, 'generation_errors': 0, 'test_errors': -1}

**Improvements with Remediation** - Tests that passed in TD but failed/errored in Base:
* task_id: 63
* task_id: 84
* task_id: 109
* task_id: 120
* task_id: 138
* task_id: 237
* task_id: 464
* task_id: 563
* task_id: 626
* task_id: 644

**Regressions with Remediation** - Tests that passed in Base but failed/errored in TD:
* task_id: 125
* task_id: 247
* task_id: 284
* task_id: 304
* task_id: 443
* task_id: 580
* task_id: 581
* task_id: 603
* task_id: 617
* task_id: 638

---

### mbpp_sanitized_claude35sonnet_combined vs mbpp_sanitized_claude35sonnet_combined_td

Accuracy comparison (with remediation): **TD is better** - 94.15 vs 92.74

Test counts (with remediation):
* Base: {'success': 396, 'fail': 23, 'error': 8, 'generation_errors': 0, 'test_errors': 8}
* TD: {'success': 402, 'fail': 18, 'error': 7, 'generation_errors': 0, 'test_errors': 7}
* Difference: {'success': 6, 'fail': -5, 'error': -1, 'generation_errors': 0, 'test_errors': -1}

**Improvements with Remediation** - Tests that passed in TD but failed/errored in Base:
* task_id: 63
* task_id: 120
* task_id: 125
* task_id: 306
* task_id: 310
* task_id: 405
* task_id: 429
* task_id: 592
* task_id: 644

**Regressions with Remediation** - Tests that passed in Base but failed/errored in TD:
* task_id: 304
* task_id: 415
* task_id: 581

---

### mbpp_sanitized_qwen25coder14b_combined vs mbpp_sanitized_qwen25coder14b_combined_td

Accuracy comparison (with remediation): **TD is better** - 83.37 vs 74.94

Test counts (with remediation):
* Base: {'success': 320, 'fail': 104, 'error': 3, 'generation_errors': 0, 'test_errors': 3}
* TD: {'success': 356, 'fail': 66, 'error': 3, 'generation_errors': 0, 'test_errors': 3}
* Difference: {'success': 36, 'fail': -38, 'error': 0, 'generation_errors': 0, 'test_errors': 0}

**Improvements with Remediation** - Tests that passed in TD but failed/errored in Base:
* task_id: 6
* task_id: 59
* task_id: 63
* task_id: 91
* task_id: 117
* task_id: 120
* task_id: 249
* task_id: 259
* task_id: 265
* task_id: 279
* task_id: 305
* task_id: 390
* task_id: 391
* task_id: 393
* task_id: 396
* task_id: 429
* task_id: 437
* task_id: 440
* task_id: 446
* task_id: 448
* task_id: 453
* task_id: 464
* task_id: 473
* task_id: 475
* task_id: 560
* task_id: 584
* task_id: 597
* task_id: 610
* task_id: 622
* task_id: 627
* task_id: 640
* task_id: 721
* task_id: 740
* task_id: 750
* task_id: 753
* task_id: 773
* task_id: 776
* task_id: 780
* task_id: 802

**Regressions with Remediation** - Tests that passed in Base but failed/errored in TD:
* task_id: 472
* task_id: 595
* task_id: 805

---

### mbpp_sanitized_qwen25coder32b_combined vs mbpp_sanitized_qwen25coder32b_combined_td

Accuracy comparison (with remediation): **TD is better** - 87.82 vs 85.01

Test counts (with remediation):
* Base: {'success': 363, 'fail': 51, 'error': 13, 'generation_errors': 0, 'test_errors': 13}
* TD: {'success': 375, 'fail': 42, 'error': 10, 'generation_errors': 0, 'test_errors': 10}
* Difference: {'success': 12, 'fail': -9, 'error': -3, 'generation_errors': 0, 'test_errors': -3}

**Improvements with Remediation** - Tests that passed in TD but failed/errored in Base:
* task_id: 18
* task_id: 63
* task_id: 87
* task_id: 120
* task_id: 143
* task_id: 160
* task_id: 237
* task_id: 252
* task_id: 301
* task_id: 304
* task_id: 305
* task_id: 307
* task_id: 411
* task_id: 417
* task_id: 440
* task_id: 443
* task_id: 630
* task_id: 644
* task_id: 734
* task_id: 749
* task_id: 780

**Regressions with Remediation** - Tests that passed in Base but failed/errored in TD:
* task_id: 92
* task_id: 164
* task_id: 306
* task_id: 393
* task_id: 607
* task_id: 615
* task_id: 626
* task_id: 776
* task_id: 788

---

### mbpp_sanitized_qwen25coder3b_combined vs mbpp_sanitized_qwen25coder3b_combined_td

Accuracy comparison (with remediation): **TD is better** - 69.56 vs 63.47

Test counts (with remediation):
* Base: {'success': 271, 'fail': 155, 'error': 0, 'generation_errors': 0, 'test_errors': 0}
* TD: {'success': 297, 'fail': 130, 'error': 0, 'generation_errors': 0, 'test_errors': 0}
* Difference: {'success': 26, 'fail': -25, 'error': 0, 'generation_errors': 0, 'test_errors': 0}

**Improvements with Remediation** - Tests that passed in TD but failed/errored in Base:
* task_id: 61
* task_id: 84
* task_id: 89
* task_id: 94
* task_id: 103
* task_id: 117
* task_id: 130
* task_id: 132
* task_id: 162
* task_id: 265
* task_id: 279
* task_id: 290
* task_id: 390
* task_id: 391
* task_id: 393
* task_id: 396
* task_id: 401
* task_id: 406
* task_id: 410
* task_id: 420
* task_id: 421
* task_id: 429
* task_id: 433
* task_id: 440
* task_id: 446
* task_id: 450
* task_id: 454
* task_id: 477
* task_id: 577
* task_id: 585
* task_id: 608
* task_id: 619
* task_id: 624
* task_id: 626
* task_id: 627
* task_id: 725
* task_id: 738
* task_id: 739
* task_id: 746
* task_id: 753
* task_id: 756
* task_id: 757
* task_id: 773
* task_id: 782
* task_id: 783
* task_id: 785
* task_id: 788
* task_id: 791
* task_id: 808

**Regressions with Remediation** - Tests that passed in Base but failed/errored in TD:
* task_id: 14
* task_id: 69
* task_id: 100
* task_id: 111
* task_id: 125
* task_id: 129
* task_id: 239
* task_id: 244
* task_id: 268
* task_id: 283
* task_id: 286
* task_id: 295
* task_id: 581
* task_id: 589
* task_id: 593
* task_id: 620
* task_id: 629
* task_id: 732
* task_id: 742
* task_id: 754
* task_id: 767
* task_id: 771
* task_id: 802

---

### mbpp_sanitized_qwen25coder7b_combined vs mbpp_sanitized_qwen25coder7b_combined_td

Accuracy comparison (with remediation): **TD is better** - 77.99 vs 68.38

Test counts (with remediation):
* Base: {'success': 292, 'fail': 135, 'error': 0, 'generation_errors': 0, 'test_errors': 0}
* TD: {'success': 333, 'fail': 94, 'error': 0, 'generation_errors': 0, 'test_errors': 0}
* Difference: {'success': 41, 'fail': -41, 'error': 0, 'generation_errors': 0, 'test_errors': 0}

**Improvements with Remediation** - Tests that passed in TD but failed/errored in Base:
* task_id: 59
* task_id: 67
* task_id: 91
* task_id: 100
* task_id: 123
* task_id: 130
* task_id: 133
* task_id: 160
* task_id: 164
* task_id: 167
* task_id: 228
* task_id: 252
* task_id: 259
* task_id: 265
* task_id: 279
* task_id: 290
* task_id: 299
* task_id: 391
* task_id: 393
* task_id: 396
* task_id: 418
* task_id: 421
* task_id: 424
* task_id: 429
* task_id: 439
* task_id: 440
* task_id: 445
* task_id: 446
* task_id: 448
* task_id: 452
* task_id: 464
* task_id: 475
* task_id: 477
* task_id: 562
* task_id: 584
* task_id: 585
* task_id: 604
* task_id: 614
* task_id: 624
* task_id: 627
* task_id: 633
* task_id: 641
* task_id: 644
* task_id: 740
* task_id: 745
* task_id: 749
* task_id: 750
* task_id: 756
* task_id: 772
* task_id: 773
* task_id: 784
* task_id: 788

**Regressions with Remediation** - Tests that passed in Base but failed/errored in TD:
* task_id: 63
* task_id: 69
* task_id: 72
* task_id: 74
* task_id: 87
* task_id: 453
* task_id: 573
* task_id: 610
* task_id: 622
* task_id: 735
* task_id: 755

---

## Incomplete Directories Analysis

**Completion Status:** 16/16 directories (100.0%)

🎉 **All directories are complete!** No re-execution needed.

## Experiment Metadata

**LLM Configuration:**
- Configuration Keys: CHATGPT_4O, CHATGPT_4O_MINI, CLAUDE_35_HAIKU, CLAUDE_35_SONNET, QWEN_14B_CODER, QWEN_2_5_CODER_32B, QWEN_3B_CODER, QWEN_7B_CODER
- Model Name: openai/gpt-4o-2024-11-20
**Dataset Configuration:**
- Research Question: rq2
- Dataset Coverage: 1.0 (100.0% of problems)

