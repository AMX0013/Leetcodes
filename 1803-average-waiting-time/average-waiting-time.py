class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        chef_ready_time = customers[0][0]
        # chef_ready_time = 0
        total_wait = 0
        for customer in customers:
            print("Chef ready at", chef_ready_time)
            # print(customer)
            arrival, dur = customer[0], customer[1]

            
            after_start_delay = max(chef_ready_time - arrival,0 ) + dur 
            print("delay for customer ", customer, "is:"  , after_start_delay)

            chef_ready_time = max(chef_ready_time, arrival) + dur
            # total_wait += before_start_delay + after_start_delay
            total_wait += after_start_delay


        return total_wait/len(customers)

