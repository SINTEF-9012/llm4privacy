def get_context(prompt_id):
    if prompt_id == 1:
        return [{"role": "system", "content": PROMPT_1}]
    elif prompt_id == "I":
        return [{"role": "system", "content": PROMPT_I}]
    elif prompt_id == "II":
        return [{"role": "system", "content": PROMPT_II}]
    elif prompt_id == "III":
        return [{"role": "system", "content": PROMPT_III}]
    elif prompt_id == "Ia":
        return [{"role": "system", "content": PROMPT_Ia}]
    elif prompt_id == "IIa":
        return [{"role": "system", "content": PROMPT_IIa}]
    elif prompt_id == "IIIa":
        return [{"role": "system", "content": PROMPT_IIIa}]
    elif prompt_id == "IV":
        return [{"role": "system", "content": PROMPT_IV}]
    elif prompt_id == "IVa":
        return [{"role": "system", "content": PROMPT_IVa}]
    elif prompt_id == "Va":
        return [{"role": "system", "content": PROMPT_Va}]
    elif prompt_id == "VIa":
        return [{"role": "system", "content": PROMPT_VIa}]
    elif prompt_id == "VIIa":
        return [{"role": "system", "content": PROMPT_VIIa}]
    elif prompt_id == "VIIIa":
        return [{"role": "system", "content": PROMPT_VIIIa}]
    elif prompt_id == "IXa":
        return [{"role": "system", "content": PROMPT_IXa}]
    elif prompt_id == "Xa":
        return [{"role": "system", "content": PROMPT_Xa}]
    elif prompt_id == "XIa":
        return [{"role": "system", "content": PROMPT_XIa}]
    elif prompt_id == "XIIa":
        return [{"role": "system", "content": PROMPT_XIIa}]
    elif prompt_id == "XIIIa":
        return [{"role": "system", "content": PROMPT_XIIIa}]
    elif prompt_id == "COT1":
        return [{"role": "system", "content": PROMPT_COT1}]
    elif prompt_id == "COT2":
        return [{"role": "system", "content": PROMPT_COT2}]
    else:
        raise NotImplementedError()


PROMPT_1 = """
Hi, can we do an exercise related to data privacy? Many websites have the "privacy policy", and a paper proposed that there are 10 categories of data practice in such privacy contents:

1. First Party Collection/Use: how and why a
service provider collects user information.
2. Third Party Sharing/Collection: how user information may be shared with or collected by
third parties.
3. User Choice/Control: choices and control
options available to users.
4. User Access, Edit, & Deletion: if and how
users may access, edit, or delete their information.
5. Data Retention: how long user information is
stored.
6. Data Security: how user information is protected.
7. Policy Change: if and how users will be informed about changes to the privacy policy.
8. Do Not Track: if and how Do Not Track signals3
for online tracking and advertising are
honored.
9. International & Specific Audiences: practices
that pertain only to a specific group of users
(e.g., children, Europeans, or California residents).
10. Other: additional sub-labels for introductory or general text, contact information, and
practices not covered by the other categories.

I have a specific task for you: The user will give you a sentence from some privacy contents, and you tell them which category of practices this sentence may contain. Pleasy only respond with the category.
"""

# Prompt I: Data category title
PROMPT_I = """
Websites and digital products have privacy policies. Each sentence in these privacy policies can be annotated with one or more data practice.  A data practice means how the data is used and processed by an organization. In current context, a data practice belongs to one of the following data practice categories. 
 
1. First Party Collection/Use.
2. Third Party Sharing/Collection.
3. User Choice/Control.
4. User Access, Edit, and Deletion.
5. Data Retention.
6. Data Security. 
7. Policy Change.
8. Do Not Track.
9. International and Specific Audiences.
10. Other.
 
I have a specific task for you: The user will give you a sentence from some privacy contents, and you tell them which category of practices this sentence may contain. Please only respond with the category.
"""

# Data category title with OPP-115 description
PROMPT_II = """
Websites and digital products have privacy policies. Each sentence in these privacy policies can be annotated with one or more data practice.  A data practice means how the data is used and processed by an organization. In current context, a data practice belongs to one of the following data practice categories. 
 
1. First Party Collection/Use: how and why a service provider collects user information.
2. Third Party Sharing/Collection: how user information may be shared with or collected by
third parties.
3. User Choice/Control: choices and control options available to users.
4. User Access, Edit, and Deletion: if and how users may access, edit, or delete their information.
5. Data Retention: how long user information is stored.
6. Data Security: how user information is protected.
7. Policy Change: if and how users will be informed about changes to the privacy policy.
8. Do Not Track: if and how Do Not Track signals for online tracking and advertising are
honored.
9. International and Specific Audiences: practices that pertain only to a specific group of users (e.g., children, Europeans, or California residents).
10. Other: additional sub-labels for introductory or general text, contact information, and
practices not covered by the other categories.
 
I have a specific task for you: The user will give you a sentence from some privacy contents, and you tell them which category of practices this sentence may contain. Please only respond with the category.
"""

# Data category title with extended description
PROMPT_III = """
Websites and digital products have privacy policies. A data practice means how the data is used and processed by an organization. A sentence (policy segment) in a privacy policy can be annotated with one of the following nine data practice categories:

    Category 1. First Party Collection/Use: This category is about how and why a service provider collects user information. In first party collection, the service provider that owns or operates the website/platform/service directly collects data from individuals. For instance, when a customer engages with the services of company A, company A collects data such as the products they have browsed, their purchasing choices, or their behavior patterns. When company A makes a product recommendation to a customer based on this data, it can be referred to as first-party advertising. In this case, collection and use of personal data is identified as first party data collection and use. In privacy policies, certain keywords and phrases can help to identify if the data collection or use is first party. For example: "We collect", "Data you provide", "Information we collect", "Our servers", "Our cookies", "We use your data" "Data collected from your interaction with our services", "Information you submit", “We restrict access to personal information to our employees, contractors, and agents”, etc. The following three policy segments are example segments classified as First Party Collection/Use.

    Category 2. Third Party Sharing/Collection: This category is about how user information may be shared with or collected by third parties. In third party sharing/collection an entity other than the service provider collects data from users through the service provider's platform. Third parties could include advertisers, ad network companies, analytic companies, or partner services that have their own data collection and privacy practices. Third-party entities often work with a variety of first-party websites, collecting information on user profiles from diverse sources, including news, weather, entertainment, and travel websites. For instance, if a customer uses Amazon.com's services and Amazon utilizes details about the user that have been collected by companies other than itself, this is known as third-party data collection and use. In privacy policies, certain keywords and phrases can help to identify if the data collection or use is third-party. For example: "Third-party providers", "External partners", "Ad networks", "Data we share" "Cookies from third-party advertisers", "Third-party cookies", "Third-party analytics", "Our partners’ services", “data processors”, etc. The following five policy segments are example segments classified as Third Party Sharing/Collection.

    Category 3. User Choice/Control: This category is about choices and control options available to users. Choice means giving individuals options as to how their personal information may be used. Specifically, choice relates to secondary uses of information—that is, uses beyond those necessary to complete the contemplated transaction. Control means privacy controls that allow individuals to manage use and sharing of their data. Example for choice/control can be following: “opt-in”, “opt-out”, “cookie preference” (functional/recommended/essential/performance/advertising), “location data controls”, “privacy control”, “communication preference”, “do-not-track”, “do-not-sell”, “withdraw consent”, etc. The following three policy segments are example segments classified as User Choice/Control.

    Category 4. User Access, Edit, and Deletion: This category is about if and how users may access, edit, or delete their information. These are privacy rights-based choices. In privacy policies such provision can be found in the following keywords and phrases: "right to access", “rights you have”, "request a copy", "view your information", "download your data", "personal data report", "obtain a copy", “how do I change my information”, “ how can I move my information”, "data subject access request", “delete information”, etc. The following three policy segments are example segments classified as User Access, Edit, and deletion.

    Category 5. Data Retention: This category is about how long user information is stored. Retention period outlines the time period for which personal information is stored and when it will be deleted or anonymized. Here are examples of some keywords, terms, and phrases that commonly identify "data retention" in privacy policies: "retention period", "how long we keep your data", “retaining your information”, "storage duration", "duration", "keep your data", “hold your information”, “hold your information any longer than we have to”, etc. The following three policy segments are example segments classified as Data Retention.

    Category 6. Data Security: This category is about how user information is protected. In particular, it means the security measures that ensure security of personal data, including encryption or storage of data on secure servers. It also includes processing user data to improve safety and reliability of products, services, and users. Here are examples of some keywords, terms, and phrases that commonly identify "data security" in privacy policies: “security, fraud and abuse prevention”, “information security”, “security tips”, “security measures”, “security features”, “security partners”, “security controls”, “encryption”, “data breach procedure”, “secure server”, “firewalls and antivirus software”, “appropriate technical and organizational measures to safeguard personal information”, etc. The following three policy segments are example segments classified as Data Security.

    Category 7. Policy Change: This category is about if and how users will be informed about changes to the privacy policy. Here are examples of some keywords, terms, and phrases that commonly identify "policy change" in privacy policies: “notify you about upcoming changes”, “we change this privacy policy from time to time”, “email notification of privacy policy changes”, “notification of changes”, “revisions to this policy”, “policy update alert”, “how we will inform you”, etc. The following three policy segments are example segments classified as Policy Change.

    Category 8. Do Not Track: This category is about if and how Do Not Track signals for online tracking and advertising are honored. Examples of keywords, terms, and phrases that commonly reflect "Do Not Track" in privacy policies include: “you can switch off some cookies and similar tracking technologies”, “online tracking preferences”, “do not track”, “behavioral tracking opt-out”, “opting-out of tracking”, etc. The following three policy segments are example segments classified as DO Not Track.

    Category 9. International and Specific Audiences: This category is about practices that pertain only to a specific group of users (e.g., children, Europeans, or California residents). It outlines specific provisions that apply exclusively to certain categories of users, such as children, residents of Europe, or individuals living in California. The privacy policy includes clauses for these distinct user groups. Here are examples of some keywords, terms, and phrases that commonly identify international audiences or specific audiences in privacy policies: “child permissions”, “special protection of children's personal data”, “age-specific guidelines”, “kids profile”, “parental consent”, “children and teens”, “international users”, “regional laws”, “GDPR” (General Data Protection Regulation for European users), “CCPA” (California Consumer Privacy Act for California residents), “COPPA” (Children's Online Privacy Protection Act), “ CIPA” (Children’s Internet Protection Act in United States), “specific audience considerations”, “disclosure and international transfers”, “supplemental privacy disclosures for certain services and regions”, etc. The following three policy segments are example segments classified as International and Specific Audiences.

    I have a specific task for you: I will give you a sentence from a privacy policy, and you will classify the sentence with one of these nine data practice categories. Please respond only with one of the nine categories for each sentence.
"""

# Prompt I: Data category title without Other category
PROMPT_Ia = """
Websites and digital products have privacy policies. Each sentence in these privacy policies can be annotated with one or more data practice.  A data practice means how the data is used and processed by an organization. In current context, a data practice belongs to one of the following data practice categories. 
 
1. First Party Collection/Use.
2. Third Party Sharing/Collection.
3. User Choice/Control.
4. User Access, Edit, and Deletion.
5. Data Retention.
6. Data Security. 
7. Policy Change.
8. Do Not Track.
9. International and Specific Audiences.

I have a specific task for you: The user will give you a sentence from some privacy contents, and you tell them which category of practices this sentence may contain. Please only respond with the category.
"""

# Data category title with OPP-115 description without Other category
PROMPT_IIa = """
Websites and digital products have privacy policies. Each sentence in these privacy policies can be annotated with one or more data practice.  A data practice means how the data is used and processed by an organization. In current context, a data practice belongs to one of the following data practice categories. 
 
1. First Party Collection/Use: how and why a service provider collects user information.
2. Third Party Sharing/Collection: how user information may be shared with or collected by
third parties.
3. User Choice/Control: choices and control options available to users.
4. User Access, Edit, and Deletion: if and how users may access, edit, or delete their information.
5. Data Retention: how long user information is stored.
6. Data Security: how user information is protected.
7. Policy Change: if and how users will be informed about changes to the privacy policy.
8. Do Not Track: if and how Do Not Track signals for online tracking and advertising are
honored.
9. International and Specific Audiences: practices that pertain only to a specific group of users (e.g., children, Europeans, or California residents).

I have a specific task for you: The user will give you a sentence from some privacy contents, and you tell them which category of practices this sentence may contain. Please only respond with the category.
"""

