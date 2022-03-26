from datetime import timedelta, date
import os
import math


def prRed(skk):
    print("\033[91m {}\033[00m".format(skk))


def prGreen(skk):
    print("\033[92m {}\033[00m".format(skk))


def prYellow(skk):
    print("\033[93m {}\033[00m".format(skk))


def prLightPurple(skk):
    print("\033[94m {}\033[00m".format(skk))


def prCyan(skk):
    print("\033[96m {}\033[00m".format(skk))


cwd = os.getcwd()


def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)


###############################################################
###############   USER INPUT SECTION   ########################
###############################################################

token_worth = 145  # How much is the Token worth in USD?
node_count = 6  # How many nodes do you currently have?
claim_gas_fee = 40  # When claiming rewards from each node, this is an estimate of gas paid for each node to claim.
Ethereum_Node_Rewards = (
    5  # Total Rewards you could claim as of right now on the website.
)

start_date = date(2022, 3, 22)  # Todays date
end_date = date(2022, 12, 31)  # How long do  you want to project the data out to?

total_money_invested_at_this_point = (
    20000  ### How much money have you spent on the project already in USD
)
total_money_risk_already_cashed_out = (
    6500  ### How much money have you claimed and sold (risk off the table)
)


###############################################################
###############################################################
###############################################################

node_cost = token_worth * 10

initial_investment = (
    total_money_invested_at_this_point - total_money_risk_already_cashed_out
)

reward_per_node_eth = 0.092  # rewards per day for each node
cashed_out_tokens = 0
realized_profit = 0

# True == buy another node first
recompound_flag = True


prCyan(f"### Node to Start with: {node_count} ###")
prCyan(f"### initial_investment: $ {initial_investment} ###")
prCyan(f"### Price of the strong token: $ {token_worth} ###\n")

if recompound_flag:
    prCyan(f"### What are you doing first: Purchasing another node ###\n\n")
else:
    prCyan(f"### What are you doing first: Claim Tokens First ###\n\n")

for single_date in daterange(start_date, end_date):

    daily_reward = reward_per_node_eth * node_count
    Ethereum_Node_Rewards += daily_reward

    if Ethereum_Node_Rewards >= 10:
        # recompound_flag = False
        if recompound_flag:
            ## how many nodes to buy
            nodes_to_buy = math.floor(Ethereum_Node_Rewards / 10)
            prGreen(f"### Purchasing another node ###")
            prGreen(f"### Purchasing {nodes_to_buy} nodes ###\n")
            Ethereum_Node_Rewards -= nodes_to_buy * 10
            node_count += nodes_to_buy
            recompound_flag = False
        else:
            gas_fees = claim_gas_fee * node_count
            prYellow(f"### Pulling profits off the table ###")
            prYellow(
                f"### Pulling profits off the table; claiming {round(Ethereum_Node_Rewards,2)} tokens ###\n"
            )

            profit = ((Ethereum_Node_Rewards) * token_worth) - gas_fees
            cashed_out_tokens += Ethereum_Node_Rewards
            Ethereum_Node_Rewards = 0
            realized_profit += profit
            recompound_flag = True

    if recompound_flag:
        prGreen(
            f'{single_date.strftime("%Y-%m-%d")} Ethereum_Node_Rewards: {round(Ethereum_Node_Rewards,2)} --|-- NodeCount: {node_count} --|-- cashed_out_tokens: {round(cashed_out_tokens,2)} --|-- ROI_$: {round(realized_profit - initial_investment,2)}\n'
        )
    else:
        prYellow(
            f'{single_date.strftime("%Y-%m-%d")} Ethereum_Node_Rewards: {round(Ethereum_Node_Rewards,2)} --|-- NodeCount: {node_count} --|-- cashed_out_tokens: {round(cashed_out_tokens,2)} --|-- ROI_$: {round(realized_profit - initial_investment,2)}\n'
        )
