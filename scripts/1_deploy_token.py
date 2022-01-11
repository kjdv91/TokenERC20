from brownie import accounts, config, TokenERC20

initialSupply = 100000000000000000
tokenName = "HEVADA"
tokenSymbol = "KJDV"


def main():
    account = accounts.add(config["wallets"]["from_key"])
    erc20 = TokenERC20.deploy(
        initialSupply, tokenName, tokenSymbol, {"from": account}, publish_source=True
    )
