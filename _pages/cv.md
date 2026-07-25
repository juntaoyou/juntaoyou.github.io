---
layout: archive
title: "CV"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}

Education
======
* B.S. in Artificial Intelligence, University of Science and Technology of China (USTC), 2022 – 2026
* Ph.D. in Artificial Intelligence, University of Science and Technology of China (USTC), 2026 – Present

Research Experience
======
* 2024 – 2026: Undergraduate Research Assistant
  * USTC Lab of Data Science
* 2026.4 – Present: Intern
  * Alibaba Qwen Business Group
  * Advisor: Prof. Fuli Feng
  * Mentor: Yang Zhang
  * Research Direction: LLM Personalization
  * Focus: Causal preference modeling, behavior sequence modeling, and neuron-level analysis of personalization in LLMs
  
Publications
======
  <ul>{% for post in site.publications reversed %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>

Skills
======
* Languages: Python (PyTorch, Transformers), C++, HTML/CSS/JavaScript, SQL
* ML/AI: LLM Fine-tuning, Recommendation Systems, Causal Inference, Machine Learning Algorithms
  
Talks
======
  <ul>{% for post in site.talks reversed %}
    {% include archive-single-talk-cv.html  %}
  {% endfor %}</ul>
  
Teaching
======
  <ul>{% for post in site.teaching reversed %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>