# Data category title with extended description without Other category
PROMPT_IIIa = """
Websites and digital products have privacy policies. Each sentence in these privacy policies can be annotated with one or more data practice. A data practice means how the data is used and processed by an organization. In current context, a data practice belongs to one of the following data practice categories. 
 
1. First Party Collection/Use: how and why a service provider collects user information. In first party collection the service provider that owns or operates the website/platform/service directly collect data from individuals. 
2. Third Party Sharing/Collection: how user information may be shared with or collected by
third parties. In third party sharing/collection an entity other than the service provider collects data from users through the service provider's platform. Third parties could include advertisers, analytic companies, or partner services that have their own data collection and privacy practices.
3. User Choice/Control: choices and control options available to users. Choice means giving individuals options as to how their personal information may be used. Specifically, choice relates to secondary uses of information—that is, uses beyond those necessary to complete the contemplated transaction. Control means privacy controls that allow individuals to manage use and sharing of their data. 
4. User Access, Edit, and Deletion: if and how users may access, edit, or delete their information.
5. Data Retention: how long user information is stored. All data should have retention period associated with it, retention period means maximum period the data will be stored. 
6. Data Security: how user information is protected. In particular, it means the security measures that ensures security of personal data, including encryption or storage of data on secure servers. 
7. Policy Change: if and how users will be informed about changes to the privacy policy.
8. Do Not Track: if and how Do Not Track signals for online tracking and advertising are
honored.
9. International and Specific Audiences: practices that pertain only to a specific group of users (e.g., children, Europeans, or California residents).
 
I have a specific task for you: The user will give you a sentence from some privacy contents, and you tell them which category of practices this sentence may contain. Please only respond with the category.
"""
# Data category title with extended description and examples
PROMPT_IV = """
Websites and digital products have privacy policies. I will give you a dataset of privacy policies, where privacy policies are divided into paragraph length segments and each segment is annotated with one or more data practice. A data practice means how the data is used and processed by an organization. In current context, a data practice belongs to one of the following data practice categories.

1. First Party Collection/Use: how and why a service provider collects user information. In first party collection the service provider that owns or operates the website/platform/service directly collect data from individuals. For instance, when a customer engages with the services of Amazon.com, Amazon collects data such as the products they have browsed, their purchasing choices, or their behavior patterns. When Amazon makes a product recommendation to customer based on this data, it can be referred to as first-party advertising. In this case, collection and use of personal data is identified as first party data collection and use. In privacy policies, certain keywords and phrases can help to identify if the data collection or use is first-party. For example: "We collect", "Data you provide", "Information we collect", "Our servers", "Our cookies", "We use your data" "Data collected from your interaction with our services", "Information you submit", “We restrict access to personal information to our employees, contractors, and agents”, etc.
2. Third Party Sharing/Collection: how user information may be shared with or collected by third parties. In third party sharing/collection an entity other than the service provider collects data from users through the service provider's platform. Third parties could include advertisers, ad network companies, analytic companies, or partner services that have their own data collection and privacy practices. Third-party entities often work with a variety of first-party websites, collecting information on user profiles from diverse sources, including news, weather, entertainment, and travel websites. For instance, if a customer uses Amazon.com's services and Amazon utilizes details about the user that have been collected by companies other than itself, this is known as third-party data collection and use. In privacy policies, certain keywords and phrases can help to identify if the data collection or use is third-party. For example: "Third-party providers", "External partners", "Ad networks", "Data we share" "Cookies from third-party advertisers", "Third-party cookies", "Third-party analytics", "Our partners’ services", “data processors”, etc.
3. User Choice/Control: choices and control options available to users. Choice means giving individuals options as to how their personal information may be used. Specifically, choice relates to secondary uses of information—that is, uses beyond those necessary to complete the contemplated transaction. Control means privacy controls that allow individuals to manage use and sharing of their data. Example for choice/control can be following: “opt-in”, “opt-out”, “cookie preference” (functional/recommended/essential/performance/advertising), “location data controls”, “privacy control”, “communication preference”, “do-not-track”, “do-not-sell”, “withdraw consent”, etc.
4. User Access, Edit, and Deletion: if and how users may access, edit, or delete their information. These are privacy rights-based choices. In privacy policies such provision can be found in the following keywords and phrases: "right to access", “rights you have”, "request a copy", "view your information", "download your data", "personal data report", "obtain a copy", “how do I change my information”, “ how can I move my information”, "data subject access request", “delete information”, etc.
5. Data Retention: how long user information is stored. Retention period outlines the time period for which personal information is stored and when it will be deleted or anonymized. Here are examples of some keywords, terms, and phrases that commonly identify "data retention" in privacy policies: "retention period", "how long we keep your data", “retaining your information”, "storage duration", "duration", "keep your data", “hold your information”, “hold your information any longer than we have to”, etc.
6. Data Security: how user information is protected. In particular, it means the security measures that ensures security of personal data, including encryption or storage of data on secure servers. It also includes processing user data to improve safety and reliability of products, services, and users. Here are examples of some keywords, terms, and phrases that commonly identify "data security" in privacy policies: “security, fraud and abuse prevention”, “information security”, “security tips”, “security measures”, “security features”, “security partners”, “security controls”, “encryption”, “data breach procedure”, “secure server”, “firewalls and antivirus software”, “appropriate technical and organizational measures to safeguard personal information”, etc.
7. Policy Change: if and how users will be informed about changes to the privacy policy. Here are examples of some keywords, terms, and phrases that commonly identify "policy change" in privacy policies: “notify you about upcoming changes”, “we change this privacy policy from time to time”, “email notification of privacy policy changes”, “notification of changes”, “revisions to this policy”, “policy update alert”, “how we will inform you”, etc.
8. Do Not Track: if and how Do Not Track signals for online tracking and advertising are honored. Examples of keywords, terms, and phrases that commonly reflect "Do Not Track" in privacy policies include: “you can switch off some cookies and similar tracking technologies”, “online tracking preferences”, “do not track”, “behavioral tracking opt-out”, “opting-out of tracking”, etc.
9. International and Specific Audiences: practices that pertain only to a specific group of users (e.g., children, Europeans, or California residents). This category outlines specific provisions that apply exclusively to certain categories of users, such as children, or residents of Europe, or individuals living in California. The privacy policy includes clauses for these distinct user groups. Here are examples of some keywords, terms, and phrases that commonly identify international audiences or specific audiences in privacy policies: “child permissions”, “special protection of children's personal data”, “age-specific guidelines”, “kids profile”, “parental consent”, “children and teens”, “international users”, “regional laws”, “GDPR” (General Data Protection Regulation for European users), “CCPA” (California Consumer Privacy Act for California residents), “COPPA” (Children's Online Privacy Protection Act), “ CIPA” (Children’s Internet Protection Act in United States), “specific audience considerations”, “disclosure and international transfers”, “supplemental privacy disclosures for certain services and regions”, etc.
10. Other: additional sub-labels for introductory or general text, contact information, and practices not covered by the other categories.

I have a specific task for you: The user will give you a sentence from some privacy contents, and you tell them which category of practices this sentence may contain. Please only respond with the category.
"""

# Data category title with extended description and examples without Other category
PROMPT_IVa = """
Websites and digital products have privacy policies. I will give you a dataset of privacy policies, where privacy policies are divided into paragraph length segments and each segment is annotated with one or more data practice. A data practice means how the data is used and processed by an organization. In current context, a data practice belongs to one of the following data practice categories.

1. First Party Collection/Use: how and why a service provider collects user information. In first party collection the service provider that owns or operates the website/platform/service directly collect data from individuals. For instance, when a customer engages with the services of Amazon.com, Amazon collects data such as the products they have browsed, their purchasing choices, or their behavior patterns. When Amazon makes a product recommendation to customer based on this data, it can be referred to as first-party advertising. In this case, collection and use of personal data is identified as first party data collection and use. In privacy policies, certain keywords and phrases can help to identify if the data collection or use is first-party. For example: "We collect", "Data you provide", "Information we collect", "Our servers", "Our cookies", "We use your data" "Data collected from your interaction with our services", "Information you submit", “We restrict access to personal information to our employees, contractors, and agents”, etc.
2. Third Party Sharing/Collection: how user information may be shared with or collected by third parties. In third party sharing/collection an entity other than the service provider collects data from users through the service provider's platform. Third parties could include advertisers, ad network companies, analytic companies, or partner services that have their own data collection and privacy practices. Third-party entities often work with a variety of first-party websites, collecting information on user profiles from diverse sources, including news, weather, entertainment, and travel websites. For instance, if a customer uses Amazon.com's services and Amazon utilizes details about the user that have been collected by companies other than itself, this is known as third-party data collection and use. In privacy policies, certain keywords and phrases can help to identify if the data collection or use is third-party. For example: "Third-party providers", "External partners", "Ad networks", "Data we share" "Cookies from third-party advertisers", "Third-party cookies", "Third-party analytics", "Our partners’ services", “data processors”, etc.
3. User Choice/Control: choices and control options available to users. Choice means giving individuals options as to how their personal information may be used. Specifically, choice relates to secondary uses of information—that is, uses beyond those necessary to complete the contemplated transaction. Control means privacy controls that allow individuals to manage use and sharing of their data. Example for choice/control can be following: “opt-in”, “opt-out”, “cookie preference” (functional/recommended/essential/performance/advertising), “location data controls”, “privacy control”, “communication preference”, “do-not-track”, “do-not-sell”, “withdraw consent”, etc.
4. User Access, Edit, and Deletion: if and how users may access, edit, or delete their information. These are privacy rights-based choices. In privacy policies such provision can be found in the following keywords and phrases: "right to access", “rights you have”, "request a copy", "view your information", "download your data", "personal data report", "obtain a copy", “how do I change my information”, “ how can I move my information”, "data subject access request", “delete information”, etc.
5. Data Retention: how long user information is stored. Retention period outlines the time period for which personal information is stored and when it will be deleted or anonymized. Here are examples of some keywords, terms, and phrases that commonly identify "data retention" in privacy policies: "retention period", "how long we keep your data", “retaining your information”, "storage duration", "duration", "keep your data", “hold your information”, “hold your information any longer than we have to”, etc.
6. Data Security: how user information is protected. In particular, it means the security measures that ensures security of personal data, including encryption or storage of data on secure servers. It also includes processing user data to improve safety and reliability of products, services, and users. Here are examples of some keywords, terms, and phrases that commonly identify "data security" in privacy policies: “security, fraud and abuse prevention”, “information security”, “security tips”, “security measures”, “security features”, “security partners”, “security controls”, “encryption”, “data breach procedure”, “secure server”, “firewalls and antivirus software”, “appropriate technical and organizational measures to safeguard personal information”, etc.
7. Policy Change: if and how users will be informed about changes to the privacy policy. Here are examples of some keywords, terms, and phrases that commonly identify "policy change" in privacy policies: “notify you about upcoming changes”, “we change this privacy policy from time to time”, “email notification of privacy policy changes”, “notification of changes”, “revisions to this policy”, “policy update alert”, “how we will inform you”, etc.
8. Do Not Track: if and how Do Not Track signals for online tracking and advertising are honored. Examples of keywords, terms, and phrases that commonly reflect "Do Not Track" in privacy policies include: “you can switch off some cookies and similar tracking technologies”, “online tracking preferences”, “do not track”, “behavioral tracking opt-out”, “opting-out of tracking”, etc.
9. International and Specific Audiences: practices that pertain only to a specific group of users (e.g., children, Europeans, or California residents). This category outlines specific provisions that apply exclusively to certain categories of users, such as children, or residents of Europe, or individuals living in California. The privacy policy includes clauses for these distinct user groups. Here are examples of some keywords, terms, and phrases that commonly identify international audiences or specific audiences in privacy policies: “child permissions”, “special protection of children's personal data”, “age-specific guidelines”, “kids profile”, “parental consent”, “children and teens”, “international users”, “regional laws”, “GDPR” (General Data Protection Regulation for European users), “CCPA” (California Consumer Privacy Act for California residents), “COPPA” (Children's Online Privacy Protection Act), “ CIPA” (Children’s Internet Protection Act in United States), “specific audience considerations”, “disclosure and international transfers”, “supplemental privacy disclosures for certain services and regions”, etc.

I have a specific task for you: The user will give you a sentence from some privacy contents, and you tell them which category of practices this sentence may contain. Please only respond with the category.
"""

PROMPT_Va = """
Websites and digital products have privacy policies. A data practice means how the data is used and processed by an organization. A sentence (policy segment) in a privacy policy can be annotated with one of the following nine data practice categories:

    Category 1. First Party Collection/Use: This category is about how and why a service provider collects user information. In first party collection, the service provider that owns or operates the website/platform/service directly collects data from individuals. For instance, when a customer engages with the services of company A, company A collects data such as the products they have browsed, their purchasing choices, or their behavior patterns. When company A makes a product recommendation to a customer based on this data, it can be referred to as first-party advertising. In this case, collection and use of personal data is identified as first party data collection and use. In privacy policies, certain keywords and phrases can help to identify if the data collection or use is first party. For example: "We collect", "Data you provide", "Information we collect", "Our servers", "Our cookies", "We use your data" "Data collected from your interaction with our services", "Information you submit", “We restrict access to personal information to our employees, contractors, and agents”, etc. The following three policy segments are example segments classified as First Party Collection/Use.

    Example Policy Segment 1: “We collect the following categories of personal information about you: name, email address, profile information, payment details and device IDs.”
    Classification: First Party Collection/Use

    Example Policy Segment 2: “In order to provide personalized services, we process information including your usage data and preferences.”
    Classification: First Party Collection/Use

    Example Policy Segment 3: “We may also collect sensitive personal information such as information about your racial or ethnic origin, health, precise geolocation, social security number.”
    Classification: First Party Collection/Use

    Category 2. Third Party Sharing/Collection: This category is about how user information may be shared with or collected by third parties. In third party sharing/collection an entity other than the service provider collects data from users through the service provider's platform. Third parties could include advertisers, ad network companies, analytic companies, or partner services that have their own data collection and privacy practices. Third-party entities often work with a variety of first-party websites, collecting information on user profiles from diverse sources, including news, weather, entertainment, and travel websites. For instance, if a customer uses Amazon.com's services and Amazon utilizes details about the user that have been collected by companies other than itself, this is known as third-party data collection and use. In privacy policies, certain keywords and phrases can help to identify if the data collection or use is third-party. For example: "Third-party providers", "External partners", "Ad networks", "Data we share" "Cookies from third-party advertisers", "Third-party cookies", "Third-party analytics", "Our partners’ services", “data processors”, etc. The following five policy segments are example segments classified as Third Party Sharing/Collection.

    Example Policy Segment 1: “Our website uses third-party analytics services to help understand your usage of our services.”
    Classification: Third Party Sharing/Collection.

    Example Policy Segment 2: “We collect personal Information from third parties whose services you use to access, pay for, or interact with our service.”
    Classification: Third Party Sharing/Collection.

    Example Policy Segment 3: “We may collect personal information about you from other sources or service providers vendors, agents, and contractors that collect or provide personal information to us in connection with services they perform on our behalf.”
    Classification: Third Party Sharing/Collection.

    Example Policy Segment 4: “Cookies from third-party advertisers are used on our platform to deliver targeted advertisements based on your browsing history.”
    Classification: Third Party Sharing/Collection.

    Example Policy Segment 5: “Data we share with external partners includes your user profile and preferences to enhance your experience across partnered services.”
    Classification: Third Party Sharing/Collection.

    Category 3. User Choice/Control: This category is about choices and control options available to users. Choice means giving individuals options as to how their personal information may be used. Specifically, choice relates to secondary uses of information—that is, uses beyond those necessary to complete the contemplated transaction. Control means privacy controls that allow individuals to manage use and sharing of their data. Example for choice/control can be following: “opt-in”, “opt-out”, “cookie preference” (functional/recommended/essential/performance/advertising), “location data controls”, “privacy control”, “communication preference”, “do-not-track”, “do-not-sell”, “withdraw consent”, etc. The following three policy segments are example segments classified as User Choice/Control.

    Example Policy Segment 1: “You can control what information we use to show you advertisements by visiting your advertisement settings.”
    Classification: User Choice/Control

    Example Policy Segment 2: “If you wish to withdraw your consent at any time for any data processing we perform, you can do so through our user settings page under privacy control.”
    Classification: User Choice/Control

    Example Policy Segment 3: “You may choose to opt out of receiving behavioral advertisements, you will still see Advertisements, but they will not be behavioral advertisements.”
    Classification: User Choice/Control

    Category 4. User Access, Edit, and Deletion: This category is about if and how users may access, edit, or delete their information. These are privacy rights-based choices. In privacy policies such provision can be found in the following keywords and phrases: "right to access", “rights you have”, "request a copy", "view your information", "download your data", "personal data report", "obtain a copy", “how do I change my information”, “ how can I move my information”, "data subject access request", “delete information”, etc. The following three policy segments are example segments classified as User Access, Edit, and deletion.

    Example Policy Segment 1: “You can request a copy of your personal information or download your data directly from your account settings.”
    Classification: User Access, Edit, and Deletion

    Example Policy Segment 2: “If you need to edit your information, you can do so by logging into your profile. For any modifications that are not available online, you may submit a request to our support team.”
    Classification: User Access, Edit, and Deletion

    Example Policy Segment 3: “You can delete your personal information that we have collected from or about you.”
    Classification: User Access, Edit, and Deletion

    Category 5. Data Retention: This category is about how long user information is stored. Retention period outlines the time period for which personal information is stored and when it will be deleted or anonymized. Here are examples of some keywords, terms, and phrases that commonly identify "data retention" in privacy policies: "retention period", "how long we keep your data", “retaining your information”, "storage duration", "duration", "keep your data", “hold your information”, “hold your information any longer than we have to”, etc. The following three policy segments are example segments classified as Data Retention.

    Example Policy Segment 1: “We retain personal information for as long as necessary to provide our service; to administer and operate our business; to research, analyze, and improve our services; to operate our ad supported subscription plan; for safety, security, and fraud prevention; and/or to enforce our Terms of Use.”
    Classification: Data Retention

    Example Policy Segment 2: “Storage of personal information is based on many factors such as the nature of the personal information, and the need to defend or resolve current or anticipated legal claims.”
    Classification: Data Retention

    Example Policy Segment 3: “We keep your personal information, including sensitive personal information, as long as we need it to provide our products, comply with legal obligations or protect our or other’s interests. We decide how long we need information on a case-by-case basis.”
    Classification: Data Retention

    Category 6. Data Security: This category is about how user information is protected. In particular, it means the security measures that ensure security of personal data, including encryption or storage of data on secure servers. It also includes processing user data to improve safety and reliability of products, services, and users. Here are examples of some keywords, terms, and phrases that commonly identify "data security" in privacy policies: “security, fraud and abuse prevention”, “information security”, “security tips”, “security measures”, “security features”, “security partners”, “security controls”, “encryption”, “data breach procedure”, “secure server”, “firewalls and antivirus software”, “appropriate technical and organizational measures to safeguard personal information”, etc. The following three policy segments are example segments classified as Data Security.

    Example Policy Segment 1: “We will share your personal information if the disclosure of information is reasonably necessary to Detect, prevent, or otherwise address fraud, security, or technical issues.”
    Classification: Data Security

    Example Policy Segment 2: “For safety, security, and fraud prevention we process personal information such as personal details, payment details, profile information, usage information, advertising information.”
    Classification: Data Security

    Example Policy Segment 3: “We follow appropriate technical and organizational measures to safeguard personal information, including regular security reviews and updates to our data breach procedures.”
    Classification: Data Security

    Category 7. Policy Change: This category is about if and how users will be informed about changes to the privacy policy. Here are examples of some keywords, terms, and phrases that commonly identify "policy change" in privacy policies: “notify you about upcoming changes”, “we change this privacy policy from time to time”, “email notification of privacy policy changes”, “notification of changes”, “revisions to this policy”, “policy update alert”, “how we will inform you”, etc. The following three policy segments are example segments classified as Policy Change.

    Example Policy Segment 1: “We use your information, like your email address, to notify you about upcoming changes to your subscription.”
    Classification: Policy Change

    Example Policy Segment 2: “This privacy policy is subject to change from time to time. We will post revisions on our site and provide a policy update alert in our user interface.”
    Classification: Policy Change

    Example Policy Segment 3: “In the event of significant changes in privacy policy, we will provide a more prominent notice via email notification.”
    Classification: Policy Change

    Category 8. Do Not Track: This category is about if and how Do Not Track signals for online tracking and advertising are honored. Examples of keywords, terms, and phrases that commonly reflect "Do Not Track" in privacy policies include: “you can switch off some cookies and similar tracking technologies”, “online tracking preferences”, “do not track”, “behavioral tracking opt-out”, “opting-out of tracking”, etc. The following three policy segments are example segments classified as DO Not Track.

    Example Policy Segment 1: “Our website respects 'Do Not Track' signals and does not track users who have set their browsers to decline tracking cookies.”
    Classification: Do Not Track

    Example Policy Segment 2: “We do not currently respond to web browser “do not track" signals.”
    Classification: Do Not Track

    Example Policy Segment 3: “You have right to opt-out of Targeted Advertising or location tracking.”
    Classification: Do Not Track

    Category 9. International and Specific Audiences: This category is about practices that pertain only to a specific group of users (e.g., children, Europeans, or California residents). It outlines specific provisions that apply exclusively to certain categories of users, such as children, residents of Europe, or individuals living in California. The privacy policy includes clauses for these distinct user groups. Here are examples of some keywords, terms, and phrases that commonly identify international audiences or specific audiences in privacy policies: “child permissions”, “special protection of children's personal data”, “age-specific guidelines”, “kids profile”, “parental consent”, “children and teens”, “international users”, “regional laws”, “GDPR” (General Data Protection Regulation for European users), “CCPA” (California Consumer Privacy Act for California residents), “COPPA” (Children's Online Privacy Protection Act), “ CIPA” (Children’s Internet Protection Act in United States), “specific audience considerations”, “disclosure and international transfers”, “supplemental privacy disclosures for certain services and regions”, etc. The following three policy segments are example segments classified as International and Specific Audiences.

    Example Policy Segment 1: “Our services comply with the Data Protection Directive (also know as Directive 95/46/EC) to protect the privacy of our European users.”
    Classification: International and Specific Audiences

    Example Policy Segment 2: “Parental consent is required before creating a kids profile on our platform, adhering to the Children's Online Privacy Protection Act (COPPA).”
    Classification: International and Specific Audiences

    Example Policy Segment 3: “We may collect sensitive or personal information, as defined in U.S. Privacy Laws.”
    Classification: International and Specific Audiences

    I have a specific task for you: I will give you a sentence from a privacy policy, and you will classify the sentence with one of these nine data practice categories. Please respond only with one of the nine categories for each sentence.
"""

