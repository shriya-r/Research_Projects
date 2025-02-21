#include <iomanip>
#include <iostream>
#include <vector>
#include <fstream>
#include <sstream>
#include <cstring>
#include <string>
using namespace std;

int indexer(int num, vector<int> indexes) {
    bool found = false;
    for (int j = 0; j < indexes.size(); j++) { // output the data structure's index
        if (indexes[j] == num) {
            num = j;
            found = true;
            return num;
        }
    }
    return num;
}

void Updates(vector<pair<vector<int>, vector<vector<string>>>> &subroutines, vector<int> indexes, vector<vector<string>> &function_info, int num, double runtime) {
    vector<vector<string>> subroutine_list = subroutines[num].second;
    if (runtime != -1) {
        int number = 0;
        string called = function_info[num][2];
        string num1 = "";
        for (int j = 0; j < called.length(); j++) {
            if (called[j] == '+') {
                break;
            }
            num1 += called[j]; // get the number of calls in an int
        }
        number = stoi(num1);
        double run_time = number*runtime;
        function_info[num][0] = to_string(run_time); // update the self time, if necessary
    }
    double children = 0;
    for (int i = 0; i < subroutine_list.size(); i++) {
        // for each subroutine, add up the self + children times to be this function_info[num][1]
        int index = indexer(stoi(subroutine_list[i][3]), indexes);
        children += stod(function_info[index][1]);
        double run_time = stod(function_info[index][0]);
        string called = subroutine_list[i][2];
        string num_times = "";
        string total_times = "";
        for (int j = 0; j < called.length(); j++) {
            if (called[j] == '/') {
                num_times += total_times;
                total_times = "";
            }
            else {
                total_times += called[j]; // get the number of calls in an int
            }
        }
        int num_time = stoi(num_times);
        int total = stoi(total_times);
        run_time = (run_time * num_time) / total;
        children += run_time;
    }
    function_info[num][1] = to_string(children);
    // for each of the caller functions, find the num using its index from the indexes list
    vector<int> caller_list = subroutines[num].first;
    for (int i = 0; i < caller_list.size(); i++) {
        // for each caller, re-calculate the children runtime
        if (caller_list[i] != 0) {
            int index = indexer(caller_list[i], indexes);
            if (index != -1) {
                Updates(subroutines, indexes, function_info, index, -1);
            }
        }
    }
} // the function_info data structure has accurate updated values

int main(int argc, char *argv[])
{
    if (argc < 2) {
        cout << "Input a call graph text file.";
        return 0;
    }
    ifstream ifile(argv[1]);
    string line = "";
    string words = "";
    while (words != "index") {
        words = "";
        getline(ifile, line);
        stringstream ss;
        ss << line;
        ss >> words;
    }
    vector<vector<string>> function_info;
    vector<int> indexes;
    vector<pair<vector<int>, vector<vector<string>>>> subroutines;
    pair<vector<int>, vector<vector<string>>> entry;
    subroutines.push_back(entry);
    getline(ifile, line);
    int i = 0;
    bool isOver = false; // until the end of the call graph
    while (!isOver) {
        while (line[0] != '[') { // all the functions that are calling the primary function
            for (int j = 0; j < line.length(); j++) {
                if (line[j] == '[') {
                    string number = "";
                    for (int num1 = j+1; num1 < line.length(); num1++) {
                        if (line[num1] != ']') {
                            number += line[num1];
                        }
                    }
                    int index = stoi(number);
                    subroutines[i].first.push_back(index); // index to the function stored as an integer
                    break;
                }
                if (line[j] == '<') {
                    if (line[j+1] == 's' && line[j+2] == 'p' && line[j+3] == 'o') {
                        subroutines[i].first.push_back(0); // spontaneous, does not have any callers
                        break;
                    }
                }
            }
            cout << line << endl;
            getline(ifile, line);
        }
        if (line[0] == '[') { // the primary function in the entry
            vector<string> info;
            stringstream ss;
            ss << line;
            ss >> words; // index
            string indices = "";
            for (int w = 0; w < words.length(); w++) {
                if (words[w] != ']' && words[w] != '[') {
                    indices += words[w];
                }
            }
            indexes.push_back(stoi(indices));
            ss >> words;
            ss >> words; // time in self
            info.push_back(words);
            ss >> words; // time in children
            info.push_back(words);
            ss >> words; // called
            info.push_back(words);
            ss >> words; // name
            string temp;
            getline(ss, temp, '['); // the rest of the name until the '[' character
            words += temp;
            info.push_back(words);
            function_info.push_back(info);
            cout << line << endl;
            getline(ifile, line);
        }
        while (line[0] != '-') { // all the subroutines of the primary function
            vector<string> info;
            stringstream ss;
            ss << line;
            ss >> words; // time in self
            info.push_back(words);
            ss >> words; // time in children
            info.push_back(words);
            ss >> words; // called
            info.push_back(words);
            ss >> words; // name as an string
            string temp;
            getline(ss, temp, '['); // the rest of the name until the '[' character
            getline(ss, words, ']'); // the index of the function as a string
            info.push_back(words);
            subroutines[i].second.push_back(info);
            cout << line << endl;
            getline(ifile, line);
        }
        if (line[0] == '-') {
            subroutines.push_back(entry); // end of entry, so add another one
            i++;
            cout << line << endl;
            getline(ifile, line);
        }
        if (line == "") {
            isOver = true; // end of call graph
            subroutines.pop_back(); // remove the empty entry
        }
    }
    ifile.close();
    double time = 0;
    for (int k = 0; k < subroutines.size(); k++) {
        if (subroutines[k].first[0] == 0) {
            time += stod(function_info[k][0]);
            time += stod(function_info[k][1]); // total runtime
        }
    }
    cout << "Total Time: " << time << " seconds" << endl;
    bool done = false;
    while (!done) {
        cout << "Would you like to update any runtimes? (y/n)" << endl;
        char update;
        cin >> update;
        if (update == 'y') {
            cout << "Enter the index for the function you want to update:" << endl; // inputs for function
            int num;
            cin >> num;
            bool found = false;
            for (int j = 0; j < i; j++) {
                if (indexes[j] == num) {
                    num = j;
                    found = true;
                    break;
                }
            }
            if (found) {
                cout << "Enter the updated runtime" << endl;
                double run_time;
                cin >> run_time;
                Updates(subroutines, indexes, function_info, num, run_time); // update if valid inputs
                double updated_time = 0;
                for (int k = 0; k < subroutines.size(); k++) {
                    if (subroutines[k].first[0] == 0) {
                        updated_time += stod(function_info[k][0]);
                        updated_time += stod(function_info[k][1]);
                    }
                }
                cout << "Updated Total Time: " << updated_time << " seconds" << endl;
            }
            else {
                done = true; // if invalid inputs, then done
                break;
            }
        }
        else {
            done = true; // update each function until inputs are completed
            break;
        }
    }
    return 0;
}
