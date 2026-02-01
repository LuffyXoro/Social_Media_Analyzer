from preprocessing.clean_text import clean_text

def test_clean_text_removes_urls():
    text = "!!!Http"
    assert clean_text(text)=="http"

def test_clean_text_removes_html_tags():
    text = "<b>Bold Text</b>"
    assert clean_text(text)=="bold text"

def test_clean_text_empty_string():
    text = ""
    assert clean_text(text)=="" 

if __name__ == "__main__":
    test_clean_text_removes_urls()
    test_clean_text_removes_html_tags()
    test_clean_text_empty_string()
    print("All tests passed.")