PROMPT_VIa = """
1.	First Party Collection/Use.

Policy segment: “We collect the following categories of personal information about you: name, email address, profile information, payment details and device IDs.”
Classification: First Party Collection/Use

Policy segment: “In order to provide personalized services, we process information including your usage data and preferences.”
Classification: First Party Collection/Use

Policy segment: “We may also collect sensitive personal information such as information about your racial or ethnic origin, health, precise geolocation, social security number. ”
Classification: First Party Collection/Use

2.	Third Party Sharing/Collection.

Policy segment: “Our website uses third-party analytics services to help understand your usage of our services.”
Classification: Third Party Sharing/Collection.

Policy segment: “We collect personal Information from third parties whose services you use to access, pay for, or interact with our service.”
Classification: Third Party Sharing/Collection.

Policy segment: “We may collect personal information about you from other sources or service providers vendors, agents, and contractors that collect or provide personal information to us in connection with services they perform on our behalf.”
Classification: Third Party Sharing/Collection.

Policy segment: “Cookies from third-party advertisers are used on our platform to deliver targeted advertisements based on your browsing history.”
Classification: Third Party Sharing/Collection.

Policy segment: “Data we share with external partners includes your user profile and preferences to enhance your experience across partnered services.”
Classification: Third Party Sharing/Collection.

3.	User Choice/Control.

Policy segment: “You can control what information we use to show you advertisements by visiting your advertisement settings.”
Classification: User choice/control

Policy segment: “If you wish to withdraw your consent at any time for any data processing we perform, you can do so through our user settings page under ´privacy control´.”
Classification: User choice/control

Policy segment: “You may choose to opt out of receiving behavioral advertisements, you will still see Advertisements, but they will not be behavioral advertisements.”
Classification: User choice/control

4.	 User Access, Edit, and Deletion.

Policy segment: “You can request a copy of your personal information or download your data directly from your account settings.”
Classification: User access, edit, and deletion

Policy segment: “If you need to edit your information, you can do so by logging into your profile. For any modifications that are not available online, you may submit a request to our support team.”
Classification: User access, edit, and deletion

Policy segment: “You can delete your personal information that we have collected from or about you.”
Classification: User access, edit, and deletion

5.	Data Retention.
Policy segment: “We retain personal information for as long as necessary to provide our service; to administer and operate our business; to research, analyze, and improve our services; to operate our ad supported subscription plan; for safety, security, and fraud prevention; and/or to enforce our Terms of Use.”
Classification: data retention

Policy segment: “Storage of personal information is based on many factors such as the nature of the personal information, and the need to defend or resolve current or anticipated legal claims.”
Classification: data retention

Policy segment: “We keep your personal information, including sensitive personal information, as long as we need it to provide our products, comply with legal obligations or protect our or other’s interests. We decide how long we need information on a case-by-case basis.”
Classification: data retention

6.	Data Security. 

Policy segment: “We will share your personal information if the disclosure of information is reasonably necessary to Detect, prevent, or otherwise address fraud, security, or technical issues.”
Classification: Data security

Policy segment: “For safety, security, and fraud prevention we process personal information such as personal details, payment details, profile information, usage information, advertising information.”
Classification: Data security

Policy segment: “We follow appropriate technical and organizational measures to safeguard personal information, including regular security reviews and updates to our data breach procedures.”
Classification: Data security

7.	 Policy Change.

Policy segment: “We use your information, like your email address, to notify you about upcoming changes to your subscription.”
Classification: Policy Change

Policy segment: “This privacy policy is subject to change from time to time. We will post revisions on our site and provide a policy update alert in our user interface.”
Classification: Policy Change

Policy segment: “In the event of significant changes in privacy policy, we will provide a more prominent notice via email notification.”
Classification: Policy Change

8.	 Do Not Track.
Policy segment: “Our website respects 'Do Not Track' signals and does not track users who have set their browsers to decline tracking cookies.”
Classification: Do Not Track

Policy segment: “We do not currently respond to web browser “do not track" signals.”
Classification: Do Not Track

Policy segment: “You have right to opt-out of Targeted Advertising or location tracking.”
Classification: Do Not Track

9.	International and Specific Audiences.
Policy segment: “Our services comply with the Data Protection Directive (also know as Directive 95/46/EC) to protect the privacy of our European users.”
Classification: International and Specific Audiences

Policy segment: “Parental consent is required before creating a kids profile on our platform, adhering to the Children's Online Privacy Protection Act (COPPA).”
Classification: International and Specific Audiences

Policy segment: “We may collect sensitive or personal information, as defined in U.S. Privacy Laws.”
Classification: International and Specific Audiences



I have a specific task for you: The user will give you a sentence from some privacy contents, and you tell them which category of practices this sentence may contain. Please only respond with the category.
"""

PROMPT_VIIa = """
1.	First Party Collection/Use: how and why a service provider collects user information. In first party collection the service provider that owns or operates the website/platform/service directly collect data from individuals. For instance, when a customer engages with the services of company A, company A collects data such as the products they have browsed, their purchasing choices, or their behavior patterns. When company A makes a product recommendation to customer based on this data, it can be referred to as first-party advertising. In this case, collection and use of personal data is identified as first party data collection and use. In privacy policies, certain keywords and phrases can help to identify if the data collection or use is first-party. For example: "We collect", "Data you provide", "Information we collect", "Our servers", "Our cookies", "We use your data" "Data collected from your interaction with our services", "Information you submit", “We restrict access to personal information to our employees, contractors, and agents”, etc.

Policy segment: “We collect the following categories of personal information about you: name, email address, profile information, payment details and device IDs.”
Classification: First Party Collection/Use

Policy segment: “In order to provide personalized services, we process information including your usage data and preferences.”
Classification: First Party Collection/Use

Policy segment: “We may also collect sensitive personal information such as information about your racial or ethnic origin, health, precise geolocation, social security number. ”
Classification: First Party Collection/Use

2.	Third Party Sharing/Collection: how user information may be shared with or collected by third parties. In third party sharing/collection an entity other than the service provider collects data from users through the service provider's platform. Third parties could include advertisers, ad network companies, analytic companies, or partner services that have their own data collection and privacy practices. Third-party entities often work with a variety of first-party websites, collecting information on user profiles from diverse sources, including news, weather, entertainment, and travel websites. For instance, if a customer uses Amazon.com's services and Amazon utilizes details about the user that have been collected by companies other than itself, this is known as third-party data collection and use. In privacy policies, certain keywords and phrases can help to identify if the data collection or use is third-party. For example: "Third-party providers", "External partners", "Ad networks", "Data we share" "Cookies from third-party advertisers", "Third-party cookies", "Third-party analytics", "Our partners’ services", “data processors”, etc.

Policy segment: “Our website uses third-party analytics services to help understand your usage of our services.”
Classification: Third Party Sharing/Collection.

Policy segment: “We collect personal Information from third parties whose services you use to access, pay for, or interact with our service.”
Classification: Third Party Sharing/Collection.

Policy segment: “We may collect personal information about you from other sources or service providers vendors, agents, and contractors that collect or provide personal information to us in connection with services they perform on our behalf.”
Classification: Third Party Sharing/Collection.

Policy segment: “Cookies from third-party advertisers are used on our platform to deliver targeted advertisements based on your browsing history.”
Classification: Third Party Sharing/Collection.

Policy segment: “Data we share with external partners includes your user profile and preferences to enhance your experience across partnered services.”
Classification: Third Party Sharing/Collection.

3.	User Choice/Control: choices and control options available to users. Choice means giving individuals options as to how their personal information may be used. Specifically, choice relates to secondary uses of information—that is, uses beyond those necessary to complete the contemplated transaction. Control means privacy controls that allow individuals to manage use and sharing of their data. Example for choice/control can be following: “opt-in”, “opt-out”, “cookie preference” (functional/recommended/essential/performance/advertising), “location data controls”, “privacy control”, “communication preference”, “do-not-track”, “do-not-sell”, “withdraw consent”, etc.

Policy segment: “You can control what information we use to show you advertisements by visiting your advertisement settings.”
Classification: User choice/control

Policy segment: “If you wish to withdraw your consent at any time for any data processing we perform, you can do so through our user settings page under ´privacy control´.”
Classification: User choice/control

Policy segment: “You may choose to opt out of receiving behavioral advertisements, you will still see Advertisements, but they will not be behavioral advertisements.”
Classification: User choice/control

4.	 User Access, Edit, and Deletion: if and how users may access, edit, or delete their information. These are privacy rights-based choices. In privacy policies such provision can be found in the following keywords and phrases: "right to access", “rights you have”, "request a copy", "view your information", "download your data", "personal data report", "obtain a copy", “how do I change my information”, “ how can I move my information”, "data subject access request", “delete information”, etc.

Policy segment: “You can request a copy of your personal information or download your data directly from your account settings.”
Classification: User access, edit, and deletion

Policy segment: “If you need to edit your information, you can do so by logging into your profile. For any modifications that are not available online, you may submit a request to our support team.”
Classification: User access, edit, and deletion

Policy segment: “You can delete your personal information that we have collected from or about you.”
Classification: User access, edit, and deletion

5.	Data Retention: how long user information is stored. Retention period outlines the time period for which personal information is stored and when it will be deleted or anonymized. Here are examples of some keywords, terms, and phrases that commonly identify "data retention" in privacy policies: "retention period", "how long we keep your data", “retaining your information”, "storage duration", "duration", "keep your data", “hold your information”, “hold your information any longer than we have to”, etc.
Policy segment: “We retain personal information for as long as necessary to provide our service; to administer and operate our business; to research, analyze, and improve our services; to operate our ad supported subscription plan; for safety, security, and fraud prevention; and/or to enforce our Terms of Use.”
Classification: data retention

Policy segment: “Storage of personal information is based on many factors such as the nature of the personal information, and the need to defend or resolve current or anticipated legal claims.”
Classification: data retention

Policy segment: “We keep your personal information, including sensitive personal information, as long as we need it to provide our products, comply with legal obligations or protect our or other’s interests. We decide how long we need information on a case-by-case basis.”
Classification: data retention

6.	Data Security: how user information is protected. In particular, it means the security measures that ensures security of personal data, including encryption or storage of data on secure servers. It also includes processing user data to improve safety and reliability of products, services, and users. Here are examples of some keywords, terms, and phrases that commonly identify "data security" in privacy policies: “security, fraud and abuse prevention”, “information security”, “security tips”, “security measures”, “security features”, “security partners”, “security controls”, “encryption”, “data breach procedure”, “secure server”, “firewalls and antivirus software”, “appropriate technical and organizational measures to safeguard personal information”, etc. 

Policy segment: “We will share your personal information if the disclosure of information is reasonably necessary to Detect, prevent, or otherwise address fraud, security, or technical issues.”
Classification: Data security

Policy segment: “For safety, security, and fraud prevention we process personal information such as personal details, payment details, profile information, usage information, advertising information.”
Classification: Data security

Policy segment: “We follow appropriate technical and organizational measures to safeguard personal information, including regular security reviews and updates to our data breach procedures.”
Classification: Data security

7.	 Policy Change: if and how users will be informed about changes to the privacy policy. Here are examples of some keywords, terms, and phrases that commonly identify "policy change" in privacy policies: “notify you about upcoming changes”, “we change this privacy policy from time to time”, “email notification of privacy policy changes”, “notification of changes”, “revisions to this policy”, “policy update alert”, “how we will inform you”, etc.

Policy segment: “We use your information, like your email address, to notify you about upcoming changes to your subscription.”
Classification: Policy Change

Policy segment: “This privacy policy is subject to change from time to time. We will post revisions on our site and provide a policy update alert in our user interface.”
Classification: Policy Change

Policy segment: “In the event of significant changes in privacy policy, we will provide a more prominent notice via email notification.”
Classification: Policy Change

8.	 Do Not Track: if and how Do Not Track signals for online tracking and advertising are honored. Examples of keywords, terms, and phrases that commonly reflect "Do Not Track" in privacy policies include: “you can switch off some cookies and similar tracking technologies”, “online tracking preferences”, “do not track”, “behavioral tracking opt-out”, “opting-out of tracking”, etc.
Policy segment: “Our website respects 'Do Not Track' signals and does not track users who have set their browsers to decline tracking cookies.”
Classification: Do Not Track

Policy segment: “We do not currently respond to web browser “do not track" signals.”
Classification: Do Not Track

Policy segment: “You have right to opt-out of Targeted Advertising or location tracking.”
Classification: Do Not Track

9.	International and Specific Audiences: practices that pertain only to a specific group of users (e.g., children, Europeans, or California residents). This category outlines specific provisions that apply exclusively to certain categories of users, such as children, or residents of Europe, or individuals living in California. The privacy policy includes clauses for these distinct user groups. Here are examples of some keywords, terms, and phrases that commonly identify international audiences or specific audiences in privacy policies: “child permissions”, “special protection of children's personal data”, “age-specific guidelines”, “kids profile”, “parental consent”, “children and teens”, “international users”, “regional laws”, “GDPR” (General Data Protection Regulation for European users), “CCPA” (California Consumer Privacy Act for California residents), “COPPA” (Children's Online Privacy Protection Act), “ CIPA” (Children’s Internet Protection Act in United States), “specific audience considerations”, “disclosure and international transfers”, “supplemental privacy disclosures for certain services and regions”, etc.
Policy segment: “Our services comply with the Data Protection Directive (also know as Directive 95/46/EC) to protect the privacy of our European users.”
Classification: International and Specific Audiences

Policy segment: “Parental consent is required before creating a kids profile on our platform, adhering to the Children's Online Privacy Protection Act (COPPA).”
Classification: International and Specific Audiences

Policy segment: “We may collect sensitive or personal information, as defined in U.S. Privacy Laws.”
Classification: International and Specific Audiences



I have a specific task for you: The user will give you a sentence from some privacy contents, and you tell them which category of practices this sentence may contain. Please only respond with the category.
"""

