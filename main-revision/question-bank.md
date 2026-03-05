Why did you implement dynamic sparsity instead of static sparsity?

Why fused GEMM over naive GEMM?

How does KV cache improve GPU utilization?



## 1️⃣ Key Projects to Highlight

| Project                                  | Core Point to Highlight                                                         | Likely Questions / Follow-ups                                                   |
| ---------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| **Self-Tuning Sparse Attention**         | Dynamic sparsity for long-sequence Transformers (5.5× speedup, L1 error < 0.03) | Why dynamic sparsity? How maintain accuracy? GPU memory tradeoffs?              |
| **High-Throughput LLM Inference System** | KV caching + Continuous Batching → 2–7× throughput                              | How batching improves GPU utilization? Pipeline bottlenecks? Latency reduction? |
| **Fused GEMM Kernels (CUDA/Triton)**     | Shared memory tiling, fused post-processing, 86% cuBLAS speed                   | How decide tile size? Shared memory vs registers? Occupancy tuning?             |
| **Modular Multi-Agent LLM Automation**   | Orchestrates planning, retrieval, synthesis for research                        | How to evaluate results? Why modular? System reasoning for scalability?         |
| **Text Line Recognition (DTLR + BART)**  | Edge-efficient pipeline, 76% faster than TrOCR                                  | How to reduce training data? Model adaptation? Metrics interpretation?          |

---

## 2️⃣ Deep Learning “Why” Questions

**Prepare clear answers with your experience as examples.**

| Topic                   | Sample Question                                        | Key Points / Talking Points                                              |
| ----------------------- | ------------------------------------------------------ | ------------------------------------------------------------------------ |
| Backprop / Optimization | Why use Adam instead of SGD?                           | Momentum vs adaptive LR, sparse gradient advantages, bias correction     |
| Initialization          | Why not all-zero weights?                              | Vanishing/exploding gradients, He/Xavier init, relu vs tanh              |
| BatchNorm / LayerNorm   | Why BatchNorm in CNNs, LayerNorm in Transformers?      | Internal covariate shift, batch size dependency, normalization axis      |
| Multi-head Attention    | Why multiple heads?                                    | Captures different relations, representation diversity                   |
| Sparse Attention        | Why dynamic vs static?                                 | Efficiency on long sequences, maintain accuracy, GPU utilization         |
| Overfitting             | Training loss decreases but validation loss increases? | Regularization, dropout, data augmentation, early stopping               |
| Mixed Precision         | Why use FP16/BF16?                                     | TensorCore optimization, loss scaling to prevent gradient underflow      |
| Inference Latency       | How to reduce inference latency?                       | Fused kernels, quantization, pruning, batching, KV cache, pipelining     |
| GPU Utilization         | GPU utilization low → what to check?                   | Batch size, data pipeline, kernel inefficiency, occupancy, memory access |
| GEMM Tiling             | How to decide tile size?                               | Fit shared memory, register usage, occupancy, empirical autotuning       |

---

## 3️⃣ Mini-Coding / Algorithm Questions

Focus on **short, whiteboard-style implementations**, not full system code:

1. **Softmax / ReLU / GELU / LayerNorm** (forward + backward)
2. **Adam update step** (1st & 2nd moment, bias correction)
3. **Forward Conv2D** (with stride/padding; im2col optional)
4. **Mini-backprop** for MLP
5. **Optional:** small KV cache logic or batching example (pseudocode)

> Tip: Use **project examples** to justify why you implemented them that way.

---

## 4️⃣ System / Performance Reasoning

| Question                                 | Sample Talking Points (based on your projects)                                        |
| ---------------------------------------- | ------------------------------------------------------------------------------------- |
| How to improve GPU inference throughput? | KV caching, fused kernels, continuous batching, pipelining, quantization              |
| How to debug low GPU utilization?        | Check batch size, data loader speed, kernel occupancy, memory coalescing              |
| How to tune GEMM tile size?              | Shared memory fit, registers per thread, occupancy, benchmarking different tile sizes |

---

## 5️⃣ Behavioral / Research Questions

* “Tell me about your most interesting deep learning project.”

  * 2–3 min: Problem → Approach → Key challenge → Result → GPU/Performance takeaway
* “What recent paper or method excites you?”

  * Mention sparse attention, transformers, or LLM efficiency
* “How would you improve current transformer architectures?”

  * Discuss memory-efficient attention, kernel optimizations, mixed precision

---

