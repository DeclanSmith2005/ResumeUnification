REVIEW NOTES

These are proposed resume drafts, written on the assumption that the suggested technical details reflect work you performed. Confirm or revise every REVIEW item before submitting an application. The PDF previews contain the draft bullet text without review labels so that you can assess the original presentation.

Each REVIEW identifier appears immediately above its bullet in the corresponding component. Those LaTeX comments are invisible in the PDF. Bullets labelled SOURCE contain reframed claims from the supplied components. This is provenance information, not independent verification.

No new numerical achievements were invented. The existing latency, fill rate, ranking, CPU, and backtest figures were carried forward. Check the benchmark conditions, your individual contribution, and the calculation of every retained metric. The Amazon December 2026 launch and audience remain described as planned. Dates and shared skills are unchanged.

The volatility strategy's 1.4% maximum drawdown is the magnitude of the original negative 1.4% figure. Its Sharpe ratio and CAGR remain results from the original 12 month simulation. Do not present them as validated after costs or on unseen data unless you can substantiate that.

Trading research uses the two expanded trading projects. Quackston and CPU Architecture remain alternate trading components, commented out in main.py. Swapping them in may require shortening other content to preserve one page. These notes apply to the imported specialty drafts; the generic SWE content is unchanged.

PerformanceEngineering

P01. components/PerformanceEngineering/Amazon_PerformanceEngineering.txt, bullet 1
Confirm that you profiled the rendering critical path. Parallel batches, response caching, and the latency figures were already in the supplied component.

P02. components/PerformanceEngineering/Amazon_PerformanceEngineering.txt, bullet 2
Bounded concurrency, timeout handling, and cache invalidation are proposed implementation details. Confirm your ownership and whether they are implemented or still planned.

P03. components/PerformanceEngineering/Scotiabank2026_PerformanceEngineering.txt, bullet 1
cProfile, EXPLAIN ANALYZE, ORM profiling, and query batching are proposed. The Python backend, PostgreSQL, SQLAlchemy, and technical leadership are established in the source.

P04. components/PerformanceEngineering/Scotiabank2026_PerformanceEngineering.txt, bullet 2
Adjacency list storage, cached state, and avoiding repeated scans are proposed. Confirm the actual graph representation and update strategy.

P05. components/PerformanceEngineering/Scotiabank2025_PerformanceEngineering.txt, bullet 1
Tracing request and SQL execution paths is proposed. The migration and response time figures are retained from the source; confirm what caused the improvement.

P06. components/PerformanceEngineering/Scotiabank2025_PerformanceEngineering.txt, bullet 2
Confirm that the tests checked slow responses and inconsistent log processing, and that you correlated individual failures with Splunk traces. The test count and tools come from the source.

P07. components/PerformanceEngineering/BrightBridge_PerformanceEngineering.txt, bullet 1
Confirm that contention occurred on individual tutor time slots and that the protected invariant was preventing duplicate bookings. Transactions, optimistic locking, and concurrent reservations are established.

P08. components/PerformanceEngineering/BrightBridge_PerformanceEngineering.txt, bullet 2
Invocation profiling and evaluation under burst traffic are proposed. The endpoint count, hosting platform, and rate limiting are retained.

P09. components/PerformanceEngineering/CPUArchitecture_PerformanceEngineering.txt, bullet 1
Cycle accurate testbenches and explicit critical path analysis are proposed. Confirm the simulator, tests, and timing analysis you actually used.

P11. components/PerformanceEngineering/Quackston_PerformanceEngineering.txt, bullet 1
Separating route computation from telemetry I/O is proposed. Confirm whether this used separate processes, threads, or another design. Timing figures are retained.

P12. components/PerformanceEngineering/Quackston_PerformanceEngineering.txt, bullet 2
Adjacency lists, a binary min heap, and systematic graph size or telemetry rate benchmarks are proposed. Replace them with the actual representation and evaluation.