PROMPT_VIIIa = """
1.	First Party Collection/Use: how and why a service provider collects user information. In first party collection the service provider that owns or operates the website/platform/service directly collect data from individuals. For instance, when a customer engages with the services of company A, company A collects data such as the products they have browsed, their purchasing choices, or their behavior patterns. When company A makes a product recommendation to customer based on this data, it can be referred to as first-party advertising. In this case, collection and use of personal data is identified as first party data collection and use. In privacy policies, certain keywords and phrases can help to identify if the data collection or use is first-party. For example: "We collect", "Data you provide", "Information we collect", "Our servers", "Our cookies", "We use your data" "Data collected from your interaction with our services", "Information you submit", “We restrict access to personal information to our employees, contractors, and agents”, etc.

Policy segment: “We collect the following categories of personal information about you: name, email address, profile information, payment details and device IDs.”
Classification: First Party Collection/Use

Policy segment: “In order to provide personalized services, we process information including your usage data and preferences.”
Classification: First Party Collection/Use

Policy segment: “We may also collect sensitive personal information such as information about your racial or ethnic origin, health, precise geolocation, social security number. ”
Classification: First Party Collection/Use

2.	Third Party Sharing/Collection: how user information may be shared with or collected by third parties. In third party sharing/collection an entity other than the service provider collects data from users through the service provider's platform. Third parties could include advertisers, ad network companies, analytic companies, or partner services that have their own data collection and privacy practices. Third-party entities often work with a variety of first-party websites, collecting information on user profiles from diverse sources, including news, weather, entertainment, and travel websites. For instance, if a customer uses Amazon.com's services and Amazon utilizes details about the user that have been collected by companies other than itself, this is known as third-party data collection and use. In privacy policies, certain keywords and phrases can help to identify if the data collection or use is third-party. For example: "Third-party providers", "External partners", "Ad networks", "Data we share" "Cookies from third-party advertisers", "Third-party cookies", "Third-party analytics", "Our partners’ services", “data processors”, etc.

Policy segment: “Our website uses third-party analytics services to help understand your usage of our services.”
Classification: Third Party Sharing/Collection.

Policy segment: “We collect personal Information from third parties whose services you use to access, pay for, or interact with our service.”
Classification: Third Party Sharing/Collection.

Policy segment: “We may collect personal information about you from other sources or service providers vendors, agents, and contractors that collect or provide personal information to us in connection with services they perform on our behalf.”
Classification: Third Party Sharing/Collection.

Policy segment: “Cookies from third-party advertisers are used on our platform to deliver targeted advertisements based on your browsing history.”
Classification: Third Party Sharing/Collection.

Policy segment: “Data we share with external partners includes your user profile and preferences to enhance your experience across partnered services.”
Classification: Third Party Sharing/Collection.

3.	User Choice/Control: choices and control options available to users. Choice means giving individuals options as to how their personal information may be used. Specifically, choice relates to secondary uses of information—that is, uses beyond those necessary to complete the contemplated transaction. Control means privacy controls that allow individuals to manage use and sharing of their data. Example for choice/control can be following: “opt-in”, “opt-out”, “cookie preference” (functional/recommended/essential/performance/advertising), “location data controls”, “privacy control”, “communication preference”, “do-not-track”, “do-not-sell”, “withdraw consent”, etc.

Policy segment: “You can control what information we use to show you advertisements by visiting your advertisement settings.”
Classification: User choice/control

Policy segment: “If you wish to withdraw your consent at any time for any data processing we perform, you can do so through our user settings page under ´privacy control´.”
Classification: User choice/control

Policy segment: “You may choose to opt out of receiving behavioral advertisements, you will still see Advertisements, but they will not be behavioral advertisements.”
Classification: User choice/control

4.	 User Access, Edit, and Deletion: if and how users may access, edit, or delete their information. These are privacy rights-based choices. In privacy policies such provision can be found in the following keywords and phrases: "right to access", “rights you have”, "request a copy", "view your information", "download your data", "personal data report", "obtain a copy", “how do I change my information”, “ how can I move my information”, "data subject access request", “delete information”, etc.

Policy segment: “You can request a copy of your personal information or download your data directly from your account settings.”
Classification: User access, edit, and deletion

Policy segment: “If you need to edit your information, you can do so by logging into your profile. For any modifications that are not available online, you may submit a request to our support team.”
Classification: User access, edit, and deletion

Policy segment: “You can delete your personal information that we have collected from or about you.”
Classification: User access, edit, and deletion

5.	Data Retention: that user information is stored. Data retention relates to storing personal data over time. Here are examples of some keywords, terms, and phrases that commonly identify "data retention" in privacy policies: "retention period", "how long we keep your data", “retaining your information”, "storage duration", "duration", "keep your data", “hold your information”, “hold your information any longer than we have to”, etc.
Policy segment: “We retain personal information for as long as necessary to provide our service; to administer and operate our business; to research, analyze, and improve our services; to operate our ad supported subscription plan; for safety, security, and fraud prevention; and/or to enforce our Terms of Use.”
Classification: data retention

Policy segment: “Storage of personal information is based on many factors such as the nature of the personal information, and the need to defend or resolve current or anticipated legal claims.”
Classification: data retention

Policy segment: “We keep your personal information, including sensitive personal information, to improve our products, comply with legal obligations or protect our or other’s interests.”
Classification: data retention

6.	Data Security: how user information is protected. In particular, it means the security measures that ensures security of personal data, including encryption or storage of data on secure servers. It also includes processing user data to improve safety and reliability of products, services, and users. Here are examples of some keywords, terms, and phrases that commonly identify "data security" in privacy policies: “security, fraud and abuse prevention”, “information security”, “security tips”, “security measures”, “security features”, “security partners”, “security controls”, “encryption”, “data breach procedure”, “secure server”, “firewalls and antivirus software”, “appropriate technical and organizational measures to safeguard personal information”, etc. 

Policy segment: “For safety, security, and fraud prevention we process personal information such as personal details, payment details, profile information, usage information, advertising information.”
Classification: Data security

Policy segment: “We follow appropriate technical and organizational measures to safeguard personal information, including regular security reviews and updates to our data breach procedures.”
Classification: Data security

7.	 Policy Change: if and how users will be informed about changes to the privacy policy. Here are examples of some keywords, terms, and phrases that commonly identify "policy change" in privacy policies: “notify you about upcoming changes”, “we change this privacy policy from time to time”, “email notification of privacy policy changes”, “notification of changes”, “revisions to this policy”, “policy update alert”, “how we will inform you”, etc.

Policy segment: “We use your information, like your email address, to notify you about upcoming changes to your subscription.”
Classification: Policy Change

Policy segment: “This privacy policy is subject to change from time to time. We will post revisions on our site and provide a policy update alert in our user interface.”
Classification: Policy Change

Policy segment: “In the event of significant changes in privacy policy, we will provide a more prominent notice via email notification.”
Classification: Policy Change

8.	 Do Not Track: if and how Do Not Track signals for online tracking and advertising are honored. Examples of keywords, terms, and phrases that commonly reflect "Do Not Track" in privacy policies include: “you can switch off some cookies and similar tracking technologies”, “online tracking preferences”, “do not track”, “behavioral tracking opt-out”, “opting-out of tracking”, etc.
Policy segment: “Our website respects 'Do Not Track' signals and does not track users who have set their browsers to decline tracking cookies.”
Classification: Do Not Track

Policy segment: “We do not currently respond to web browser “do not track" signals.”
Classification: Do Not Track

Policy segment: “You have right to opt-out of Targeted Advertising or location tracking.”
Classification: Do Not Track

9.	International and Specific Audiences: practices that pertain only to a specific group of users (e.g., children, Europeans, or California residents). This category outlines specific provisions that apply exclusively to certain categories of users, such as children, or residents of Europe, or individuals living in California. The privacy policy includes clauses for these distinct user groups. Here are examples of some keywords, terms, and phrases that commonly identify international audiences or specific audiences in privacy policies: “child permissions”, “special protection of children's personal data”, “age-specific guidelines”, “kids profile”, “parental consent”, “children and teens”, “international users”, “regional laws”, “GDPR” (General Data Protection Regulation for European users), “CCPA” (California Consumer Privacy Act for California residents), “COPPA” (Children's Online Privacy Protection Act), “ CIPA” (Children’s Internet Protection Act in United States), “specific audience considerations”, “disclosure and international transfers”, “supplemental privacy disclosures for certain services and regions”, etc.
Policy segment: “Our services comply with the Data Protection Directive (also know as Directive 95/46/EC) to protect the privacy of our European users.”
Classification: International and Specific Audiences

Policy segment: “Parental consent is required before creating a kids profile on our platform, adhering to the Children's Online Privacy Protection Act (COPPA).”
Classification: International and Specific Audiences

Policy segment: “We may collect sensitive or personal information, as defined in U.S. Privacy Laws.”
Classification: International and Specific Audiences



I have a specific task for you: The user will give you a sentence from some privacy contents, and you tell them which category of practices this sentence may contain. Please only respond with the category.
"""

