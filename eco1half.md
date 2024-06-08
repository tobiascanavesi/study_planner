A First Course in Mathematical Economics

# A First Course In Mathematical

Economics By Sunanda Roy Cambridge Scholars Publishing

![2_image_0.png](2_image_0.png)

A First Course in Mathematical Economics By Sunanda Roy This book first published 2020 Cambridge Scholars Publishing Lady Stephenson Library, Newcastle upon Tyne, NE6 2PA, UK
British Library Cataloguing in Publication Data A catalogue record for this book is available from the British Library Copyright © 2020 by Sunanda Roy All rights for this book reserved. No part of this book may be reproduced, stored in a retrieval system, or transmitted, in any form or by any means, electronic, mechanical, photocopying, recording or otherwise, without the prior permission of the copyright owner.

ISBN (10): 1-5275-4723-X ISBN (13): 978-1-5275-4723-0

# Contents

Preface Chapter 1 ...................................................................................................................1 Single Variable Functions: Basics Sets Functions Function composition Function inversion Functions and sets in economics Chapter 2 ..............................................................................................31 Common Types of Single Variable Functions Linear functions Polynomials Power functions Exponential functions Logarithmic Functions Chapter 3 ..............................................................................................................59 Single Variable Differentiable Functions and their Properties Properties related to the first order derivatives Properties related to the second order derivatives Parametric shifts of functions Chapter 4 ..................................................................................................83 Simple Linear Models in Economics Market model with linear demand and supply Budget sets The simple Keynesian model Chapter 5 ...............................................................................................115 Non-linear Functions in Economics Cost functions Production functions Revenue and profit functions Exponential and logarithmic functions in economics Chapter 6 ................................................................................................137 Single Variable Optimization in Economics Basic concepts The extreme value theorem Stationary values and extreme points Optimization in economics Chapter 7 ..............................................................................................159 Multivariate Functions Functions of two variables Partial derivatives Total differential Functions of more than two variables vi Chapter 8 ..............................................................................................187 Multivariate Tools and Optimization Implicit functions Homogeneous functions Concavity and convexity Extreme points of multivariate functions Multivariate optimization in economics Two useful results Chapter 9 .............................................................................................217 Simultaneous Linear Equation Systems An input-output economy Method of substitution Method of elimination Parametric solutions Elements of matrix algebra Chapter 10 Gaussian Method of Solving Linear Systems The Gaussian elimination method Linear systems with many solutions Chapter 11 ...............................................................................................275 Matrix Inversion Method of Solving Linear Systems Special types of matrices The matrix inversion solution method Determinants and adjoint of a matrix The Hessian matrix vii Chapter 12 ........................................................................................305 Constrained Optimization in economics Constrained optimization problems in economics Two-variable single constraint problems The Lagrangian method Sufficiency conditions Answers to End of Chapter Questions ......................................335

# Preface

## Purpose

The book is primarily intended for undergraduate economics or applied economics majors transitioning from a possibly nontechnical and introductory Principles course into a calculus based intermediate or senior level course in economics.

Assuming that college mathematics is part of their curriculum, students at this stage of the program are likely to be familiar with the basic techniques of differentiation and integration. They may, however, be unused to thinking about the real world in terms of functions and equations and may fail to appreciate the benefits of abstraction and parsimony that comes with the mathematical approach. These factors make their transition into intermediate economic theory and its applications especially difficult and challenging. Many instructors of intermediate level courses express a common related concern. A student may know how to obtain derivatives of functions in a math course setting and yet struggle to apply them in the study of optimizing behavior of economic agents.

The book provides a bridge from college math courses to based intermediate economics. Mathematical calculus techniques that are specifically most useful for formalizing and presenting economic ideas to an undergraduate audience are reviewed. The presentation style emphasizes the intuition underlying these techniques and their usefulness in economic analysis. Inclusion of mathematical proofs and non-essential technical details are kept at a minimum. Several chapters and sections within other chapters are devoted to the use of these tools to either formalize familiar concepts and ideas from introductory economics or provide an initial exposure to more advanced concepts one is likely to face in intermediate economic theory.

A reappraisal of familiar material from introductory courses using a mathematical approach is intended to motivate and make the transition to calculus-based economics courses easier. It provides a hands-on experience of the additional analytical power gained via formalism. The many worked out examples and in-text review and end of chapter exercises emphasize skills that are necessary to put tools into practice and solve problems in the upper level courses.

The book is designed as a companion volume to but not as a substitute for a textbook on intermediate economic theory.

