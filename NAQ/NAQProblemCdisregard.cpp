#include<bits/stdc++.h>
using namespace std;
int whiteOrBlack(int num){
  // return 1 if white, 0 if black
  if(num<=12){
    if(num==2 || num==5 || num==7 || num==10 || num==12){
      return 0;
    }
    else return 1;
  }
  int t = num%12;
  if(t==2 || t==5 || t==7 || t==10 || t==0){
    return 0;
  }
  else return 1;
}

int main(){
  // get inputs
  int ww,wb,bw,bb,L;
  cin>>ww>>wb>>bw>>bb>>L;
  for(int k=0;k<4;k++){
    int l,u;
    map<int,map<int*,int*>> erg;
    map<int*,int*> WorB;
    int a[2];
    int b[12];
    for(int i=0;i<ww;i++){
      cin>>l>>u;
      a[0]=l; a[1]=u;
      for(int j=0;j<12;j++){
        cin>>b[j];
      }
      WorB.insert(pair<int*,int*>(a,b));
      erg.insert(pair<int,map<int*,int*>>(k,WorB));
    }
  }
  // get input notes
  int firstNote, secondNote;
  int totalDifficulty=0;
  cin>>firstNote;
  int firstFinger = 1;
  while(cin>>secondNote){
    int heightChange = secondNote - firstNote;
    int colorOfFirstNote = whiteOrBlack(firstNote);
    int colorOfSecondNote = whiteOrBlack(secondNote);
    int secondFinger;
    int curDifficulty;
    // Black to Black
    if(colorOfFirstNote==0 && colorOfSecondNote==0){
      erg.find(3)->second;
    }
    // Black to White
    if(colorOfFirstNote==0 && colorOfSecondNote==1){

    }
    // White to Black
    if(colorOfFirstNote==1 && colorOfSecondNote==0){

    }
    // White to White
    if(colorOfFirstNote==1 && colorOfSecondNote==1){

    }

    totalDifficulty += curDifficulty;
    // prepare for next set of notes
    firstNote = secondNote;
    firstFinger = secondFinger;
  }
  cout<<totalDifficulty<<"\n";
  return 0;
}