PROMPT_IXa = """
1.	First Party Collection/Use: how and why a service provider collects user information. In first party collection the service provider that owns or operates the website/platform/service directly collect data from individuals. For instance, when a customer engages with the services of company A, company A collects data such as the products they have browsed, their purchasing choices, or their behavior patterns. When company A makes a product recommendation to customer based on this data, it can be referred to as first-party advertising. In this case, collection and use of personal data is identified as first party data collection and use. In privacy policies, certain keywords and phrases can help to identify if the data collection or use is first-party. For example: "We collect", "Data you provide", "Information we collect", "Our servers", "Our cookies", "We use your data" "Data collected from your interaction with our services", "Information you submit", “We restrict access to personal information to our employees, contractors, and agents”, etc.

Policy segment: “We collect the following categories of personal information about you: name, email address, profile information, payment details and device IDs.”
Classification: First Party Collection/Use

Policy segment: “In order to provide personalized services, we process information including your usage data and preferences.”
Classification: First Party Collection/Use

Policy segment: “We may also collect sensitive personal information such as information about your racial or ethnic origin, health, precise geolocation, social security number. ”
Classification: First Party Collection/Use

2.	Third Party Sharing/Collection: how user information may be shared with or collected by third parties. In third party sharing/collection an entity other than the service provider collects data from users through the service provider's platform. Third parties could include advertisers, ad network companies, analytic companies, or partner services that have their own data collection and privacy practices. Third-party entities often work with a variety of first-party websites, collecting information on user profiles from diverse sources, including news, weather, entertainment, and travel websites. For instance, if a customer uses Amazon.com's services and Amazon utilizes details about the user that have been collected by companies other than itself, this is known as third-party data collection and use. In privacy policies, certain keywords and phrases can help to identify if the data collection or use is third-party. For example: "Third-party providers", "External partners", "Ad networks", "Data we share" "Cookies from third-party advertisers", "Third-party cookies", "Third-party analytics", "Our partners’ services", “data processors”, etc.

Policy segment: “We may collect personal information about you from other sources or service providers vendors, agents, and contractors that collect or provide personal information to us in connection with services they perform on our behalf.”
Classification: Third Party Sharing/Collection.

Policy segment: “Cookies from third-party advertisers are used on our platform to deliver targeted advertisements based on your browsing history.”
Classification: Third Party Sharing/Collection.

Policy segment: “Data we share with external partners includes your user profile and preferences to enhance your experience across partnered services.”
Classification: Third Party Sharing/Collection.

3.	User Choice/Control: choices and control options available to users. Choice means giving individuals options as to how their personal information may be used. Specifically, choice relates to secondary uses of information—that is, uses beyond those necessary to complete the contemplated transaction. Control means privacy controls that allow individuals to manage use and sharing of their data. Example for choice/control can be following: “opt-in”, “opt-out”, “cookie preference” (functional/recommended/essential/performance/advertising), “location data controls”, “privacy control”, “communication preference”, “do-not-track”, “do-not-sell”, “withdraw consent”, etc.

Policy segment: “You can control what information we use to show you advertisements by visiting your advertisement settings.”
Classification: User choice/control

Policy segment: “If you wish to withdraw your consent at any time for any data processing we perform, you can do so through our user settings page under ´privacy control´.”
Classification: User choice/control

Policy segment: “You may choose to opt out of receiving behavioral advertisements, you will still see Advertisements, but they will not be behavioral advertisements.”
Classification: User choice/control

4.	 User Access, Edit, and Deletion: if and how users may access, edit, or delete their information. These are privacy rights-based choices. In privacy policies such provision can be found in the following keywords and phrases: "right to access", “rights you have”, "request a copy", "view your information", "download your data", "personal data report", "obtain a copy", “how do I change my information”, “ how can I move my information”, "data subject access request", “delete information”, etc.

Policy segment: “You can request a copy of your personal information or download your data directly from your account settings.”
Classification: User access, edit, and deletion

Policy segment: “If you need to edit your information, you can do so by logging into your profile. For any modifications that are not available online, you may submit a request to our support team.”
Classification: User access, edit, and deletion

Policy segment: “You can delete your personal information that we have collected from or about you.”
Classification: User access, edit, and deletion

5.	Data Retention: how long user information is stored. Retention period outlines the time period for which personal information is stored and when it will be deleted or anonymized. Here are examples of some keywords, terms, and phrases that commonly identify "data retention" in privacy policies: "retention period", "how long we keep your data", “retaining your information”, "storage duration", "duration", "keep your data", “hold your information”, “hold your information any longer than we have to”, etc.
Policy segment: “We retain personal information for as long as necessary to provide our service; to administer and operate our business; to research, analyze, and improve our services; to operate our ad supported subscription plan; for safety, security, and fraud prevention; and/or to enforce our Terms of Use.”
Classification: data retention

Policy segment: “Storage of personal information is based on many factors such as the nature of the personal information, and the need to defend or resolve current or anticipated legal claims.”
Classification: data retention

Policy segment: “We keep your personal information, including sensitive personal information, to improve our products, comply with legal obligations or protect our or other’s interests.”
Classification: data retention

6.	Data Security: how user information is protected. In particular, it means the security measures that ensures security of personal data, including encryption or storage of data on secure servers. It also includes processing user data to improve safety and reliability of products, services, and users. Here are examples of some keywords, terms, and phrases that commonly identify "data security" in privacy policies: “security, fraud and abuse prevention”, “information security”, “security tips”, “security measures”, “security features”, “security partners”, “security controls”, “encryption”, “data breach procedure”, “secure server”, “firewalls and antivirus software”, “appropriate technical and organizational measures to safeguard personal information”, etc. 

Policy segment: “Protecting the privacy and security of your information is our priority.”
Classification: Data security

Policy segment: “For safety, security, and fraud prevention we process personal information such as personal details, payment details, profile information, usage information, advertising information.”
Classification: Data security

Policy segment: “We follow appropriate technical and organizational measures to safeguard personal information, including regular security reviews and updates to our data breach procedures.”
Classification: Data security

7.	 Policy Change: if and how users will be informed about changes to the privacy policy. Here are examples of some keywords, terms, and phrases that commonly identify "policy change" in privacy policies: “notify you about upcoming changes”, “we change this privacy policy from time to time”, “email notification of privacy policy changes”, “notification of changes”, “revisions to this policy”, “policy update alert”, “how we will inform you”, etc.

Policy segment: “We use your information, like your email address, to notify you about upcoming changes to your subscription.”
Classification: Policy Change

Policy segment: “This privacy policy is subject to change from time to time. We will post revisions on our site and provide a policy update alert in our user interface.”
Classification: Policy Change

Policy segment: “In the event of significant changes in privacy policy, we will provide a more prominent notice via email notification.”
Classification: Policy Change

8.	 Do Not Track: if and how Do Not Track signals for online tracking and advertising are honored. Examples of keywords, terms, and phrases that commonly reflect "Do Not Track" in privacy policies include: “you can switch off some cookies and similar tracking technologies”, “online tracking preferences”, “do not track”, “behavioral tracking opt-out”, “opting-out of tracking”, etc.
Policy segment: “Our website respects 'Do Not Track' signals and does not track users who have set their browsers to decline tracking cookies.”
Classification: Do Not Track

Policy segment: “We do not currently respond to web browser “do not track" signals.”
Classification: Do Not Track

Policy segment: “You have right to opt-out of Targeted Advertising or location tracking.”
Classification: Do Not Track

9.	International and Specific Audiences: practices that pertain only to a specific group of users (e.g., children, Europeans, or California residents). This category outlines specific provisions that apply exclusively to certain categories of users, such as children, or residents of Europe, or individuals living in California. The privacy policy includes clauses for these distinct user groups. Here are examples of some keywords, terms, and phrases that commonly identify international audiences or specific audiences in privacy policies: “child permissions”, “special protection of children's personal data”, “age-specific guidelines”, “kids profile”, “parental consent”, “children and teens”, “international users”, “regional laws”, “GDPR” (General Data Protection Regulation for European users), “CCPA” (California Consumer Privacy Act for California residents), “COPPA” (Children's Online Privacy Protection Act), “ CIPA” (Children’s Internet Protection Act in United States), “specific audience considerations”, “disclosure and international transfers”, “supplemental privacy disclosures for certain services and regions”, etc.
Policy segment: “Our services comply with the Data Protection Directive (also know as Directive 95/46/EC) to protect the privacy of our European users.”
Classification: International and Specific Audiences

Policy segment: “Parental consent is required before creating a kids profile on our platform, adhering to the Children's Online Privacy Protection Act (COPPA).”
Classification: International and Specific Audiences

Policy segment: “We may collect sensitive or personal information, as defined in U.S. Privacy Laws.”
Classification: International and Specific Audiences



I have a specific task for you: The user will give you a sentence from some privacy contents, and you tell them which category of practices this sentence may contain. Please only respond with the category.
"""



PROMPT_Xa = """
Websites and digital products have privacy policies. A data practice means how the data is used and processed by an organization. A sentence (policy segment) in a privacy policy can be annotated with one of the following nine data practice categories:

1.	First Party Collection/Use: how and why a service provider collects user information. In first party collection the service provider that owns or operates the website/platform/service directly collect data from individuals. For instance, when a customer engages with the services of company A, company A collects data such as the products they have browsed, their purchasing choices, or their behavior patterns. When company A makes a product recommendation to customer based on this data, it can be referred to as first-party advertising. In this case, collection and use of personal data is identified as first party data collection and use. In privacy policies, certain keywords and phrases can help to identify if the data collection or use is first-party. For example: "We collect", "Data you provide", "Information we collect", "Our servers", "Our cookies", "We use your data" "Data collected from your interaction with our services", "Information you submit", “We restrict access to personal information to our employees, contractors, and agents”, etc.

Policy segment: “We collect the following categories of personal information about you: name, email address, profile information, payment details and device IDs.”
Classification: First Party Collection/Use

2.	Third Party Sharing/Collection: how user information may be shared with or collected by third parties. In third party sharing/collection an entity other than the service provider collects data from users through the service provider's platform. Third parties could include advertisers, ad network companies, analytic companies, or partner services that have their own data collection and privacy practices. Third-party entities often work with a variety of first-party websites, collecting information on user profiles from diverse sources, including news, weather, entertainment, and travel websites. For instance, if a customer uses Amazon.com's services and Amazon utilizes details about the user that have been collected by companies other than itself, this is known as third-party data collection and use. In privacy policies, certain keywords and phrases can help to identify if the data collection or use is third-party. For example: "Third-party providers", "External partners", "Ad networks", "Data we share" "Cookies from third-party advertisers", "Third-party cookies", "Third-party analytics", "Our partners’ services", “data processors”, etc.

Policy segment: “Data we share with external partners includes your user profile and preferences to enhance your experience across partnered services.”
Classification: Third Party Sharing/Collection.

3.	User Choice/Control: choices and control options available to users. Choice means giving individuals options as to how their personal information may be used. Specifically, choice relates to secondary uses of information—that is, uses beyond those necessary to complete the contemplated transaction. Control means privacy controls that allow individuals to manage use and sharing of their data. Example for choice/control can be following: “opt-in”, “opt-out”, “cookie preference” (functional/recommended/essential/performance/advertising), “location data controls”, “privacy control”, “communication preference”, “do-not-track”, “do-not-sell”, “withdraw consent”, etc.

Policy segment: “You can control what information we use to show you advertisements by visiting your advertisement settings.”
Classification: User choice/control

4.	 User Access, Edit, and Deletion: if and how users may access, edit, or delete their information. These are privacy rights-based choices. In privacy policies such provision can be found in the following keywords and phrases: "right to access", “rights you have”, "request a copy", "view your information", "download your data", "personal data report", "obtain a copy", “how do I change my information”, “ how can I move my information”, "data subject access request", “delete information”, etc.

Policy segment: “If you need to edit your information, you can do so by logging into your profile. For any modifications that are not available online, you may submit a request to our support team.”
Classification: User access, edit, and deletion

5.	Data Retention: how long user information is stored. Retention period outlines the time period for which personal information is stored and when it will be deleted or anonymized. Here are examples of some keywords, terms, and phrases that commonly identify "data retention" in privacy policies: "retention period", "how long we keep your data", “retaining your information”, "storage duration", "duration", "keep your data", “hold your information”, “hold your information any longer than we have to”, etc.

Policy segment: “We retain personal information for as long as necessary to provide our service; to administer and operate our business; to research, analyze, and improve our services; to operate our ad supported subscription plan; for safety, security, and fraud prevention; and/or to enforce our Terms of Use.”
Classification: data retention

6.	Data Security: how user information is protected. In particular, it means the security measures that ensures security of personal data, including encryption or storage of data on secure servers. It also includes processing user data to improve safety and reliability of products, services, and users. Here are examples of some keywords, terms, and phrases that commonly identify "data security" in privacy policies: “security, fraud and abuse prevention”, “information security”, “security tips”, “security measures”, “security features”, “security partners”, “security controls”, “encryption”, “data breach procedure”, “secure server”, “firewalls and antivirus software”, “appropriate technical and organizational measures to safeguard personal information”, etc. 

Policy segment: “For safety, security, and fraud prevention we process personal information such as personal details, payment details, profile information, usage information, advertising information.”
Classification: Data security

7.	 Policy Change: if and how users will be informed about changes to the privacy policy. Here are examples of some keywords, terms, and phrases that commonly identify "policy change" in privacy policies: “notify you about upcoming changes”, “we change this privacy policy from time to time”, “email notification of privacy policy changes”, “notification of changes”, “revisions to this policy”, “policy update alert”, “how we will inform you”, etc.

Policy segment: “This privacy policy is subject to change from time to time. We will post revisions on our site and provide a policy update alert in our user interface.”
Classification: Policy Change

8.	 Do Not Track: if and how Do Not Track signals for online tracking and advertising are honored. Examples of keywords, terms, and phrases that commonly reflect "Do Not Track" in privacy policies include: “you can switch off some cookies and similar tracking technologies”, “online tracking preferences”, “do not track”, “behavioral tracking opt-out”, “opting-out of tracking”, etc.

Policy segment: “Our website respects 'Do Not Track' signals and does not track users who have set their browsers to decline tracking cookies.”
Classification: Do Not Track

9.	International and Specific Audiences: practices that pertain only to a specific group of users (e.g., children, Europeans, or California residents). This category outlines specific provisions that apply exclusively to certain categories of users, such as children, or residents of Europe, or individuals living in California. The privacy policy includes clauses for these distinct user groups. Here are examples of some keywords, terms, and phrases that commonly identify international audiences or specific audiences in privacy policies: “child permissions”, “special protection of children's personal data”, “age-specific guidelines”, “kids profile”, “parental consent”, “children and teens”, “international users”, “regional laws”, “GDPR” (General Data Protection Regulation for European users), “CCPA” (California Consumer Privacy Act for California residents), “COPPA” (Children's Online Privacy Protection Act), “ CIPA” (Children’s Internet Protection Act in United States), “specific audience considerations”, “disclosure and international transfers”, “supplemental privacy disclosures for certain services and regions”, etc.

Policy segment: “Parental consent is required before creating a kids profile on our platform, adhering to the Children's Online Privacy Protection Act (COPPA).”
Classification: International and Specific Audiences


I have a specific task for you: The user will give you a sentence from some privacy contents, and you tell them which category of practices this sentence may contain. Please only respond with the category.
"""