Concepts and ideas from such courses are selectively discussed with the explicit purpose of illustrating the use of the mathematical techniques. The book does not attempt an indepth treatment of these topics. The book is ideal for a second or third year undergraduate mathematical methods course in a quantitatively oriented economics program. As a matter of fact, it grew out of the material developed for such a course offered at Iowa State University.

On a similar note, this is not a book on mathematics and does not cover all the mathematical tools a graduate student in economics ought to know although some may find it beneficial as a supplementary text. There are many excellent textbooks in the market that are appropriate for Masters or Ph.D. level courses. Much of this advanced material in mathematical economics has been intentionally excluded to make the book less intimidating and more user friendly for undergraduate students to whom it primarily caters. Readers in other disciplines and programs that require a working, but not a more advanced knowledge of mathematical economics may also find the book useful for the same reason.

## Prerequisites

The book assumes that students will have a working knowledge of basic calculus usually covered in first year college mathematics courses. This includes familiarity with the concepts of limit, continuity, differentiation and integration of functions and specifically, skills in these areas with respect to single variable functions. It also assumes that students would have taken Principles of microeconomics and macroeconomics.

## Topics Covered

The first three chapters review basic set theory and properties of differentiable single variable functions including properties of specific types of single variable functions that are most common in economic applications, such as polynomials, power functions, exponential and logarithmic functions. Tools that are especially useful in economics but often under-represented in other texts, such as parametric shifts of graphs and function inversion, are given more attention in these chapters. Chapters 4 and 5 employ these tools to formalize concepts and ideas from Principles courses. Chapter 6 is devoted to optimization of single variable functions. Chapter 7 and 8 are devoted to properties of multivariate functions, their optimization and other multivariate tools that are critical in intermediate economic theory. Chapters 9-11 cover matrix algebra and various solution techniques for linear systems. Finally, Chapter 12 provides a basic introduction to constrained maximization tools and applications.

## Acknowledgment

As mentioned earlier, the book grew out of the material developed for an undergraduate mathematical methods course that I taught at Iowa State University for many years. I owe a deep debt of gratitude to my colleague, Dr Arne Hallam, who conceived this course and taught it for many years before I took over as instructor. The class materials he passed on to me have been a major source of inspiration and ideas about what is important and useful to a beginner in mathematical economics.

I owe a similar debt of gratitude to my two graduate teaching assistants, Phillip and Stephen Herr, for their help in developing the in-text review exercises and end of chapter questions. I am grateful to my undergraduate teaching assistants Marcus Holloway, Lucy Dougherty and Katelyn Collins for their feedback on early versions of the first several chapters. I am especially keen to acknowledge Marcus for his help in preparing some of the graphs in Excel. Other graduate students who have assisted me in teaching the said course over many years have also enriched the book with their comments and suggestions on some of the included material. All remaining errors are mine.

The book would not have been written without the support of and encouragement from my husband, Tirthankar, and son, Kausteya. To their love, patience and understanding during this process, I owe the most.

Sunanda Roy Iowa, January 2020

# Chapter 1 Single Variable Functions:  Basics

Chapter 1 reviews some of the fundamental concepts related to sets, set operations, functions and their properties. Section 1 defines sets and their operations. Section 2 describes the basic properties of functions. Sections 3 and 4 discuss two useful function operations: composition and inversion. Section 5 lists some of the important and commonly studied functions and sets in introductory economics courses which are discussed in later chapters of this text.

## 1.1 Sets 1.1.1 Definitions And Set Operations

A set is the fundamental unit of mathematical analysis. A set is defined as any arbitrary collection of objects, physical or abstract.

The objects making up the set are called its elements or members.

Let X denote a set. We use the notation x E X , to indicate that the object x is a member or element of the set X . Similarly, the notation x list of objects are used to denote that these are elements of a set. For example, the list of positive integers, {1,2,3...}, describes the set of natural numbers, N .

In daily life, collections of objects - physical or abstract - are usually formed with a specific practical purpose in mind. The members of such collections end up sharing some common feature or property and the group often has a name. We refer to, for instance, "the electorate", "small businesses", "the milky way" or "tableware". The members of a mathematical set, by contrast, may or may not have any discernible common feature. The collection,

## A = {Tolstoy, The Mad Hatter, Mona Lisa, The Brooklyn Bridge}

with seemingly no common trait that the elements share, qualifies as a set according to the mathematical definition of the term.

A set is described as finite if it has a finite number of elements.

