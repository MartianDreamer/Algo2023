
class WordDictionary {

    private final WordDictionary[] children;
    private boolean end;

    public WordDictionary() {
        this.children = new WordDictionary[26];
        this.end = false;
    }

    public void addWord(String word) {
        addWord(word, 0);
    }

    public boolean search(String word) {
        return search(word, 0);
    }

    private boolean search(String word, int idx) {

        if (idx == word.length()) {
            return this.end;
        }

        char c = word.charAt(idx);

        if (c != '.') {
            return children[c - 'a'] != null && children[c - 'a'].search(word, idx + 1);
        }

        for (WordDictionary wd : children) {
            if (wd != null && wd.search(word, idx + 1)) {
                return true;
            }
        }
        return false;
    }

    private void addWord(String word, int idx) {
        if (idx == word.length()) {
            this.end = true;
            return;
        }
        char c = word.charAt(idx);
        if (this.children[c - 'a'] == null) {
            this.children[c - 'a'] = new WordDictionary();
        }
        this.children[c - 'a'].addWord(word, idx + 1);
    }

    public static void main(String[] args) {
        WordDictionary wd = new WordDictionary();
        wd.addWord("bad");
        wd.addWord("dad");
        wd.addWord("mad");
        System.out.println(wd.search("pad"));
        System.out.println(wd.search("bad"));
        System.out.println(wd.search(".ad"));
        System.out.println(wd.search("b.."));
    }

}
