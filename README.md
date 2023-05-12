# Community Structure Identification: Amazon Co-Purchasing Network

## Girvan-Newman

The Girvan–Newman algorithm detects communities by progressively removing edges from the original network. The connected components of the remaining network are the communities. Instead of trying to construct a measure that tells us which edges are the most central to communities, the Girvan–Newman algorithm focuses on edges that are most likely "between" communities.

The algorithm's steps for community detection are summarized below:

1. The betweenness of all existing edges in the network is calculated first.
2. The edge(s) with the highest betweenness are removed.
3. The betweenness of all edges affected by the removal is recalculated.
4. Steps 2 and 3 are repeated until no edges remain.

### Students

- Tran Thi Ngoc Diep - 2270711
- Nguyen Truong Minh Hoang - 2270757
- Mai Hong Quoc Khanh - 2270587
- Pham Le Gia Thinh - 2270593