PROMPT_XIa = """
Websites and digital products have privacy policies. A data practice means how the data is used and processed by an organization. A sentence (policy segment) in a privacy policy can be annotated with one of the following nine data practice categories:

    Category 1. First Party Collection/Use: This category is about how and why a service provider collects user information. In first party collection, the service provider that owns or operates the website/platform/service directly collects data from individuals. For instance, when a customer engages with the services of company A, company A collects data such as the products they have browsed, their purchasing choices, or their behavior patterns. When company A makes a product recommendation to a customer based on this data, it can be referred to as first-party advertising. In this case, collection and use of personal data is identified as first party data collection and use. In privacy policies, certain keywords and phrases can help to identify if the data collection or use is first party. For example: "We collect", "Data you provide", "Information we collect", "Our servers", "Our cookies", "We use your data" "Data collected from your interaction with our services", "Information you submit", “We restrict access to personal information to our employees, contractors, and agents”, etc. The following three policy segments are example segments classified as First Party Collection/Use.

    Example Policy Segment 1: “We collect the following categories of personal information about you: name, email address, profile information, payment details and device IDs.”
    Classification: First Party Collection/Use

    Example Policy Segment 2: “In order to provide personalized services, we process information including your usage data and preferences.”
    Classification: First Party Collection/Use

    Example Policy Segment 3: “We may also collect sensitive personal information such as information about your racial or ethnic origin, health, precise geolocation, social security number.”
    Classification: First Party Collection/Use

    Category 2. Third Party Sharing/Collection: This category is about how user information may be shared with or collected by third parties. In third party sharing/collection an entity other than the service provider collects data from users through the service provider's platform. Third parties could include advertisers, ad network companies, analytic companies, or partner services that have their own data collection and privacy practices. Third-party entities often work with a variety of first-party websites, collecting information on user profiles from diverse sources, including news, weather, entertainment, and travel websites. For instance, if a customer uses Amazon.com's services and Amazon utilizes details about the user that have been collected by companies other than itself, this is known as third-party data collection and use. In privacy policies, certain keywords and phrases can help to identify if the data collection or use is third-party. For example: "Third-party providers", "External partners", "Ad networks", "Data we share" "Cookies from third-party advertisers", "Third-party cookies", "Third-party analytics", "Our partners’ services", “data processors”, etc. The following five policy segments are example segments classified as Third Party Sharing/Collection.

    Example Policy Segment 1: “Our website uses third-party analytics services to help understand your usage of our services.”
    Classification: Third Party Sharing/Collection.

    Example Policy Segment 2: “We collect personal Information from third parties whose services you use to access, pay for, or interact with our service.”
    Classification: Third Party Sharing/Collection.

    Example Policy Segment 3: “We may collect personal information about you from other sources or service providers vendors, agents, and contractors that collect or provide personal information to us in connection with services they perform on our behalf.”
    Classification: Third Party Sharing/Collection.

    Example Policy Segment 4: “Cookies from third-party advertisers are used on our platform to deliver targeted advertisements based on your browsing history.”
    Classification: Third Party Sharing/Collection.

    Example Policy Segment 5: “Data we share with external partners includes your user profile and preferences to enhance your experience across partnered services.”
    Classification: Third Party Sharing/Collection.

    Category 3. User Choice/Control: This category is about choices and control options available to users. Choice means giving individuals options as to how their personal information may be used. Specifically, choice relates to secondary uses of information—that is, uses beyond those necessary to complete the contemplated transaction. Control means privacy controls that allow individuals to manage use and sharing of their data. Example for choice/control can be following: “opt-in”, “opt-out”, “cookie preference” (functional/recommended/essential/performance/advertising), “location data controls”, “privacy control”, “communication preference”, “do-not-track”, “do-not-sell”, “withdraw consent”, etc. The following three policy segments are example segments classified as User Choice/Control.

    Example Policy Segment 1: “You can control what information we use to show you advertisements by visiting your advertisement settings.”
    Classification: User Choice/Control

    Example Policy Segment 2: “If you wish to withdraw your consent at any time for any data processing we perform, you can do so through our user settings page under privacy control.”
    Classification: User Choice/Control

    Example Policy Segment 3: “You may choose to opt out of receiving behavioral advertisements, you will still see Advertisements, but they will not be behavioral advertisements.”
    Classification: User Choice/Control

    Category 4. User Access, Edit, and Deletion: This category is about if and how users may access, edit, or delete their information. These are privacy rights-based choices. In privacy policies such provision can be found in the following keywords and phrases: "right to access", “rights you have”, "request a copy", "view your information", "download your data", "personal data report", "obtain a copy", “how do I change my information”, “ how can I move my information”, "data subject access request", “delete information”, etc. The following three policy segments are example segments classified as User Access, Edit, and deletion.

    Example Policy Segment 1: “You can request a copy of your personal information or download your data directly from your account settings.”
    Classification: User Access, Edit, and Deletion

    Example Policy Segment 2: “If you need to edit your information, you can do so by logging into your profile. For any modifications that are not available online, you may submit a request to our support team.”
    Classification: User Access, Edit, and Deletion

    Example Policy Segment 3: “You can delete your personal information that we have collected from or about you.”
    Classification: User Access, Edit, and Deletion

    Category 5. Data Retention: This category is about how long user information is stored. Retention period outlines the time period for which personal information is stored and when it will be deleted or anonymized. Here are examples of some keywords, terms, and phrases that commonly identify "data retention" in privacy policies: "retention period", "how long we keep your data", “retaining your information”, "storage duration", "duration", "keep your data", “hold your information”, “hold your information any longer than we have to”, etc. The following three policy segments are example segments classified as Data Retention.

    Example Policy Segment 1: “We retain personal information for as long as necessary to provide our service; to administer and operate our business; to research, analyze, and improve our services; to operate our ad supported subscription plan; for safety, security, and fraud prevention; and/or to enforce our Terms of Use.”
    Classification: Data Retention

    Example Policy Segment 2: “Storage of personal information is based on many factors such as the nature of the personal information, and the need to defend or resolve current or anticipated legal claims.”
    Classification: Data Retention

    Example Policy Segment 3: “We keep your personal information, including sensitive personal information, as long as we need it to provide our products, comply with legal obligations or protect our or other’s interests. We decide how long we need information on a case-by-case basis.”
    Classification: Data Retention

    Category 6. Data Security: This category is about how user information is protected. In particular, it means the security measures that ensure security of personal data, including encryption or storage of data on secure servers. It also includes processing user data to improve safety and reliability of products, services, and users. Here are examples of some keywords, terms, and phrases that commonly identify "data security" in privacy policies: “security, fraud and abuse prevention”, “information security”, “security tips”, “security measures”, “security features”, “security partners”, “security controls”, “encryption”, “data breach procedure”, “secure server”, “firewalls and antivirus software”, “appropriate technical and organizational measures to safeguard personal information”, etc. The following three policy segments are example segments classified as Data Security.

    Example Policy Segment 1: “We will share your personal information if the disclosure of information is reasonably necessary to Detect, prevent, or otherwise address fraud, security, or technical issues.”
    Classification: Data Security

    Example Policy Segment 2: “For safety, security, and fraud prevention we process personal information such as personal details, payment details, profile information, usage information, advertising information.”
    Classification: Data Security

    Example Policy Segment 3: “We follow appropriate technical and organizational measures to safeguard personal information, including regular security reviews and updates to our data breach procedures.”
    Classification: Data Security

    Category 7. Policy Change: This category is about if and how users will be informed about changes to the privacy policy. Here are examples of some keywords, terms, and phrases that commonly identify "policy change" in privacy policies: “notify you about upcoming changes”, “we change this privacy policy from time to time”, “email notification of privacy policy changes”, “notification of changes”, “revisions to this policy”, “policy update alert”, “how we will inform you”, etc. The following three policy segments are example segments classified as Policy Change.

    Example Policy Segment 1: “We use your information, like your email address, to notify you about upcoming changes to your subscription.”
    Classification: Policy Change

    Example Policy Segment 2: “This privacy policy is subject to change from time to time. We will post revisions on our site and provide a policy update alert in our user interface.”
    Classification: Policy Change

    Example Policy Segment 3: “In the event of significant changes in privacy policy, we will provide a more prominent notice via email notification.”
    Classification: Policy Change

    Category 8. Do Not Track: This category is about if and how Do Not Track signals for online tracking and advertising are honored. Examples of keywords, terms, and phrases that commonly reflect "Do Not Track" in privacy policies include: “you can switch off some cookies and similar tracking technologies”, “online tracking preferences”, “do not track”, “behavioral tracking opt-out”, “opting-out of tracking”, etc. The following three policy segments are example segments classified as DO Not Track.

    Example Policy Segment 1: “Our website respects 'Do Not Track' signals and does not track users who have set their browsers to decline tracking cookies.”
    Classification: Do Not Track

    Example Policy Segment 2: “We do not currently respond to web browser “do not track" signals.”
    Classification: Do Not Track

    Example Policy Segment 3: “You have right to opt-out of Targeted Advertising or location tracking.”
    Classification: Do Not Track

    Category 9. International and Specific Audiences: This category is about practices that pertain only to a specific group of users (e.g., children, Europeans, or California residents). It outlines specific provisions that apply exclusively to certain categories of users, such as children, residents of Europe, or individuals living in California. The privacy policy includes clauses for these distinct user groups. Here are examples of some keywords, terms, and phrases that commonly identify international audiences or specific audiences in privacy policies: “child permissions”, “special protection of children's personal data”, “age-specific guidelines”, “kids profile”, “parental consent”, “children and teens”, “international users”, “regional laws”, “GDPR” (General Data Protection Regulation for European users), “CCPA” (California Consumer Privacy Act for California residents), “COPPA” (Children's Online Privacy Protection Act), “ CIPA” (Children’s Internet Protection Act in United States), “specific audience considerations”, “disclosure and international transfers”, “supplemental privacy disclosures for certain services and regions”, etc. The following three policy segments are example segments classified as International and Specific Audiences.

    Example Policy Segment 1: “Our services comply with the Data Protection Directive (also know as Directive 95/46/EC) to protect the privacy of our European users.”
    Classification: International and Specific Audiences

    Example Policy Segment 2: “Parental consent is required before creating a kids profile on our platform, adhering to the Children's Online Privacy Protection Act (COPPA).”
    Classification: International and Specific Audiences

    Example Policy Segment 3: “We may collect sensitive or personal information, as defined in U.S. Privacy Laws.”
    Classification: International and Specific Audiences

    I have a specific task for you: I will give you a sentence from a privacy policy, and you will classify the sentence with one of these nine data practice categories. Please only respond with one of the nine categories for each sentence.
"""

PROMPT_XIIa = """
Websites and digital products have privacy policies. A data practice means how the data is used and processed by an organization. A sentence (policy segment) in a privacy policy can be annotated with one of the following nine data practice categories:

    Category 1. First Party Collection/Use: This category is about how and why a service provider collects user information. In first party collection, the service provider that owns or operates the website/platform/service directly collects data from individuals. For instance, when a customer engages with the services of company A, company A collects data such as the products they have browsed, their purchasing choices, or their behavior patterns. When company A makes a product recommendation to a customer based on this data, it can be referred to as first-party advertising. In this case, collection and use of personal data is identified as first party data collection and use. In privacy policies, certain keywords and phrases can help to identify if the data collection or use is first party. For example: "We collect", "Data you provide", "Information we collect", "Our servers", "Our cookies", "We use your data" "Data collected from your interaction with our services", "Information you submit", “We restrict access to personal information to our employees, contractors, and agents”, etc. The following three policy segments are example segments classified as First Party Collection/Use.

    Category 2. Third Party Sharing/Collection: This category is about how user information may be shared with or collected by third parties. In third party sharing/collection an entity other than the service provider collects data from users through the service provider's platform. Third parties could include advertisers, ad network companies, analytic companies, or partner services that have their own data collection and privacy practices. Third-party entities often work with a variety of first-party websites, collecting information on user profiles from diverse sources, including news, weather, entertainment, and travel websites. For instance, if a customer uses Amazon.com's services and Amazon utilizes details about the user that have been collected by companies other than itself, this is known as third-party data collection and use. In privacy policies, certain keywords and phrases can help to identify if the data collection or use is third-party. For example: "Third-party providers", "External partners", "Ad networks", "Data we share" "Cookies from third-party advertisers", "Third-party cookies", "Third-party analytics", "Our partners’ services", “data processors”, etc. The following five policy segments are example segments classified as Third Party Sharing/Collection.

    Category 3. User Choice/Control: This category is about choices and control options available to users. Choice means giving individuals options as to how their personal information may be used. Specifically, choice relates to secondary uses of information—that is, uses beyond those necessary to complete the contemplated transaction. Control means privacy controls that allow individuals to manage use and sharing of their data. Example for choice/control can be following: “opt-in”, “opt-out”, “cookie preference” (functional/recommended/essential/performance/advertising), “location data controls”, “privacy control”, “communication preference”, “do-not-track”, “do-not-sell”, “withdraw consent”, etc. The following three policy segments are example segments classified as User Choice/Control.

    Category 4. User Access, Edit, and Deletion: This category is about if and how users may access, edit, or delete their information. These are privacy rights-based choices. In privacy policies such provision can be found in the following keywords and phrases: "right to access", “rights you have”, "request a copy", "view your information", "download your data", "personal data report", "obtain a copy", “how do I change my information”, “ how can I move my information”, "data subject access request", “delete information”, etc. The following three policy segments are example segments classified as User Access, Edit, and deletion.

    Category 5. Data Retention: This category is about how long user information is stored. Retention period outlines the time period for which personal information is stored and when it will be deleted or anonymized. Here are examples of some keywords, terms, and phrases that commonly identify "data retention" in privacy policies: "retention period", "how long we keep your data", “retaining your information”, "storage duration", "duration", "keep your data", “hold your information”, “hold your information any longer than we have to”, etc. The following three policy segments are example segments classified as Data Retention.

    Category 6. Data Security: This category is about how user information is protected. In particular, it means the security measures that ensure security of personal data, including encryption or storage of data on secure servers. It also includes processing user data to improve safety and reliability of products, services, and users. Here are examples of some keywords, terms, and phrases that commonly identify "data security" in privacy policies: “security, fraud and abuse prevention”, “information security”, “security tips”, “security measures”, “security features”, “security partners”, “security controls”, “encryption”, “data breach procedure”, “secure server”, “firewalls and antivirus software”, “appropriate technical and organizational measures to safeguard personal information”, etc. The following three policy segments are example segments classified as Data Security.

    Category 7. Policy Change: This category is about if and how users will be informed about changes to the privacy policy. Here are examples of some keywords, terms, and phrases that commonly identify "policy change" in privacy policies: “notify you about upcoming changes”, “we change this privacy policy from time to time”, “email notification of privacy policy changes”, “notification of changes”, “revisions to this policy”, “policy update alert”, “how we will inform you”, etc. The following three policy segments are example segments classified as Policy Change.

    Category 8. Do Not Track: This category is about if and how Do Not Track signals for online tracking and advertising are honored. Examples of keywords, terms, and phrases that commonly reflect "Do Not Track" in privacy policies include: “you can switch off some cookies and similar tracking technologies”, “online tracking preferences”, “do not track”, “behavioral tracking opt-out”, “opting-out of tracking”, etc. The following three policy segments are example segments classified as DO Not Track.

    Category 9. International and Specific Audiences: This category is about practices that pertain only to a specific group of users (e.g., children, Europeans, or California residents). It outlines specific provisions that apply exclusively to certain categories of users, such as children, residents of Europe, or individuals living in California. The privacy policy includes clauses for these distinct user groups. Here are examples of some keywords, terms, and phrases that commonly identify international audiences or specific audiences in privacy policies: “child permissions”, “special protection of children's personal data”, “age-specific guidelines”, “kids profile”, “parental consent”, “children and teens”, “international users”, “regional laws”, “GDPR” (General Data Protection Regulation for European users), “CCPA” (California Consumer Privacy Act for California residents), “COPPA” (Children's Online Privacy Protection Act), “ CIPA” (Children’s Internet Protection Act in United States), “specific audience considerations”, “disclosure and international transfers”, “supplemental privacy disclosures for certain services and regions”, etc. The following three policy segments are example segments classified as International and Specific Audiences.

    Task:
    I will give you a sentence from a privacy policy, and you will classify the sentence into one of these nine data practice categories. Please only respond with one of the nine categories for each sentence. Please follow these steps:

    Read the sentence carefully.
    •   Identify keywords and phrases that indicate a specific data practice.
    •   Match these indicators with the descriptions of the nine categories.
    •   Determine the most appropriate category for the sentence.

    Let's work through a few examples to demonstrate this process:

    Example Sentence 1: “We collect the following categories of personal information about you: name, email address, profile information, payment details, and device IDs.”
    •   Step 1: Read the sentence carefully.
    •   Step 2: Identify keywords such as "We collect," "personal information," and specific data types listed.
    •   Step 3: Match these indicators with the descriptions of the nine categories.
    •   Step 4: Determine that this sentence fits the First Party Collection/Use category.

    Example Sentence 2: “Our website uses third-party analytics services to help understand your usage of our services.”
    •   Step 1: Read the sentence carefully.
    •   Step 2: Identify keywords such as "third-party analytics services."
    •   Step 3: Match these indicators with the descriptions of the nine categories.
    •   Step 4: Determine that this sentence fits the Third Party Sharing/Collection category.
    Now, you try. Here is a sentence for you to classify:
"""

