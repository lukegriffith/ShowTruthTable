# ShowTruthTable.py 

Python3 progarm I created to help me with logic in my introduction to Computer Math course. 

    enter python expression or type exit.
            > r and q

    | q      | r      | r and q |
    |    True|    True|    True |
    |    True|   False|   False |
    |   False|    True|   False |
    |   False|   False|   False |

    enter python expression or type exit.
            > not (q or p and r)

    | p      | q      | r      | not (q or p and r) |
    |    True|    True|    True|              False |
    |    True|    True|   False|              False |
    |    True|   False|    True|              False |
    |    True|   False|   False|               True |
    |   False|    True|    True|              False |
    |   False|    True|   False|              False |
    |   False|   False|    True|               True |
    |   False|   False|   False|               True |
    
    enter python expression or type exit.
            > p <= q
    
    | p      | q      | p <= q |
    |    True|    True|   True |
    |    True|   False|  False |
    |   False|    True|   True |
    |   False|   False|   True |
    
    enter python expression or type exit.
            > xor((p <= q), r)
    
    | p      | q      | r      | xor((p <= q), r) |
    |    True|    True|    True|            False |
    |    True|    True|   False|             True |
    |    True|   False|    True|             True |
    |    True|   False|   False|            False |
    |   False|    True|    True|            False |
    |   False|    True|   False|             True |
    |   False|   False|    True|            False |
    |   False|   False|   False|             True |


