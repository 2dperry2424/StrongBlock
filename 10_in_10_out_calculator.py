# The intent of the script is only to provide investment calculations for strongblock.
# This file is not financial guidance in any way. 


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

token_worth = 145
node_count = 6
claim_gas_fee = 40
strong_tokens_in_wallet = 5


###############################################################
###############################################################
###############################################################

node_cost = token_worth * 10

#### USE IF STARTING ON YOUR FIRST NODE ###
# initial_investment = node_cost * node_count

#### USE IF YOUR ARE ALREADY INTO THE PROJECT AND KNOW HOW MUCH IS NEEDED FOR A COMPLETE ROI ####
total_money_invested_at_this_point = 20000
total_money_risk_already_cashed_out = 6500
initial_investment = (
    total_money_invested_at_this_point - total_money_risk_already_cashed_out
)


reward_per_node_eth = 0.092

cashed_out_tokens = 0
0.5
realized_profit = 0


start_date = date(2022, 3, 22)
end_date = date(2022, 12, 31)

# True == buy another nude first
recompound_flag = True


print(cwd)
file = f"{cwd}\\10_backin_10_claimed-out_____{node_count}-node-start.txt"
# file = f"{cwd}\\10_claimed-out_____{node_count}-node-start.txt"


with open(file, "w") as f:

    f.write(f"### Node to Start with: {node_count} ###\n")
    f.write(f"### investment: ${initial_investment} ###\n")
    f.write(f"### Price of the strong token: {token_worth} ###\n")

    prCyan(f"### Node to Start with: {node_count} ###")
    prCyan(f"### initial_investment: $ {initial_investment} ###")
    prCyan(f"### Price of the strong token: $ {token_worth} ###\n")
    if recompound_flag:
        f.write(f"### What are you doing first: Purchasing another node ###\n\n")
    else:
        f.write(f"### What are you doing first: Claim Tokens First ###\n\n")

    for single_date in daterange(start_date, end_date):

        daily_reward = reward_per_node_eth * node_count
        strong_tokens_in_wallet += daily_reward

        if strong_tokens_in_wallet >= 10:
            # recompound_flag = False
            if recompound_flag:
                ## how many nodes to buy
                nodes_to_buy = math.floor(strong_tokens_in_wallet / 10)
                print(nodes_to_buy)
                prGreen(f"### Purchasing another node ###")
                f.write(f"### Purchasing {nodes_to_buy} nodes ###\n")
                prGreen(f"### Purchasing {nodes_to_buy} nodes ###\n")
                strong_tokens_in_wallet -= nodes_to_buy * 10
                node_count += nodes_to_buy
                recompound_flag = False
            else:
                gas_fees = claim_gas_fee * node_count
                prYellow(f"### Pulling profits off the table ###")
                f.write(
                    f"### Pulling profits off the table; claiming {round(strong_tokens_in_wallet,2)} tokens ###\n"
                )
                prYellow(
                    f"### Pulling profits off the table; claiming {round(strong_tokens_in_wallet,2)} tokens ###\n"
                )

                profit = ((strong_tokens_in_wallet) * token_worth) - gas_fees
                cashed_out_tokens += strong_tokens_in_wallet
                strong_tokens_in_wallet = 0
                realized_profit += profit
                recompound_flag = True

        f.write(
            f'{single_date.strftime("%Y-%m-%d")} Reward_bank: {round(strong_tokens_in_wallet,2)} --|-- NodeCount: {node_count} --|-- cashed_out_tokens: {round(cashed_out_tokens,2)} --|-- ROI_$: {round(realized_profit - initial_investment,2)}\n'
        )
        if recompound_flag:
            prGreen(
                f'{single_date.strftime("%Y-%m-%d")} Reward_bank: {round(strong_tokens_in_wallet,2)} --|-- NodeCount: {node_count} --|-- cashed_out_tokens: {round(cashed_out_tokens,2)} --|-- ROI_$: {round(realized_profit - initial_investment,2)}\n'
            )
        else:
            prYellow(
                f'{single_date.strftime("%Y-%m-%d")} Reward_bank: {round(strong_tokens_in_wallet,2)} --|-- NodeCount: {node_count} --|-- cashed_out_tokens: {round(cashed_out_tokens,2)} --|-- ROI_$: {round(realized_profit - initial_investment,2)}\n'
            )