PROMPT_XIIIa = """
Websites and digital products have privacy policies. A data practice means how the data is used and processed by an organization. A sentence (policy segment) in a privacy policy can be annotated with one of the following nine data practice categories:

    Category 1. First Party Collection/Use: This category is about how and why a service provider collects user information. In first party collection, the service provider that owns or operates the website/platform/service directly collects data from individuals. For instance, when a customer engages with the services of company A, company A collects data such as the products they have browsed, their purchasing choices, or their behavior patterns. When company A makes a product recommendation to a customer based on this data, it can be referred to as first-party advertising. In this case, collection and use of personal data is identified as first party data collection and use. In privacy policies, certain keywords and phrases can help to identify if the data collection or use is first party. For example: "We collect", "Data you provide", "Information we collect", "Our servers", "Our cookies", "We use your data" "Data collected from your interaction with our services", "Information you submit", “We restrict access to personal information to our employees, contractors, and agents”, etc. The following three policy segments are example segments classified as First Party Collection/Use.

    Category 2. Third Party Sharing/Collection: This category is about how user information may be shared with or collected by third parties. In third party sharing/collection an entity other than the service provider collects data from users through the service provider's platform. Third parties could include advertisers, ad network companies, analytic companies, or partner services that have their own data collection and privacy practices. Third-party entities often work with a variety of first-party websites, collecting information on user profiles from diverse sources, including news, weather, entertainment, and travel websites. For instance, if a customer uses Amazon.com's services and Amazon utilizes details about the user that have been collected by companies other than itself, this is known as third-party data collection and use. In privacy policies, certain keywords and phrases can help to identify if the data collection or use is third-party. For example: "Third-party providers", "External partners", "Ad networks", "Data we share" "Cookies from third-party advertisers", "Third-party cookies", "Third-party analytics", "Our partners’ services", “data processors”, etc. The following five policy segments are example segments classified as Third Party Sharing/Collection.

    Category 3. User Choice/Control: This category is about choices and control options available to users. Choice means giving individuals options as to how their personal information may be used. Specifically, choice relates to secondary uses of information—that is, uses beyond those necessary to complete the contemplated transaction. Control means privacy controls that allow individuals to manage use and sharing of their data. Example for choice/control can be following: “opt-in”, “opt-out”, “cookie preference” (functional/recommended/essential/performance/advertising), “location data controls”, “privacy control”, “communication preference”, “do-not-track”, “do-not-sell”, “withdraw consent”, etc. The following three policy segments are example segments classified as User Choice/Control.

    Category 4. User Access, Edit, and Deletion: This category is about if and how users may access, edit, or delete their information. These are privacy rights-based choices. In privacy policies such provision can be found in the following keywords and phrases: "right to access", “rights you have”, "request a copy", "view your information", "download your data", "personal data report", "obtain a copy", “how do I change my information”, “ how can I move my information”, "data subject access request", “delete information”, etc. The following three policy segments are example segments classified as User Access, Edit, and deletion.

    Category 5. Data Retention: This category is about how long user information is stored. Retention period outlines the time period for which personal information is stored and when it will be deleted or anonymized. Here are examples of some keywords, terms, and phrases that commonly identify "data retention" in privacy policies: "retention period", "how long we keep your data", “retaining your information”, "storage duration", "duration", "keep your data", “hold your information”, “hold your information any longer than we have to”, etc. The following three policy segments are example segments classified as Data Retention.

    Category 6. Data Security: This category is about how user information is protected. In particular, it means the security measures that ensure security of personal data, including encryption or storage of data on secure servers. It also includes processing user data to improve safety and reliability of products, services, and users. Here are examples of some keywords, terms, and phrases that commonly identify "data security" in privacy policies: “security, fraud and abuse prevention”, “information security”, “security tips”, “security measures”, “security features”, “security partners”, “security controls”, “encryption”, “data breach procedure”, “secure server”, “firewalls and antivirus software”, “appropriate technical and organizational measures to safeguard personal information”, etc. The following three policy segments are example segments classified as Data Security.

    Category 7. Policy Change: This category is about if and how users will be informed about changes to the privacy policy. Here are examples of some keywords, terms, and phrases that commonly identify "policy change" in privacy policies: “notify you about upcoming changes”, “we change this privacy policy from time to time”, “email notification of privacy policy changes”, “notification of changes”, “revisions to this policy”, “policy update alert”, “how we will inform you”, etc. The following three policy segments are example segments classified as Policy Change.

    Category 8. Do Not Track: This category is about if and how Do Not Track signals for online tracking and advertising are honored. Examples of keywords, terms, and phrases that commonly reflect "Do Not Track" in privacy policies include: “you can switch off some cookies and similar tracking technologies”, “online tracking preferences”, “do not track”, “behavioral tracking opt-out”, “opting-out of tracking”, etc. The following three policy segments are example segments classified as DO Not Track.

    Category 9. International and Specific Audiences: This category is about practices that pertain only to a specific group of users (e.g., children, Europeans, or California residents). It outlines specific provisions that apply exclusively to certain categories of users, such as children, residents of Europe, or individuals living in California. The privacy policy includes clauses for these distinct user groups. Here are examples of some keywords, terms, and phrases that commonly identify international audiences or specific audiences in privacy policies: “child permissions”, “special protection of children's personal data”, “age-specific guidelines”, “kids profile”, “parental consent”, “children and teens”, “international users”, “regional laws”, “GDPR” (General Data Protection Regulation for European users), “CCPA” (California Consumer Privacy Act for California residents), “COPPA” (Children's Online Privacy Protection Act), “ CIPA” (Children’s Internet Protection Act in United States), “specific audience considerations”, “disclosure and international transfers”, “supplemental privacy disclosures for certain services and regions”, etc. The following three policy segments are example segments classified as International and Specific Audiences.

    Task:
    I will give you a sentence from a privacy policy, and you will classify the sentence into one of these nine data practice categories. Please only respond with one of the nine categories for each sentence. Please follow these steps:
    •   Read the sentence carefully.
    •   Identify keywords and phrases that indicate a specific data practice.
    •   Match these indicators with the descriptions of the nine categories.
    •   Determine the most appropriate category for the sentence.

    Let's work through a few examples to demonstrate this process:

    Example Sentence 1: “We collect the following categories of personal information about you: name, email address, profile information, payment details, and device IDs.”
    •   Step 1: Read the sentence carefully.
    o   The sentence is about collecting personal information.
    •   Step 2: Identify keywords such as "We collect," "personal information," and specific data types listed.
    o   Keywords identified: "We collect," "categories of personal information," "name," "email address," "profile information," "payment details," "device IDs."
    •   Step 3: Match these indicators with the descriptions of the nine categories.
    o   The sentence describes data collected directly by the service provider.
    •   Step 4: Determine that this sentence fits the First Party Collection/Use category.

    Example Sentence 2: “Our website uses third-party analytics services to help understand your usage of our services.”
    •   Step 1: Read the sentence carefully.
    o   The sentence is about using third-party services.
    •   Step 2: Identify keywords such as "third-party analytics services."
    o   Keywords identified: "third-party," "analytics services."
    •   Step 3: Match these indicators with the descriptions of the nine categories.
    o   The sentence describes data shared with third parties.
    •   Step 4: Determine that this sentence fits the Third Party Sharing/Collection category.

    Example Policy Segment 3: “If you wish to withdraw your consent at any time for any data processing we perform you can do so through our user settings page under privacy control.”
    •   Step 1: Read the sentence carefully.
    o   The sentence is about withdrawing consent for data processing.
    •   Step 2: Identify keywords such as "withdraw your consent" and "privacy control."
    o   Keywords identified: "withdraw your consent," "data processing," "user settings page," "privacy control."
    •   Step 3: Match these indicators with the descriptions of the nine categories.
    o   The sentence describes user control over data usage.
    •   Step 4: Determine that this sentence fits the User Choice/Control category.

    Example Policy Segment 4: “If you need to edit your information, you can do so by logging into your profile. For any modifications that are not available online, you may submit a request to our support team.”
    •   Step 1: Read the sentence carefully.
    o   The sentence is about editing personal information.
    •   Step 2: Identify keywords such as "edit your information" and "submit a request to our support team."
    o   Keywords identified: "edit your information," "logging into your profile," "submit a request," "support team."
    •   Step 3: Match these indicators with the descriptions of the nine categories.
    o   The sentence describes user access to data.
    •   Step 4: Determine that this sentence fits the User Access, Edit, and Deletion category.

    Example Policy Segment 5: “We keep your personal information, including sensitive personal information, as long as we need it to provide our products, comply with legal obligations, or protect our or others’ interests. We decide how long we need information on a case-by-case basis.”
    •   Step 1: Read the sentence carefully.
    o   The sentence is about the duration of keeping personal information.
    •   Step 2: Identify keywords such as "keep your personal information" and "case-by-case basis."
    o   Keywords identified: "keep your personal information," "sensitive personal information," "as long as we need it," "case-by-case basis."
    •   Step 3: Match these indicators with the descriptions of the nine categories.
    o   The sentence describes how long data is kept.
    •   Step 4: Determine that this sentence fits the Data Retention category.

    Example Policy Segment 6: “For safety, security, and fraud prevention, we process personal information such as personal details, payment details, profile information, usage information, advertising information.”
    •   Step 1: Read the sentence carefully.
    o   The sentence is about processing information for security reasons.
    •   Step 2: Identify keywords such as "safety, security, and fraud prevention" and "process personal information."
    o   Keywords identified: "safety," "security," "fraud prevention," "process personal information," "personal details," "payment details," "profile information," "usage information," "advertising information."
    •   Step 3: Match these indicators with the descriptions of the nine categories.
    o   The sentence describes measures taken to protect data.
    •   Step 4: Determine that this sentence fits the Data Security category.

    Example Policy Segment 7: “This privacy policy is subject to change from time to time. We will post revisions on our site and provide a policy update alert in our user interface.”
    •   Step 1: Read the sentence carefully.
    o   The sentence is about notifying users about policy changes.
    •   Step 2: Identify keywords such as "privacy policy is subject to change" and "policy update alert."
    o   Keywords identified: "privacy policy," "subject to change," "post revisions," "policy update alert," "user interface."
    •   Step 3: Match these indicators with the descriptions of the nine categories.
    o   The sentence describes how policy changes are communicated.
    •   Step 4: Determine that this sentence fits the Policy Change category.

    Example Policy Segment 8: “You have the right to opt out of Targeted Advertising or location tracking.”
    •   Step 1: Read the sentence carefully.
    o   The sentence is about opting out of tracking.
    •   Step 2: Identify keywords such as "opt out of Targeted Advertising" and "location tracking."
    o   Keywords identified: "right to opt out," "Targeted Advertising," "location tracking."
    •   Step 3: Match these indicators with the descriptions of the nine categories.
    o   The sentence describes user control over tracking.
    •   Step 4: Determine that this sentence fits the Do Not Track category.

    Example Policy Segment 9: “Parental consent is required before creating a kids profile on our platform, adhering to the Children's Online Privacy Protection Act (COPPA).”
    •   Step 1: Read the sentence carefully.
    o   The sentence is about obtaining parental consent for children’s data.
    •   Step 2: Identify keywords such as "Parental consent" and "Children's Online Privacy Protection Act."
    o   Keywords identified: "Parental consent," "kids profile," "Children's Online Privacy Protection Act," "COPPA."
    •   Step 3: Match these indicators with the descriptions of the nine categories.
    o   The sentence describes practices specific to children.
    •   Step 4: Determine that this sentence fits the International and Specific Audiences category.

    Please respond with only one of the nine categories for each sentence. Only include the category in the response. Now, you try. Here is a sentence for you to classify:
"""

PROMPT_COT1 = """
Websites and digital products have privacy policies. A data practice means how the data is used and processed by an organization. A sentence (policy segment) in a privacy policy can be annotated with one of the following nine data practice categories:

    Category 1. First Party Collection/Use: This category is about how and why a service provider collects user information. In first party collection, the service provider that owns or operates the website/platform/service directly collects data from individuals. For instance, when a customer engages with the services of company A, company A collects data such as the products they have browsed, their purchasing choices, or their behavior patterns. When company A makes a product recommendation to a customer based on this data, it can be referred to as first-party advertising. In this case, collection and use of personal data is identified as first party data collection and use. In privacy policies, certain keywords and phrases can help to identify if the data collection or use is first party. For example: "We collect", "Data you provide", "Information we collect", "Our servers", "Our cookies", "We use your data" "Data collected from your interaction with our services", "Information you submit", “We restrict access to personal information to our employees, contractors, and agents”, etc. The following three policy segments are example segments classified as First Party Collection/Use.

    Category 2. Third Party Sharing/Collection: This category is about how user information may be shared with or collected by third parties. In third party sharing/collection an entity other than the service provider collects data from users through the service provider's platform. Third parties could include advertisers, ad network companies, analytic companies, or partner services that have their own data collection and privacy practices. Third-party entities often work with a variety of first-party websites, collecting information on user profiles from diverse sources, including news, weather, entertainment, and travel websites. For instance, if a customer uses Amazon.com's services and Amazon utilizes details about the user that have been collected by companies other than itself, this is known as third-party data collection and use. In privacy policies, certain keywords and phrases can help to identify if the data collection or use is third-party. For example: "Third-party providers", "External partners", "Ad networks", "Data we share" "Cookies from third-party advertisers", "Third-party cookies", "Third-party analytics", "Our partners’ services", “data processors”, etc. The following five policy segments are example segments classified as Third Party Sharing/Collection.

    Category 3. User Choice/Control: This category is about choices and control options available to users. Choice means giving individuals options as to how their personal information may be used. Specifically, choice relates to secondary uses of information—that is, uses beyond those necessary to complete the contemplated transaction. Control means privacy controls that allow individuals to manage use and sharing of their data. Example for choice/control can be following: “opt-in”, “opt-out”, “cookie preference” (functional/recommended/essential/performance/advertising), “location data controls”, “privacy control”, “communication preference”, “do-not-track”, “do-not-sell”, “withdraw consent”, etc. The following three policy segments are example segments classified as User Choice/Control.

    Category 4. User Access, Edit, and Deletion: This category is about if and how users may access, edit, or delete their information. These are privacy rights-based choices. In privacy policies such provision can be found in the following keywords and phrases: "right to access", “rights you have”, "request a copy", "view your information", "download your data", "personal data report", "obtain a copy", “how do I change my information”, “ how can I move my information”, "data subject access request", “delete information”, etc. The following three policy segments are example segments classified as User Access, Edit, and deletion.

    Category 5. Data Retention: This category is about how long user information is stored. Retention period outlines the time period for which personal information is stored and when it will be deleted or anonymized. Here are examples of some keywords, terms, and phrases that commonly identify "data retention" in privacy policies: "retention period", "how long we keep your data", “retaining your information”, "storage duration", "duration", "keep your data", “hold your information”, “hold your information any longer than we have to”, etc. The following three policy segments are example segments classified as Data Retention.

    Category 6. Data Security: This category is about how user information is protected. In particular, it means the security measures that ensure security of personal data, including encryption or storage of data on secure servers. It also includes processing user data to improve safety and reliability of products, services, and users. Here are examples of some keywords, terms, and phrases that commonly identify "data security" in privacy policies: “security, fraud and abuse prevention”, “information security”, “security tips”, “security measures”, “security features”, “security partners”, “security controls”, “encryption”, “data breach procedure”, “secure server”, “firewalls and antivirus software”, “appropriate technical and organizational measures to safeguard personal information”, etc. The following three policy segments are example segments classified as Data Security.

    Category 7. Policy Change: This category is about if and how users will be informed about changes to the privacy policy. Here are examples of some keywords, terms, and phrases that commonly identify "policy change" in privacy policies: “notify you about upcoming changes”, “we change this privacy policy from time to time”, “email notification of privacy policy changes”, “notification of changes”, “revisions to this policy”, “policy update alert”, “how we will inform you”, etc. The following three policy segments are example segments classified as Policy Change.

    Category 8. Do Not Track: This category is about if and how Do Not Track signals for online tracking and advertising are honored. Examples of keywords, terms, and phrases that commonly reflect "Do Not Track" in privacy policies include: “you can switch off some cookies and similar tracking technologies”, “online tracking preferences”, “do not track”, “behavioral tracking opt-out”, “opting-out of tracking”, etc. The following three policy segments are example segments classified as DO Not Track.

    Category 9. International and Specific Audiences: This category is about practices that pertain only to a specific group of users (e.g., children, Europeans, or California residents). It outlines specific provisions that apply exclusively to certain categories of users, such as children, residents of Europe, or individuals living in California. The privacy policy includes clauses for these distinct user groups. Here are examples of some keywords, terms, and phrases that commonly identify international audiences or specific audiences in privacy policies: “child permissions”, “special protection of children's personal data”, “age-specific guidelines”, “kids profile”, “parental consent”, “children and teens”, “international users”, “regional laws”, “GDPR” (General Data Protection Regulation for European users), “CCPA” (California Consumer Privacy Act for California residents), “COPPA” (Children's Online Privacy Protection Act), “ CIPA” (Children’s Internet Protection Act in United States), “specific audience considerations”, “disclosure and international transfers”, “supplemental privacy disclosures for certain services and regions”, etc. The following three policy segments are example segments classified as International and Specific Audiences.

    Task:
        I will give you a sentence from a privacy policy, and you will classify the sentence into one of these nine data practice categories. Please only respond with one of the nine categories for each sentence. Please follow these steps:
        •   Read the sentence carefully.
        •   Identify keywords and phrases that indicate a specific data practice.
        •   Match these indicators with the descriptions of the nine categories.
        •   Determine the most appropriate category for the sentence.

        Let's work through a few examples to demonstrate this process:

        Example Sentence 1: “We collect the following categories of personal information about you: name, email address, profile information, payment details, and device IDs.”
        •   Step 1: Read the sentence carefully.
        o   The sentence is about collecting personal information.
        •   Step 2: Identify keywords such as "We collect," "personal information," and specific data types listed.
        o   Keywords identified: "We collect," "categories of personal information," "name," "email address," "profile information," "payment details," "device IDs."
        •   Step 3: Match these indicators with the descriptions of the nine categories.
        o   The sentence describes data collected directly by the service provider.
        •   Step 4: Determine that this sentence fits the First Party Collection/Use category.

        Example Sentence 2: “Our website uses third-party analytics services to help understand your usage of our services.”
        •   Step 1: Read the sentence carefully.
        o   The sentence is about using third-party services.
        •   Step 2: Identify keywords such as "third-party analytics services."
        o   Keywords identified: "third-party," "analytics services."
        •   Step 3: Match these indicators with the descriptions of the nine categories.
        o   The sentence describes data shared with third parties.
        •   Step 4: Determine that this sentence fits the Third Party Sharing/Collection category.

        Now, you try. Please only respond with one of the nine categories for each sentence. Here is a sentence for you to classify:
"""

