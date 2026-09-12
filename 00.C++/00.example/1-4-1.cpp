#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

std::vector<std::string> cal(std::vector<char> words, int lev, std::string tmp, std::vector<std::string>& rs)
{
    rs.push_back(tmp);
    if (lev >= words.size()) return rs;
    
    for (auto& x : words)
    {
        cal(words, lev + 1, tmp + x, rs);
    }
    return rs;
}

int solution(std::vector<char> words, std::string word)
{
    std::vector<std::string> word_list;
    cal(words, 0, "", word_list); // 참조로 전달
    auto it = std::find(word_list.begin(), word_list.end(), word);
    return (it != word_list.end()) ? std::distance(word_list.begin(), it) : -1;
}

int main(void)
{
    std::vector<char> words = {'A', 'E', 'I', 'O', 'U'};
    std::string word = "AAAE";
    int ret = solution(words, word);
    std::cout << ret << std::endl;
    return 0;
}