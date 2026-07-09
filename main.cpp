
// Name: Mpho
// Surname: Moilwa
// Student Number: 55794378

#include <iostream>
#include <string>
#include <cctype>
using namespace std;


void displayStudents(string surnames[], int ids[], int count) {
    cout << "\nStudent List:" << endl;
    for (int i = 0; i < count; i++) {
        cout << i + 1 << ". " << surnames[i] << " - " << ids[i] << endl;
    }
}


int checkSurnames(string surnames[], int ids[], int count) {
    int invalidCount = 0;
    cout << "\nSurname Check:" << endl;

    for (int i = 0; i < count; i++) {
        bool isValid = true;

        // Check length
        if (surnames[i].length() < 3) {
            isValid = false;
        }

        // Check for digits
        for (char c : surnames[i]) {
            if (isdigit(c)) {
                isValid = false;
                break;
            }
        }

        // Display result
        cout << surnames[i] << " (" << ids[i] << "): ";
        if (isValid) {
            cout << "Valid surname" << endl;
        } else {
            cout << "Invalid surname" << endl;
            invalidCount++;
        }
    }

    return invalidCount;
}


void sortStudents(string surnames[], int ids[], int count) {
    for (int i = 0; i < count - 1; i++) {
        for (int j = i + 1; j < count; j++) {
            if (surnames[j] < surnames[i]) {

                string tempName = surnames[i];
                surnames[i] = surnames[j];
                surnames[j] = tempName;


                int tempId = ids[i];
                ids[i] = ids[j];
                ids[j] = tempId;
            }
        }
    }

    cout << "\nSorted Students:" << endl;
    for (int i = 0; i < count; i++) {
        cout << i + 1 << ". " << surnames[i] << " - " << ids[i] << endl;
    }
}

int main() {
    string surnames[15];
    int ids[15];
    int count = 0;


    while (count < 15) {
        string surname;
        cout << "Enter surname: ";
        cin >> surname;

        if (surname == "X" || surname == "x") {
            break;  // terminate input
        }

        int id;
        cout << "Enter ID: ";
        cin >> id;

        surnames[count] = surname;
        ids[count] = id;
        count++;
    }

    // Display all students
    displayStudents(surnames, ids, count);


    int invalidCount = checkSurnames(surnames, ids, count);
    cout << "\nNumber of invalid surnames: " << invalidCount << endl;


    sortStudents(surnames, ids, count);

    return 0;
}