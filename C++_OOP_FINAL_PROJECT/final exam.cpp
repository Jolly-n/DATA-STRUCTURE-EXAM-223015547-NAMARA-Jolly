#include <iostream>
#include <iomanip>
using namespace std;

// --------- Struct: Date ---------
struct Date {
    int day, month, year;
    bool isEqual(const Date& other) const {
        return day == other.day && month == other.month && year == other.year;
    }
    
    void printDate() const {
        if (day < 10) cout << "0";
        cout << day << "/";
        if (month < 10) cout << "0";
        cout << month << "/" << year;
    }
};

// --------- Abstract Base Class: RoomBase ---------
class RoomBase {
protected:
    Date* reservedDates;
    int capacity;
    int reservedCount;
    string roomType;
    double pricePerNight;

public:
    RoomBase(const char* type, double price) : pricePerNight(price) {
        roomType = type;
        capacity = 10;
        reservedDates = new Date[capacity];
        reservedCount = 0;
    }

    virtual ~RoomBase() {
        delete[] reservedDates;
    }

    virtual bool isReserved(const Date* d) const = 0;
    virtual void reserve(const Date* d) = 0;
    
    const char* getRoomType() const { return roomType.c_str(); }
    double getPrice() const { return pricePerNight; }

    void showReservations() const {
        if (reservedCount == 0) {
            cout << "None";
            return;
        }
        for (int i = 0; i < reservedCount; ++i) {
            reservedDates[i].printDate();
            if (i < reservedCount - 1) cout << ", ";
        }
    }
    
    int getReservationCount() const { return reservedCount; }
};

// --------- Derived Class: BudgetRoom ---------
class BudgetRoom : public RoomBase {
public:
    BudgetRoom() : RoomBase("Budget Room", 45.0) {}

    bool isReserved(const Date* d) const override {
        Date* current = reservedDates;
        for (int i = 0; i < reservedCount; ++i, ++current) {
            if (current->isEqual(*d)) return true;
        }
        return false;
    }

    void reserve(const Date* d) override {
        if (isReserved(d)) {
            cout << " " << roomType << ": Date already reserved.\n";
            return;
        }
        if (reservedCount >= capacity) {
            capacity *= 2;
            Date* newDates = new Date[capacity];
            for (int i = 0; i < reservedCount; ++i)
                newDates[i] = reservedDates[i];
            delete[] reservedDates;
            reservedDates = newDates;
        }
        *(reservedDates + reservedCount) = *d;
        reservedCount++;
        cout << " " << roomType << ": Reservation added for ";
        d->printDate();
        cout << "\n";
    }
};

// --------- Derived Class: DeluxeRoom ---------
class DeluxeRoom : public RoomBase {
public:
    DeluxeRoom() : RoomBase("Deluxe Room", 140.0) {}

    bool isReserved(const Date* d) const override {
        Date* current = reservedDates;
        for (int i = 0; i < reservedCount; ++i, ++current) {
            if (current->isEqual(*d)) return true;
        }
        return false;
    }

    void reserve(const Date* d) override {
        if (isReserved(d)) {
            cout << " " << roomType << ": Date already reserved.\n";
            return;
        }
        if (reservedCount >= capacity) {
            capacity *= 2;
            Date* newDates = new Date[capacity];
            for (int i = 0; i < reservedCount; ++i)
                newDates[i] = reservedDates[i];
            delete[] reservedDates;
            reservedDates = newDates;
        }
        *(reservedDates + reservedCount) = *d;
        reservedCount++;
        cout << " " << roomType << ": Reservation added for ";
        d->printDate();
        cout << "\n";
    }
};

// --------- Globals ---------
RoomBase** rooms = NULL;
int* roomIDs = NULL;
int roomCount = 0;

// --------- Utility Functions ---------
void printSeparator(char ch = '=', int length = 50) {
    for (int i = 0; i < length; i++) {
        cout << ch;
    }
    cout << "\n";
}

void printHeader(const char* title) {
    cout << "\n";
    printSeparator('=', 30);
    cout << " " << title << " ";
    printSeparator('=', 30);
}

void checkAvailabilityForDate() {
    Date d;
    cout << "Enter date to check (day month year): ";
    cin >> d.day >> d.month >> d.year;
    
    cout << "\nAvailability for ";
    d.printDate();
    cout << ":\n";
    for (int i = 0; i < roomCount; ++i) {
        cout << "Room " << roomIDs[i] << ": ";
        if (rooms[i]->isReserved(&d)) {
            cout << "RESERVED\n";
        } else {
            cout << "AVAILABLE\n";
        }
    }
}

void showAllReservations() {
    printHeader("All Reservations");
    for (int i = 0; i < roomCount; ++i) {
        cout << "Room " << roomIDs[i] << " reservations: ";
        rooms[i]->showReservations();
        cout << "\n";
    }
}

