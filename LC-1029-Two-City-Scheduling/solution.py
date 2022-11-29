from typing import List


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:

        # sort by gratest possible savings first
        costs.sort(key=lambda c: abs(c[0] - c[1]), reverse=True)

        min_cost = 0

        max_num = len(costs) / 2
        group_a_cnt = 0
        group_b_cnt = 0

        for cost in costs:
            # possible case 1: group a full
            if group_a_cnt == max_num:
                group_to_add = 1  # group b index
                group_b_cnt += 1

            # possible case 2: group b full
            elif group_b_cnt == max_num:
                group_to_add = 0  # group a index
                group_a_cnt += 1
            else:

                # possible case 3: no group full
                # choose group greedily
                if cost[0] < cost[1]:
                    group_to_add = 0
                    group_a_cnt += 1
                else:
                    group_to_add = 1
                    group_b_cnt += 1

            min_cost += cost[group_to_add]

        return min_cost
