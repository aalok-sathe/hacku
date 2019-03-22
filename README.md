# priority-sentiment
URichmond @ HackU '19

---
this program is intended to make the process of
sorting through user feedback, concerns, and
complaints easier for customer support divisions of
small companies that don't have the means to employ
a full-fledged customer support department.

the program helps automate the process of
prioritizing, visualizing, and tackling issues
users may be facing

### prerequisites
- `git clone https://github.com/aalok-sathe/hacku && cd hacku`
- Python 3.6 or higher (https://python.org/)
- StanfordCoreNLP
  - to download, do:
    ```bash
    wget https://nlp.stanford.edu/software/stanford-corenlp-full-2018-10-05.zip https://nlp.stanford.edu/software/stanford-english-corenlp-2018-10-05-models.jar```
  - install it:
  ```bash
  unzip stanford-corenlp-full-2018-10-05.zip
  mv stanford-english-corenlp-2018-10-05-models.jar stanford-corenlp-full-2018-10-05
  ```
  - start a server:
  ```bash
  cd stanford-corenlp-full-2018-10-05
  java -mx3g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer -timeout 10000
  ```
- `pycorenlp, nltk`, and other packages
  ```bash
  python3 -m pip install -r requirements.txt
  ```


### usage
```bash
    $ python3
    >>> import sentipriori
```