void showHotelRooms() {
    printHeader("Hotel Rooms");
    for (int i = 0; i < roomCount; ++i) {
        cout << "Index " << i << ": " << rooms[i]->getRoomType() 
             << " " << roomIDs[i] << " - $" << fixed << setprecision(0) 
             << rooms[i]->getPrice() << "/night\n";
    }
}

// --------- Add Room ---------
void addRoom(RoomBase* newRoom, int roomID) {
    RoomBase** newRoomArray = new RoomBase*[roomCount + 1];
    int* newIDArray = new int[roomCount + 1];

    for (int i = 0; i < roomCount; ++i) {
        newRoomArray[i] = rooms[i];
        newIDArray[i] = roomIDs[i];
    }

    newRoomArray[roomCount] = newRoom;
    newIDArray[roomCount] = roomID;

    delete[] rooms;
    delete[] roomIDs;

    rooms = newRoomArray;
    roomIDs = newIDArray;
    roomCount++;

    cout << " Room added with ID: " << roomID << "\n";
}

// --------- Find Index by Room ID ---------
int findRoomIndex(int roomID) {
    for (int i = 0; i < roomCount; ++i) {
        if (roomIDs[i] == roomID)
            return i;
    }
    return -1;
}

// --------- Remove Room ---------
void removeRoom(int roomID) {
    int index = findRoomIndex(roomID);
    if (index == -1) {
        cout << " Room ID not found.\n";
        return;
    }

    cout << "\n";
    printSeparator('=', 30);
    cout << " Testing Room Removal ";
    printSeparator('=', 30);
    cout << "Removing room " << roomID << "\n";

    delete rooms[index];

    RoomBase** newRoomArray = new RoomBase*[roomCount - 1];
    int* newIDArray = new int[roomCount - 1];
    int j = 0;
    for (int i = 0; i < roomCount; ++i) {
        if (i == index) continue;
        newRoomArray[j] = rooms[i];
        newIDArray[j] = roomIDs[i];
        j++;
    }

    delete[] rooms;
    delete[] roomIDs;

    rooms = newRoomArray;
    roomIDs = newIDArray;
    roomCount--;

    cout << " Room with ID " << roomID << " removed.\n";
}

// --------- Input Date ---------
Date inputDate() {
    Date d;
    cout << "Enter reservation date (day month year): ";
    cin >> d.day >> d.month >> d.year;
    return d;
}

// --------- Main Menu Display ---------
void displayMenu() {
    cout << "\n";
    printSeparator('=', 40);
    cout << " HOTEL RESERVATION SYSTEM\n";
    printSeparator('=', 40);
    cout << "1. Add Budget Room\n";
    cout << "2. Add Deluxe Room\n";
    cout << "3. Remove Room by ID\n";
    cout << "4. Make Reservation by Room ID\n";
    cout << "5. Check Reservation by Room ID\n";
    cout << "6. View Reservations by Room ID\n";
    cout << "7. Check Availability for Date\n";
    cout << "8. Show All Reservations\n";
    cout << "9. Show Hotel Rooms\n";
    cout << "0. Exit\n";
    printSeparator('-', 40);
    cout << "Choice: ";
}

// --------- Main ---------
int main() {
    int choice;
    do {
        displayMenu();
        cin >> choice;

        if (choice == 1 || choice == 2) {
            int id;
            cout << "Enter new Room ID: ";
            cin >> id;
            if (findRoomIndex(id) != -1) {
                cout << " Room ID already exists.\n";
                continue;
            }
            if (choice == 1) addRoom(new BudgetRoom(), id);
            else addRoom(new DeluxeRoom(), id);
        }

        else if (choice == 3) {
            int id;
            cout << "Enter Room ID to remove: ";
            cin >> id;
            removeRoom(id);
        }

        else if (choice == 4 || choice == 5 || choice == 6) {
            int id;
            cout << "Enter Room ID: ";
            cin >> id;
            int index = findRoomIndex(id);
            if (index == -1) {
                cout << " Room ID not found.\n";
                continue;
            }

            if (choice == 4) {
                Date d = inputDate();
                rooms[index]->reserve(&d);
            } else if (choice == 5) {
                Date d = inputDate();
                if (rooms[index]->isReserved(&d))
                    cout << " Date is already reserved.\n";
                else
                    cout << " Date is available.\n";
            } else {
                cout << " Reservations for Room ID " << id << ":\n";
                rooms[index]->showReservations();
                cout << "\n";
            }
        }

        else if (choice == 7) {
            checkAvailabilityForDate();
        }

        else if (choice == 8) {
            showAllReservations();
        }

        else if (choice == 9) {
            showHotelRooms();
        }

        else if (choice == 0) {
            cout << "\n";
            printSeparator('-', 50);
            cout << "Process exited after execution with return value 0\n";
            cout << "Press any key to continue . . . |\n";
        }

        else {
            cout << " Invalid choice.\n";
        }

    } while (choice != 0);

    // Cleanup
    for (int i = 0; i < roomCount; ++i)
        delete rooms[i];
    delete[] rooms;
    delete[] roomIDs;

    return 0;
}
