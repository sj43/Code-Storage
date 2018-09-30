#include<iostream>
#include<vector>
#include<string>
using namespace std;


// the most obvious way of doing this

int getCharNumber(const char & c){
  int a = (int) 'a';
  int z = (int) 'z';
  int A = (int) 'A';
  int Z = (int) 'Z';
  int val = (int) c;
  if(a<=val && val<=z){
    return val-a;
  }
  else if(A<=c && c<=Z){
    return val-A;
  }
  else{
    return -1;
  }
}

vector<int> buildCharFrequencyTable(string phrase){
  vector<int> table(getCharNumber('z')-getCharNumber('a')+1,0);
  for(char & ch : phrase){
    int x = getCharNumber(ch);
    if(x!=-1){
      table[x]++;
    }
  }
  return table;
}

bool checkMaxOneOdd(vector<int> & table){
  bool foundOdd = false;
  for(auto count : table){
    if(count%2==1){
      if(foundOdd){
        return false;
      }
      foundOdd = true;
    }
  }
  return true;
}

bool isPermutationOfPalindrome1(const string & phrase){
  vector<int> table = buildCharFrequencyTable(phrase);
  return checkMaxOneOdd(table);
}


// lets optimize the first method with less code

bool isPermutationOfPalindrome(const string & phrase){
  int oddCount = 0;
  int frequency[26] = {0};
  int idx = 0;
  for(const char & c : phrase){
    idx = getCharNumber(c);
    if(idx!=-1){
      ++frequency[idx];
      if(frequency[idx]%2==1){
        ++oddCount;
      }else{
        --oddCount;
      }
    }
  }
  return oddCount<=1;
}


// Lets optimize more by using a bitvector! Checking if the resulting bitVector has zero or only
// one bit toggled to 1 (as that is the condition for possible permutation to palindrome)

int toggle(int bitVector, int index){
  if(index < 0){
    return bitVector;
  }
  int mask = 1 << index;
  if((bitVector & mask) == 0){
    bitVector |= mask;
  }else{
    bitVector &= ~mask;
  }
  return bitVector;
}

bool isExactlyOneBitSet(int bitVector){
  return ((bitVector&(bitVector-1))==0);
}

bool isPermutationOfPalindrome3(const string & phrase){
  int bitVector = 0;
  int id = 0;
  for(const char & c : phrase){
    id = getCharNumber(c);
    bitVector = toggle(bitVector, id);
  }
  return (bitVector == 0 || isExactlyOneBitSet(bitVector));
}



int main(){
  string pali = "Rats live on no evil star";
  string isPermutation = isPermutationOfPalindrome1(pali) ? "yes":"no";
  cout<< isPermutation << endl;
  return 0;
}
