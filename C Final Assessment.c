#include <stdio.h>
#include <stdlib.h>
struct Employee
    {
        char name[10];
        char designation[10];
        char city[10];
    }emp;
void write()
{
    FILE *fptr;
    int i;
    fptr=fopen("employee.txt","w");
    if(fptr!=NULL)
    {
        printf("File creation successful..\n");
    }
     else
    {
        printf("File creation Failed.\n");
        return -1;
    }

    printf("\nEmployee details %d\n",(i+1));
    printf("Enter Employee Name: ");
    scanf("%s",emp.name);
    printf("Enter Designation: ");
    scanf("%s",emp.designation);
    printf("Enter City: ");
    scanf("%s",emp.city);

    fprintf(fptr, "Employee Name: %s\nEmployee Designation: %s\nEmployee City: %s\n",emp.name,emp.designation,emp.city);
    fclose(fptr);
}
void read(Employee)
{
    FILE *fptr;
    fptr=fopen("employee.txt","r");
	if(fptr==NULL)
    {
		printf("Unable to open\n");
		exit(1);
	}
	fread(&Employee,sizeof(struct Employee),1,fptr);
	printf("\nDetails from the file: \n");

	printf("Employee Name: %s\n",emp.name);
	printf("Employee Designation: %s\n",emp.designation);
	printf("Employee City: %s\n",emp.city);
//    FILE *fptr;
//    fptr=fopen("employee.txt","r");
//    char ch;
//    if(fptr==NULL)
//    {
//        printf("Unable to open\n");
//        exit(1);
//    }
//    printf("\nEmployee Information:\n");
//    while((ch=fgetc(fptr))!=EOF)
//    {
//        printf("%c", ch);
//    }
      fclose(fptr);
}

int main()
{
    write();
    read();
    return 0;
}