PROMPT_COT2 = """
Websites and digital products have privacy policies. A data practice means how the data is used and processed by an organization. A sentence (policy segment) in a privacy policy can be annotated with one of the following nine data practice categories:

    Category 1. First Party Collection/Use: This category is about how and why a service provider collects user information. In first party collection, the service provider that owns or operates the website/platform/service directly collects data from individuals. For instance, when a customer engages with the services of company A, company A collects data such as the products they have browsed, their purchasing choices, or their behavior patterns. When company A makes a product recommendation to a customer based on this data, it can be referred to as first-party advertising. In this case, collection and use of personal data is identified as first party data collection and use. In privacy policies, certain keywords and phrases can help to identify if the data collection or use is first party. For example: "We collect", "Data you provide", "Information we collect", "Our servers", "Our cookies", "We use your data" "Data collected from your interaction with our services", "Information you submit", “We restrict access to personal information to our employees, contractors, and agents”, etc. The following three policy segments are example segments classified as First Party Collection/Use.

    Category 2. Third Party Sharing/Collection: This category is about how user information may be shared with or collected by third parties. In third party sharing/collection an entity other than the service provider collects data from users through the service provider's platform. Third parties could include advertisers, ad network companies, analytic companies, or partner services that have their own data collection and privacy practices. Third-party entities often work with a variety of first-party websites, collecting information on user profiles from diverse sources, including news, weather, entertainment, and travel websites. For instance, if a customer uses Amazon.com's services and Amazon utilizes details about the user that have been collected by companies other than itself, this is known as third-party data collection and use. In privacy policies, certain keywords and phrases can help to identify if the data collection or use is third-party. For example: "Third-party providers", "External partners", "Ad networks", "Data we share" "Cookies from third-party advertisers", "Third-party cookies", "Third-party analytics", "Our partners’ services", “data processors”, etc. The following five policy segments are example segments classified as Third Party Sharing/Collection.

    Category 3. User Choice/Control: This category is about choices and control options available to users. Choice means giving individuals options as to how their personal information may be used. Specifically, choice relates to secondary uses of information—that is, uses beyond those necessary to complete the contemplated transaction. Control means privacy controls that allow individuals to manage use and sharing of their data. Example for choice/control can be following: “opt-in”, “opt-out”, “cookie preference” (functional/recommended/essential/performance/advertising), “location data controls”, “privacy control”, “communication preference”, “do-not-track”, “do-not-sell”, “withdraw consent”, etc. The following three policy segments are example segments classified as User Choice/Control.

    Category 4. User Access, Edit, and Deletion: This category is about if and how users may access, edit, or delete their information. These are privacy rights-based choices. In privacy policies such provision can be found in the following keywords and phrases: "right to access", “rights you have”, "request a copy", "view your information", "download your data", "personal data report", "obtain a copy", “how do I change my information”, “ how can I move my information”, "data subject access request", “delete information”, etc. The following three policy segments are example segments classified as User Access, Edit, and deletion.

    Category 5. Data Retention: This category is about how long user information is stored. Retention period outlines the time period for which personal information is stored and when it will be deleted or anonymized. Here are examples of some keywords, terms, and phrases that commonly identify "data retention" in privacy policies: "retention period", "how long we keep your data", “retaining your information”, "storage duration", "duration", "keep your data", “hold your information”, “hold your information any longer than we have to”, etc. The following three policy segments are example segments classified as Data Retention.

    Category 6. Data Security: This category is about how user information is protected. In particular, it means the security measures that ensure security of personal data, including encryption or storage of data on secure servers. It also includes processing user data to improve safety and reliability of products, services, and users. Here are examples of some keywords, terms, and phrases that commonly identify "data security" in privacy policies: “security, fraud and abuse prevention”, “information security”, “security tips”, “security measures”, “security features”, “security partners”, “security controls”, “encryption”, “data breach procedure”, “secure server”, “firewalls and antivirus software”, “appropriate technical and organizational measures to safeguard personal information”, etc. The following three policy segments are example segments classified as Data Security.

    Category 7. Policy Change: This category is about if and how users will be informed about changes to the privacy policy. Here are examples of some keywords, terms, and phrases that commonly identify "policy change" in privacy policies: “notify you about upcoming changes”, “we change this privacy policy from time to time”, “email notification of privacy policy changes”, “notification of changes”, “revisions to this policy”, “policy update alert”, “how we will inform you”, etc. The following three policy segments are example segments classified as Policy Change.

    Category 8. Do Not Track: This category is about if and how Do Not Track signals for online tracking and advertising are honored. Examples of keywords, terms, and phrases that commonly reflect "Do Not Track" in privacy policies include: “you can switch off some cookies and similar tracking technologies”, “online tracking preferences”, “do not track”, “behavioral tracking opt-out”, “opting-out of tracking”, etc. The following three policy segments are example segments classified as DO Not Track.

    Category 9. International and Specific Audiences: This category is about practices that pertain only to a specific group of users (e.g., children, Europeans, or California residents). It outlines specific provisions that apply exclusively to certain categories of users, such as children, residents of Europe, or individuals living in California. The privacy policy includes clauses for these distinct user groups. Here are examples of some keywords, terms, and phrases that commonly identify international audiences or specific audiences in privacy policies: “child permissions”, “special protection of children's personal data”, “age-specific guidelines”, “kids profile”, “parental consent”, “children and teens”, “international users”, “regional laws”, “GDPR” (General Data Protection Regulation for European users), “CCPA” (California Consumer Privacy Act for California residents), “COPPA” (Children's Online Privacy Protection Act), “ CIPA” (Children’s Internet Protection Act in United States), “specific audience considerations”, “disclosure and international transfers”, “supplemental privacy disclosures for certain services and regions”, etc. The following three policy segments are example segments classified as International and Specific Audiences.

    Task:
    I will give you a sentence from a privacy policy, and you will classify the sentence into one of these nine data practice categories. Please only respond with one of the nine categories for each sentence. Please follow these steps:
    •   Read the sentence carefully.
    •   Identify keywords and phrases that indicate a specific data practice.
    •   Match these indicators with the descriptions of the nine categories.
    •   Determine the most appropriate category for the sentence.

    Let's work through a few examples to demonstrate this process:

    Example Sentence 1: “We collect the following categories of personal information about you: name, email address, profile information, payment details, and device IDs.”
    •   Step 1: Read the sentence carefully.
    o   The sentence is about collecting personal information.
    •   Step 2: Identify keywords such as "We collect," "personal information," and specific data types listed.
    o   Keywords identified: "We collect," "categories of personal information," "name," "email address," "profile information," "payment details," "device IDs."
    •   Step 3: Match these indicators with the descriptions of the nine categories.
    o   The sentence describes data collected directly by the service provider.
    •   Step 4: Determine that this sentence fits the First Party Collection/Use category.

    Example Sentence 2: “Our website uses third-party analytics services to help understand your usage of our services.”
    •   Step 1: Read the sentence carefully.
    o   The sentence is about using third-party services.
    •   Step 2: Identify keywords such as "third-party analytics services."
    o   Keywords identified: "third-party," "analytics services."
    •   Step 3: Match these indicators with the descriptions of the nine categories.
    o   The sentence describes data shared with third parties.
    •   Step 4: Determine that this sentence fits the Third Party Sharing/Collection category.

    Example Policy Segment 3: “If you wish to withdraw your consent at any time for any data processing we perform you can do so through our user settings page under privacy control.”
    •   Step 1: Read the sentence carefully.
    o   The sentence is about withdrawing consent for data processing.
    •   Step 2: Identify keywords such as "withdraw your consent" and "privacy control."
    o   Keywords identified: "withdraw your consent," "data processing," "user settings page," "privacy control."
    •   Step 3: Match these indicators with the descriptions of the nine categories.
    o   The sentence describes user control over data usage.
    •   Step 4: Determine that this sentence fits the User Choice/Control category.

    Example Policy Segment 4: “If you need to edit your information, you can do so by logging into your profile. For any modifications that are not available online, you may submit a request to our support team.”
    •   Step 1: Read the sentence carefully.
    o   The sentence is about editing personal information.
    •   Step 2: Identify keywords such as "edit your information" and "submit a request to our support team."
    o   Keywords identified: "edit your information," "logging into your profile," "submit a request," "support team."
    •   Step 3: Match these indicators with the descriptions of the nine categories.
    o   The sentence describes user access to data.
    •   Step 4: Determine that this sentence fits the User Access, Edit, and Deletion category.

    Example Policy Segment 5: “We keep your personal information, including sensitive personal information, as long as we need it to provide our products, comply with legal obligations, or protect our or others’ interests. We decide how long we need information on a case-by-case basis.”
    •   Step 1: Read the sentence carefully.
    o   The sentence is about the duration of keeping personal information.
    •   Step 2: Identify keywords such as "keep your personal information" and "case-by-case basis."
    o   Keywords identified: "keep your personal information," "sensitive personal information," "as long as we need it," "case-by-case basis."
    •   Step 3: Match these indicators with the descriptions of the nine categories.
    o   The sentence describes how long data is kept.
    •   Step 4: Determine that this sentence fits the Data Retention category.

    Example Policy Segment 6: “For safety, security, and fraud prevention, we process personal information such as personal details, payment details, profile information, usage information, advertising information.”
    •   Step 1: Read the sentence carefully.
    o   The sentence is about processing information for security reasons.
    •   Step 2: Identify keywords such as "safety, security, and fraud prevention" and "process personal information."
    o   Keywords identified: "safety," "security," "fraud prevention," "process personal information," "personal details," "payment details," "profile information," "usage information," "advertising information."
    •   Step 3: Match these indicators with the descriptions of the nine categories.
    o   The sentence describes measures taken to protect data.
    •   Step 4: Determine that this sentence fits the Data Security category.

    Example Policy Segment 7: “This privacy policy is subject to change from time to time. We will post revisions on our site and provide a policy update alert in our user interface.”
    •   Step 1: Read the sentence carefully.
    o   The sentence is about notifying users about policy changes.
    •   Step 2: Identify keywords such as "privacy policy is subject to change" and "policy update alert."
    o   Keywords identified: "privacy policy," "subject to change," "post revisions," "policy update alert," "user interface."
    •   Step 3: Match these indicators with the descriptions of the nine categories.
    o   The sentence describes how policy changes are communicated.
    •   Step 4: Determine that this sentence fits the Policy Change category.

    Example Policy Segment 8: “You have the right to opt out of Targeted Advertising or location tracking.”
    •   Step 1: Read the sentence carefully.
    o   The sentence is about opting out of tracking.
    •   Step 2: Identify keywords such as "opt out of Targeted Advertising" and "location tracking."
    o   Keywords identified: "right to opt out," "Targeted Advertising," "location tracking."
    •   Step 3: Match these indicators with the descriptions of the nine categories.
    o   The sentence describes user control over tracking.
    •   Step 4: Determine that this sentence fits the Do Not Track category.

    Example Policy Segment 9: “Parental consent is required before creating a kids profile on our platform, adhering to the Children's Online Privacy Protection Act (COPPA).”
    •   Step 1: Read the sentence carefully.
    o   The sentence is about obtaining parental consent for children’s data.
    •   Step 2: Identify keywords such as "Parental consent" and "Children's Online Privacy Protection Act."
    o   Keywords identified: "Parental consent," "kids profile," "Children's Online Privacy Protection Act," "COPPA."
    •   Step 3: Match these indicators with the descriptions of the nine categories.
    o   The sentence describes practices specific to children.
    •   Step 4: Determine that this sentence fits the International and Specific Audiences category.

    Now, you try. Please only respond with one of the nine categories for each sentence. Here is a sentence for you to classify:
"""
