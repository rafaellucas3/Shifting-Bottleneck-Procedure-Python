# Shifting Bottleneck Procedure

The shifting bottleneck procedure is known to be one of the most successful heuristic procedure for Jm||Cmax. Here is the implementation of said heuristic, presented by Adams (1988), in Python 3.7. The code presented here is an updated and commented version based on dr. N.D. (Nicky) van Foreest work. 

### Prerequisites
* Python 3.7.4;
* Networkx;
* PuLP (if you want to run the linear program optimization included);
* Gurobi 9.0 (if you're feeling fancy and want an actual good LP solver);

## References
1. The original code from dr. van Foreest can be found [here](http://nicky.vanforeest.com/scheduling/scheduling.html#scheduling).
2. Adams, J., Balas, E., & Zawack, D. (1988). The Shifting Bottleneck Procedure for Job Shop Scheduling. Management Science, 34(3), 391-401. Retrieved February 25, 2020, from www.jstor.org/stable/2632051
3. Pinedo, M. (2012). Scheduling : theory, algorithms, and systems. New York: Springer.
