# Idea Canvas — Candidate <B>

**Candidate name:** <Pricey>
**Date started:** <2026-08-31>   **Well it came from:** Online Shopping Experience

---

## 1. Problem statement

Concept Summary: A web application that finds the same exact product across multiple different online retailers to find the best price for the consumer
| Category | Description | Specific Example |
|---|---|---|
| **Software Type** | Web Application | |
| **For** | Users of online retailers like amazon, ebay, bestbuy, newegg, temu, etc. | Fred Warner is looking to a pair of new headphones and has found a specific pair he really likes. He wants to find the online retailer that will sell him the headphones for the best price |
| **Who** | Having to search for the same product across multiple different online retailers takes time and is inconvenient | Fred clicks through a wide variety of different retailers and is having to manually write down the prices and compare them. This takes up a lot of his time and is very inconvenient |
| **The Problem Is** | There is no way to compare the price of a specific product across a variety of online retailers. | Fred does not have the prices of his chosen pair of headphones in one consolidated place. This means he has to manually search for and compare the price across different retailers |
| **Which Costs** | Users can spend up to 20-30 additional minutes when online shopping looking for the best price | Fred spends 20 minutes before finding that bestbuy is selling his desired headphones for the best price |
| **Today They** | Users have to manually search through a wide variety of different online retailers to find the best price | Fred had to manually search through multiple different websites to find the best price for his headphones |
| **Which Falls Short Because** | It takes a lot of time and is very inconvenient | Fred had to spend 20 extra minutes searching for the best price |


## 2. Evidence a user exists

- **Person spoken to:** <Nikita Adamov>
- **Date and length:** <2026-09-05, 30 minutes>
- **Three verbatim quotes:**
  1. "<I typically use Amazon because it's the easiest to navigate and find what I'm looking for. Most of the time they have good reasonable prices>"
  2. "<Checking other sites is just too much of a hastle and takes too long for what its worth>"
  3. "<If I could find a better price in a reasonable time it could save me money and time>"
- **The workaround they already use:** <Sticks to one online retailer (Amazon)>     
  
## 3. Candidate scope (Must features only)

| # | Feature (one vertical slice each) | Hours |
|---|---|---:|
| 1 | API Connection to Online Retailers | 15 |
| 2 | Product Scanner for same or similar products across different APIs | 15 |
| 3 | Log in creation and profile management | 10 |
| 4 | Price calculator algorithm | 2 |
| 5 | Web Page scanner for product | 5 |
| | Walking skeleton + CI | 10 |
| | Deployment + clean-machine test | 10 |
| | **Construction total** | 67 |

Budget: plan on **60 hours**, hard ceiling **75**. Above 75 you are borrowing from
testing and documentation, which are graded.

## 4. Out of scope — will NOT be built

1. Mobile App       
2. Single Sign-on verification     
3. Email or text notifications     
4. User location tracking     
5. Social Networking platform    
6. Social Media platform   

## 5. Feasibility screen

| Gate | Verdict | Evidence (dated) |
|---|---|---|
| **Build** — novelty load 2 | pass | <Python (known), APIs (Known), HTML (known), MongoDB (unkown), Render (unknown) |
| **Get** — every dependency exercised for real | fail | <AWS Analytical API unable to be purchased because of Amazon Professional Selling Account costs $39.99 as of 2026-09-06> |
| **Ship** — Render has been selected as my deployment method, terms read | pass | <Render + pricing page read on 2026-09-06> |
| **Show** — a stranger sees it work in 10 minutes | pass | <1. Search for a product you want on a known online retailer. 2. Click on the web app drop down after finding desired product 3. Look through the list of other online retailers selling the same product 4. Select the online retailer you think will give you the best price 5. Use the "Find Best Price" function in Pricey to generate who will give the best price 6. click on the retailer you would like to buy from 7. review the price to verify the correct shipping and item cost 8. Click on the offer listed and be redirected to the retailer of your choice 9. buy the product 10. save money and time using Pricey > |

**Technologies:** <Python> (known) · <API> (Known) · <MongoDB> (new) · <Render> (new)
**Novelty load:** <2>

## 6. The one hard part

<The most difficult part of this project would be getting access to all the different online retailers product lists and updated statistical data on prices, shipping costs, and availability. After researching just one online retailer API (Amazon AWS) I discovered that I need to pay for a professional account to gain access to the "free" Product Statistic API which costs $39.99 a month. Hypothetically I could make a bunch of fake online retailers and put them in a MongoDB database with set product lists but it would not be applicable to the real world. >

## 7. Scorecard (1–5 each; weight in parentheses)

| Criterion | (w) | Score | Weighted |
|---|---:|---:|---:|
| Evidence a user exists | 3 | 5 | 15 |
| Fits ~45 hours of features | 3 | 3 | 9 |
| Novelty load | 2 | 2 | 4 |
| Dependencies verified | 2 | 3 | 6 |
| Demonstrable in ten minutes | 1 | 5 | 5 |
| **Total (max 55)** | | | 39 |

## 8. If this candidate is rejected

<The biggest reason that I would or have rejected this project idea is that it is too big of a project for a singluar person with no budget. In order for this project to work as intended and properly, I would need connection to all the major online retailer Product List APIs which are not all free and would cost a substantial amount of money (which I don't have). Hypothetically I could create a bunch of fake online retailers and give them fake products with ID numbers and prices to have the web application scan through and run a bunch of algorithms to find the best price. However, this would not be applicable to the actual demographic I want to deploy it to as it would not be taking real data>