## 6️⃣ Quick Mental Checklist Before Answering

1. **Start conceptual** → then give **example from your resume/projects**
2. **Mention GPU/system impact** → NVIDIA loves performance-aware thinking
3. **Include trade-offs** → memory vs compute, precision vs accuracy
4. **Be ready for follow-ups** → they may ask “why this choice?” 3–4 layers deep
5. **Speak confidently about numbers** → speedups, sparsity, throughput

---

### ✅ Suggested Prep Flow (Tonight / 1–2 hours)

1. **Review all 5 main projects** → 2–3 min story per project
2. **Deep Learning “Why” questions** → answer aloud, tie to projects
3. **System-level Qs** → GPU utilization, latency, GEMM tiling
4. **Mini-coding refresh** → softmax, ReLU, Adam, Conv2D forward
5. **Mock pitch** → summarize your best project in <2 minutes

---



## 1️⃣ “How would you improve inference latency?”

**Answer Framework:** Focus on **algorithm + model + system level optimizations**.

**Key Points:**

1. **Model-level:**

   * Quantization (FP16 / INT8) → reduces memory and compute.
   * Pruning / sparse attention → fewer operations without losing accuracy.
   * Knowledge distillation → smaller student model.

2. **Kernel-level / GPU-level:**

   * Fused kernels (combine Linear + Bias + Activation) → fewer memory accesses.
   * Continuous batching → improve GPU utilization with dynamic batching.
   * Optimize memory access (coalesced loads, shared memory).

3. **Pipeline / system-level:**

   * KV caching for transformer inference → reduces repeated computations.
   * Reduce CPU-GPU synchronization overhead.
   * Overlap data loading and computation (pipelining streams).

**Sample Answer (using your projects):**

> “In my high-throughput LLM inference engine, we improved latency by using KV caching to avoid recomputation, implementing continuous batching to maximize GPU occupancy, and applying fused kernels for Linear + Bias + Activation operations. Additionally, I would consider FP16 quantization or pruning to reduce computation without sacrificing accuracy.”

---

## 2️⃣ “If GPU utilization is low, what do you check?”

**Answer Framework:** Think **bottleneck diagnosis**: is it **GPU compute**, **memory**, or **data feeding**?

**Key Points:**

1. **Batch size too small** → GPU not fully utilized.
2. **Data loading bottleneck** → CPU / disk unable to feed GPU quickly.
3. **Kernel inefficiency** → uncoalesced memory accesses, warp divergence.
4. **Too many small kernel launches** → overhead dominates.
5. **Mixed precision / compute mismatch** → GPU compute units underused.

**Sample Answer (using your projects):**

> “I would first check if the batch size is sufficient to fully occupy GPU cores. Then I’d examine the data pipeline to ensure the GPU isn’t waiting on the CPU. I’d also inspect kernel launches — fused kernels or vectorized memory access can improve throughput. In my fused GEMM work, we optimized shared memory tiling and occupancy to achieve up to 86% of cuBLAS performance, which illustrates how kernel-level optimization directly impacts utilization.”

---

## 3️⃣ “How do you decide tile size in GEMM kernels?”

**Answer Framework:** Tile size is about **balancing memory and compute** for GPU efficiency.

**Key Points:**

1. **Tile size affects:**

   * Shared memory usage → must fit per Streaming Multiprocessor (SM).
   * Register usage → avoid spilling to global memory.
   * Thread block occupancy → enough threads to hide latency.

2. **Guidelines:**

   * Start with tile size that **fits shared memory per block**.
   * Tune for **occupancy** → maximize number of active warps per SM.
   * Consider **matrix dimensions** → use smaller tiles for irregular shapes.

3. **Iterative tuning:**

   * Often empirically tuned using autotuning or benchmarking (e.g., like you did in your fused GEMM project).

**Sample Answer (using your projects):**

> “In my fused GEMM kernels, I first determined the tile size that fits in shared memory while leaving enough registers for other operations. I then benchmarked different tile sizes to maximize occupancy and throughput on the GPU, considering the matrix dimensions and SM capacity. This approach allowed me to reach 86% of cuBLAS performance while keeping global memory accesses efficient.”

---

✅ **Tip for the Interview:**

* Answer **conceptually first**, then use **a quick example from your own work**.
* Always mention **trade-offs** — e.g., memory vs compute, precision vs speed.
* This shows both **research reasoning** and **practical GPU experience**, which is exactly what NVIDIA likes.

