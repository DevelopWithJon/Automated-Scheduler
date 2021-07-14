## Automated-Scheduler

# Table of Contents
- General Info
- Schedule Conditions
- Method

# General Info
This tool is used to automate a simple schedule (Link to example schedule https://imgur.com/a/VhEljCZ). In the example, I made basic assignment for the first day of the week. As you can see shifts are broken down by hour from 8am-7pm and that there are 2 products being covered at any given time. From the times of 2-4 OM one person will handle both products. Creating a schedule can take up to an hour every week given everyones personal obligation and time off. This scheduler does most of the work in just seconds. 

# Schedule Conditions

- Assignee cannot work both the first shift and last shift in one day (both products)
- Assignee cannot work on 2 products at the same time (except 2-4)
- Assignee cannot work back to back shifts (considers both products)
- Assignee cannot work more than 2 shifts in one day

# Method 

To do this I used a recurive function algorithm that loops through a list of possible assigments. First it identifies an empty spot in the schedule, then choose an assignment, validates the choice through all the conditions. Because of the recursive design, the program can make decisions and correct mistake at each assignment as well as look back for a better choice.

