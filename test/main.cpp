#include "Bank.hpp"
int	main(int argc, char **argv)
{
    Bank testAccount("aboly", 1000);
    testAccount.monthlySalary();
    testAccount.showAmount();


    return 0;
}

