#ifndef BANK_H
#define BANK_H

#include <string>
#include <iostream>
using namespace std;	
class Bank  
{
	private:
		string accountId;
		double amount;

	public:
		string getAccountId() const;
		double getAmount() const;
		void monthlySalary();
		void showAmount();
		Bank(string _accountId, double _amount);
		~Bank();

};
#endif