
'''
The take-out orders as they were entered into the system and given to the kitchen. (take_out_orders)
The dine-in orders as they were entered into the system and given to the kitchen. (dine_in_orders)
Each customer order (from either register) as it was finished by the kitchen. (served_orders)
Given all three lists, write a function to check that my service is first-come, first-served.
All food should come out in the same order customers requested it.
'''

def first_come_first_serve(take_out_orders, dine_in_orders, served_orders):
    take_out_count = 0
    dine_in_count = 0
    fifo = True
    for order in served_orders:
        if take_out_count < len(take_out_orders) and order == take_out_orders[take_out_count]: #and take_out_count < len(take_out_orders):
            take_out_count = take_out_count + 1
        elif dine_in_count < len(dine_in_orders) and order == dine_in_orders[dine_in_count]: #and dine_in_count < len(dine_in_orders):
            dine_in_count = dine_in_count + 1
        else:
            fifo = False
            break
    if fifo is False:
        print("The cafe is not first come first served")
    else:
        print("The cafe is first come first served")

if __name__ == '__main__':
    #take_out_orders = [17, 8, 24]
    #dine_in_orders = [12, 19, 2]
    #served_orders = [17, 8, 12, 19, 24, 2]
    take_out_orders = [1, 3, 5]
    dine_in_orders = [2, 4, 6]
    served_orders = [1, 2, 4, 6, 5, 3]
    first_come_first_serve(take_out_orders, dine_in_orders, served_orders)