#include <stdio.h>
#include <vector>
#include <algorithm>
using namespace std;

int n;
int map[25][25];
int dir[4][2] = { {-1,0},{1,0},{0,-1},{0,1} };
int que[50];
char buf[26];

int dfs(int x, int y) {
    int cnt = 1;
    map[x][y] = 2;

    for (int i = 0; i < 4;++i) {
        int xx = x + dir[i][0];
        int yy = y + dir[i][1];

        if (xx < 0 || xx >= n || yy < 0 || yy >= n)
            continue;
        if (map[xx][yy] != 1)
            continue;

        cnt += dfs(xx, yy);
    }
    return cnt;
}

int main() {
    scanf("%d", &n);

    for (int i = 0; i < n; ++i) {
        scanf("%s", buf);
        for (int j = 0; j < n; ++j)
            map[i][j] = buf[j] - '0';
    }

    int cnt = 0;
    for (int i = 0; i < n; ++i)
        for (int j = 0; j < n; ++j)
            if (map[i][j] == 1)
                que[cnt++] = dfs(i, j);

    printf("%d\n", cnt);
    sort(que, que + cnt);
    for (int i = 0; i < cnt; ++i)
        printf("%d\n", que[i]);

    return 0;
}
