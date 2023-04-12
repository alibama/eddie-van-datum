Running this app - type 
"streamlit run stream.py" in the terminal below

current chatgpt prompts are

1) can you provide a schema diagram for the edgar filings required by the sec?
                       +------------+
                       | Submission |
                       +------------+
                              |
                     +------------+
                     |  Filing    |
                     +------------+
                           /   \
                          /     \
                         /       \
               +------------+ +------------+
               |   Header   | |   Footer   |
               +------------+ +------------+
                     |             |
                     |             |
               +------------+ +------------+
               |   Company  | |   Exhibit  |
               +------------+ +------------+
                     |             |
                     |             |
               +------------+
               |  Documents |
               +------------+

In this schema, a "Submission" represents the overall package of information being submitted to the SEC. A Submission may contain one or more "Filings", each of which pertains to a specific company, form type, and reporting period.

Each Filing contains a "Header" and "Footer", which provide basic information about the filing such as the company name, reporting period, and form type. The Filing also includes a "Company" section, which contains information about the company submitting the filing, and an "Exhibit" section, which may include additional information or exhibits related to the filing.

The most important part of a filing is the "Documents" section, which contains the actual information being submitted to the SEC. This may include financial statements, disclosures, or other information required by SEC regulations.

Note that this is a simplified schema, and there may be additional sections or elements included in specific filings depending on the form type and reporting requirements.

what are the fields in the exhibits sections?

The contents of the "Exhibits" section of an SEC filing can vary depending on the specific filing and the nature of the exhibit being included. Generally speaking, an exhibit is a document or other piece of information that is not already included in the main body of the filing, but which is necessary to provide additional context or support for the information presented in the filing.

Some of the common types of exhibits that may be included in an SEC filing, along with the fields that may be included in each exhibit, are:

Financial statements: Typically include fields such as balance sheet, income statement, cash flow statement, and notes to the financial statements.

Legal agreements: May include fields such as parties involved, effective date, termination date, scope of the agreement, and any obligations or commitments that result from the agreement.

Material contracts: May include fields such as parties involved, effective date, termination date, scope of the contract, and any obligations or commitments that result from the contract.

Corporate governance documents: May include fields such as company bylaws, articles of incorporation, and other documents that govern the operation of the company.

Investor presentations: May include fields such as company overview, financial performance, growth strategy, and risk factors.

Other supporting materials: May include any other documents or information that the filer believes will be helpful in providing context or support for the information presented in the filing.

It's important to note that the specific fields included in an exhibit can vary widely depending on the nature of the exhibit and the requirements of the SEC.

*now to the software development*

please write a streamlit python app that creates a user interface to gather this information and then print it to the screen after the user hits submit 

(renders the majority of the code)

 this is great - can you build out conditional forms specific selection box - the 10-K, 10-Q, 8-K, and S-1
and lastly

can you add another form field for users to upload documents into that uploads files and pins them to pinata through an api?



2) what are the fields in the exhibits sections?


# Run Streamlit on Codespaces

Fork this repo, add your Streamlit app to it, and run it on GitHub Codespaces. :balloon:

## How it works

- `.devcontainer/devcontainer.json` creates a container with Python 3.7 and the latest version of Streamlit.
- It uses `forwardPorts` to make port `8501` inside the container available locally.
- Additionally, it sets the following configuration options in `.streamlit/config.toml` so that the app can be run on Codespaces without the addition of command line arguments:

    ```toml
    [server]
    enableCORS = false
    enableXsrfProtection = false
    ```

## Example usage

Fork this repo, open it on GitHub Codespaces, and run the following command to view the Hello app:

```bash
streamlit hello
```

![st-codespaces](https://user-images.githubusercontent.com/20672874/173758145-674a171a-60de-4850-a30f-ab8b921ffd43.gif)

If it weren't for the `.streamlit/config.toml` file, you would have had to run the following command:

```bash
streamlit hello --server.enableCORS false --server.enableXsrfProtection false
```