P13. components/PerformanceEngineering/FaceBell_PerformanceEngineering.txt, bullet 1
Python instrumentation, per-stage timestamps, decoupling frame capture from cloud requests, bounded queues, and discarding stale frames are proposed. Confirm the language, instrumentation, queue policy, and concurrency model actually used. AWS Rekognition and the sub-200 ms stream-to-notification result are retained from the original generic SWE component. Confirm whether the proposed mechanisms contributed to that result and how latency was measured; no percentile, frame rate, or load level is established.

P14. components/PerformanceEngineering/FaceBell_PerformanceEngineering.txt, bullet 2
OpenCV motion filtering, recognition confidence threshold tuning, and their contribution to the false-positive improvement are proposed. Confirm the actual edge filtering and recognition configuration. The 40% reduction in false positives and first place in the ECE Innovation Design Competition are retained from the original component. Frame filtering concerns redundant inference work; it is not itself evidence of greater recognition accuracy. No new numerical improvement is claimed.

TradingResearch

T01. components/TradingResearch/Amazon_TradingResearch.txt, bullet 1
Explicit comparative benchmarking and diagnosis of serial bottlenecks are proposed. The implementation changes and latency figures are established.

T02. components/TradingResearch/Amazon_TradingResearch.txt, bullet 2
Schema validation and deterministic error handling are proposed. Confirm the validation performed and error behavior; this remains Amazon content work, not trading work.

T03. components/TradingResearch/Scotiabank2026_TradingResearch.txt, bullet 1
Confirm the persistence mechanism and consistency guarantees. Do not interpret this as an automated research or backtesting engine; the application was onboarding.

T04. components/TradingResearch/Scotiabank2026_TradingResearch.txt, bullet 2
Deterministic test fixtures, reproducible failure environments, and schema validation tests are proposed. The listed implementation tools and leadership are established.

T05. components/TradingResearch/Scotiabank2025_TradingResearch.txt, bullet 1
Confirm that database backed data retrieval was the part you optimized. The migration and latency figures are retained, without claiming market data experience.

T06. components/TradingResearch/Scotiabank2025_TradingResearch.txt, bullet 2
Missing, duplicate, and out of order record checks are proposed test cases. Confirm which cases the original tests actually covered.

T08. components/TradingResearch/RITC_TradingResearch.txt, bullet 2
Explicit calibration, inventory based quote adjustments, and analysis of spread capture versus fill probability are proposed. Confirm the actual quoting policy.

T09. components/TradingResearch/RITC_TradingResearch.txt, bullet 3
Market data replay and parameter comparisons are proposed. Beta neutral arbitrage, volatility normalized z scores, and risk limits are retained from the current source.

T10. components/TradingResearch/VolatilityStrategy_TradingResearch.txt, bullet 1
Rolling realized volatility and estimated fund exposure changes are proposed signal inputs. Confirm the actual formula, data inputs, and rebalance timing.

T11. components/TradingResearch/VolatilityStrategy_TradingResearch.txt, bullet 2
Python/pandas, lagged inputs, position sizing, cost modelling, and parameter sensitivity analysis are proposed. Confirm each item and distinguish completed analysis from planned extensions.

T12. components/TradingResearch/VolatilityStrategy_TradingResearch.txt, bullet 3
The original simulation metrics are retained, with drawdown expressed as a magnitude. Daily P&L, turnover, and regime analysis are proposed additions. These figures are not newly validated or assumed to include transaction costs or holdout testing.

T13. components/TradingResearch/Quackston_TradingResearch.txt, bullet 1
The graph representation and binary min heap are proposed. The algorithm, telemetry, and latency are established. This component is an alternate.

T14. components/TradingResearch/Quackston_TradingResearch.txt, bullet 2
Telemetry replay, expected path comparisons, and reproducible failure cases are proposed. Confirm whether such an evaluation harness existed.

T16. components/TradingResearch/CPUArchitecture_TradingResearch.txt, bullet 2
Instruction level testbenches, register and memory checks, and equivalence testing are proposed. This component is an alternate.