It is described as infinite if it contains infinitely many elements. The set A = {Tolstoy, the mad Hatter, Mona Lisa, the Brooklyn bridge}
is finite. The set of natural numbers N , is infinite. The set of all real numbers which is commonly denoted by R , is another example of an infinite set that plays a very important part in mathematics.

2 A large finite set or an infinite set is often described by specifying a common property that its elements share since it is difficult or impossible to list all its elements. For example, we may describe the set of all large cap companies, as L = {All companies with equity capital above $10 billion}
In descriptions of infinite sets, the sign " |" is used to stand for
"such that". Expressions to the right of the sign specify any common property or properties that the elements of the set share.  For example, the set S = {(x,y) | x + y = 1} is the collection of paired numbers,
( x, y ) which satisfy the equation x + y = 1. Geometrically, S turns out to be all the points on a straight line in the 2-dimensional x - y (Cartesian) plane.

Sets and set operations are extremely useful in simplifying and shortening descriptions in mathematical economics that would otherwise become too long and complicated if stated in any other language.

Let X and Y be two sets. We say that X is a subset of Y if all members of X are also members of Y . This relationship is denoted by the notation, X ⊆ Y .

If, all members of X are members of Y and all members of Y are also members of X , then both statements are true: namely, X C Y
and Y C_ X . In such cases we say that the sets are identical or equal, that is, X = Y . If all members of X are members of Y but some members of Y are not members of X , we say that X is a proper subset of Y and denote this relationship by the notation, X C Y.

3 The last relationship implies that the set X has fewer elements than the set Y.

A null set is a set with no elements in it and is denoted by the symbol 0. When using sets to analyze a given situation, it is useful to think of all sets under study as subsets of a fixed set. This fixed set is described as the universal set for the given context. For example, to study voting patterns of different demographic groups in a society, we may define the set of all registered voters in that society as the universal set.

The union of X and Y , denoted by the notation X U Y , is the set of all elements which are either in X or in Y or in both. The intersection of X and Y , denoted by the notation X N Y , is the set of all elements which belong to both X and Y . If X ∩ Y = ∅ , the sets X and Y have no common elements and are said to be disjoint.

The complement of X in the universal set, denoted by X c , is defined as the set of all elements in the universal set that do not belong to X.

For any two subsets of the universal set, X and Y , the set Y - X
denotes all elements in Y that do not belong to X . The set Y - X is therefore often described as the relative complement of X in Y , as opposed to the complement of X in the universal set (which is denoted by X c .) The relative complement of X in Y is also sometimes denoted by the notation, Y \ X which is read as, "from Y drop all elements of X.

4 and the sets A = {1,2,4}, B = {2,4,5}, C = {1,3,5}, and D =
{1, 2, 3, 4, 5, 6, 8}.

Then A ∩ B = {2,4}; A ∪ B = {1,2,4,5}; A c = {0,3,5,6,7,8,9}
and B − A or B \ A = {5}.

Review Exercise 1.1.1 : Specify the sets DUC , DNC , Dc , D\C ,
C \ D .

EXAMPLE 1.1.2: Let the Universal set be I = {0, ±1, ±2, ±3 . . .},
the set of all positive and negative integers and the number 0. Define X as the set of all positive even integers, Y as the set of all positive odd integers and I as the set of all negative integers. As before, N
denotes the set of natural numbers.

Then X,Y,N ⊂ I and X,Y ⊂ N ; X U Y = N ; Y ∩ X = ∅ ; The complement of X in the Universal set can be expressed as the following union of three sets, X c = Ï ∪ {0} ∪ Y. The relative complement of X
in N is the set N \ X = Y.

Review Exercise 1.1.2 : Express Y c as the union of sets. What is the relative complement of Y in N equal to?

E XAMPLE 1.1.3: Let x and y be real numbers. That is, x, y E R.

Identify the set Z = {(x,y) | y − 2x = 5,x E N,x < 6,y < 13}.

The equation y − 2 x = 5 is the same as y = 2 x +5. Since x ∈ N and x < 6, it can only take values from the set {1, 2, 3, 4, 5}. Correspondingly, y can only take values from the set {7,9,11,13,15}. However as the last condition states that y < 13, the pairs that satisfy all conditions are (1, 7), (2, 9) and (3, 11). Thus Z = {(1, 7), (2, 9), (3, 11)}.

Review Exercise 1.1.3 : Let x,y E R. Identify the set Z =
{( x,y) | x + 2y = 12,x < 10,x ∈ N,y ≤ 7,y ∈ I } .