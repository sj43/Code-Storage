#include <bits/stdc++.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);


// Complete the decode function below.
// Complete the decode function below.
string decode(vector<string> codes, string encoded) {
    map<string, string> keycode;
    vector<string> words;
    string w;
    for (int i = 0;i < codes.size();i++) {
        for (stringstream sts(codes[i]);(sts >> w);) {
            if (w == "[newline]")
                w = "\n";
            words.push_back(w);
        }
        keycode.insert(pair<string, string>(words[1], words[0]));
        words.clear();
    }
    map<string, string>::iterator it;
    string result_string = "";
    int len = 0;
    int j=0;
    int len_encoded = encoded.length();
    while (j<len_encoded) {
        int k = 1;
        while (true) {
            string str3 = encoded.substr(j, k);
            it = keycode.find(str3);
            if (it != keycode.end()) {
                result_string.append(it->second);
                break;
            }
            k++;
            if (j + k > len_encoded) break;
        }
        j+=k;
    }

    return result_string;
}


int main()
{
    //ofstream fout(getenv("OUTPUT_PATH"));

    string codes_count_temp;
    getline(cin, codes_count_temp);

    int codes_count = stoi(ltrim(rtrim(codes_count_temp)));

    vector<string> codes(codes_count);

    for (int i = 0; i < codes_count; i++) {
        string codes_item;
        getline(cin, codes_item);

        codes[i] = codes_item;
    }

    string encoded;
    getline(cin, encoded);

    string res = decode(codes, encoded);

    cout<< res << "\n";
    //fout << res << "\n";

    //fout.close();

    return 0;
}

string ltrim(const string &str) {
    string s(str);

    s.erase(
        s.begin(),
        find_if(s.begin(), s.end(), not1(ptr_fun<int, int>(isspace)))
    );

    return s;
}

string rtrim(const string &str) {
    string s(str);

    s.erase(
        find_if(s.rbegin(), s.rend(), not1(ptr_fun<int, int>(isspace))).base(),
        s.end()
    );

    return s;
}
