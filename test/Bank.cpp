#include "Bank.hpp"  
#include <iostream>

Bank::Bank(string _accountId, double _amount)
{
	accountId = _accountId;
    amount = _amount;
}
	
Bank::~Bank()
{
	cout << "Done!" << endl;
}

string Bank::getAccountId()const{
    return accountId;
}

double Bank::getAmount()const{
    return amount;
}

void Bank::monthlySalary(){
    amount = amount + 4000;
}

void Bank::showAmount(){
    cout << amount << '$'<< endl;
}