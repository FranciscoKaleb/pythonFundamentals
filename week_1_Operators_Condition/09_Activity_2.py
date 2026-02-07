

# Calculate the total commission earned by Agent, unit manager, branch head in 5 years-
# -if client pays 100,000 per year

# Year 1	(Selling agent 25%, Unit Manager 15%, Branch Head 10%)	
# Year 2	(Selling agent 8%, Unit Manager 5%, Branch Head 2%)	
# Year 3	(Selling agent 5%, Unit Manager 4%, Branch Head 1%)	
# Year 4	(Selling agent 3%, Unit Manager 2%, Branch Head 0%)	
# Year 5	(Selling agent 2%, Unit Manager 1% Branch Head 0%)	

# no if else involve in this problem

print('-----------------[ 5 year Insurance Commission Calculation]------------------')
amount = 100000
agent_com = 0
unit_m_com = 0
branch_h_com = 0

# year 1
agent_com = agent_com + amount*0.25
unit_m_com = unit_m_com + amount*0.15
branch_h_com = branch_h_com + amount*0.1

#year 2
agent_com = agent_com + amount*0.08
unit_m_com = unit_m_com + amount*0.05
branch_h_com = branch_h_com + amount*0.02

#year 3
agent_com = agent_com + amount*0.05
unit_m_com = unit_m_com + amount*0.04
branch_h_com = branch_h_com + amount*0.01

#year 4
agent_com = agent_com + amount*0.03
unit_m_com = unit_m_com + amount*0.02

#year 5
agent_com = agent_com + amount*0.02
unit_m_com = unit_m_com + amount*0.01

print(f'5 years commission breakdown:')
print(f'Agent: {agent_com}')
print(f'Unit manager: {unit_m_com}')
print(f'Branch Head: {branch_h_com}')


# TEST CASE:
# 5 years commission breakdown:
# Agent: 43000.0
# Unit manager: 27000.0
# Branch Head: 13000.0