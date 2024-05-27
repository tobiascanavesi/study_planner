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

## 1.1.2 Venn Diagrams

Venn diagrams are a useful geometric way to understand set relationships. Sets are represented by geometric shapes, usually circles, and are embedded in a larger rectangular area representing the universal set.

E XAMPLE 1.1.4: One of Gulliver's famous voyages was to the island of Laputa where all citizens were devoted to the Arts. Let Ω be the set of all citizens of Laputa.  Let M be the set of music lovers, B be the set of mathematicians and A be the set of amateur astronomers. Use Venn diagrams to identify the sets, M ∪ B, M ∩ B, ( M ∪ B ) ∩ A and MU(BNA). Establish the relationship between (M\B)U(B\M)
and ( M ∪ B ) \ ( B ∩ M ).

The large rectangles in Figures 1.1.1a)-e) represent the Universal set, Ω. Assume that there are Laputans who are neither music lovers, nor mathematicians, nor amateur astronomers but devoted to some other Arts. Then the sets M , B and A are therefore proper subsets of Ω and are represented by the circles.

In Figure 1.1.1a), the shaded area (includes both the dark and the lightly shaded) represents the set M ∪ B . It includes all members who belong to either circle M or circle B or both circles. The lensshaped dark shaded area in Figure 1.1.1b) represents the set M ∩ B . It includes only members who belong to both circles M and B .

The shaded areas marked "a" in Figure 1.1.1c) represent the set
(M U B) N A. The elements in the two brown circles represent the set ( M ∪ B ). The set A includes elements in the gray circle. The set ( M ∪ B ) ∩ A includes only those elements which are common to the brown and the gray shaded areas.

The shaded areas marked "b" in Figure 1.1.1d) represent the set MU( BNA ). The set ( BNA ) includes elements that are only common to the green and gray circles. Add to this set, the elements from the brown circle M to get M ∪ ( B ∩ A ).

The blue crescent shaped shaded area in Figure 1.1.1e) represents the set ( M \ B ). The yellow crescent shaped shaded area represents
( B \ M ). These two sets are disjoint - the lens shaped intersection of the sets M and B are not included in either relative complements.

The set ( M \ B ) ∪ ( B \ M ) is represented by the union of the two areas marked "c".

It is clear from Figure 1.1.1e) that the set ( M \ B ) U ( B \ M ) has been obtained from the union set ( MUB ) by removing the lens shaped intersection set ( M ∩ B ). In other words, the set ( M \ B ) ∪ ( B \ M ) is identical to the set ( M ∪ B ) \ ( B ∩ M ).

Although the last assertion is clear, it is nevertheless useful to know how such logical equivalences are established in mathematics without the visual aid of Venn diagrams. We show this in Example 1.1.5.

EXAMPLE 1.1.5: Prove that (M\B)U(B\M) = (MUB)\(BNM).

Let x ∈ ( M \ B ) ∪ ( B \ M ). Then either x ∈ ( M \ B ) or x ∈ ( B \ M ).

7 Note that as these two sets are disjoint, x cannot belong to both. If x ∈ ( M \ B ) then x ∈ M but x ⇔ B . This implies that x ∈ ( M ∪ B )
and x & ( B ∩ M ). Hence x ∈ ( M ∪ B ) \ ( B ∩ M ). If x ∈ ( B \ M ) then x E B but x E M . This implies that x E ( M ∪ B ) and x E ( B ∩ M ). Hence x ∈ ( M ∪ B ) \ ( B ∩ M ). As any element x which belongs to
( M \ B ) ∪ ( B \ M ) also belongs to ( M ∪ B ) \ ( B ∩ M ) we conclude that ( M \ B ) ∪ ( B \ M ) ⊆ ( M ∪ B ) \ ( B ∩ M ).

Next consider y ∈ ( M ∪ B ) \ ( B ∩ M ). Then y ∈ ( M ∪ B ) but y ξ ( B∩ M ). Hence either y ∈ M or y ∈ B but not both. If y ∈ M and y & B , then y ∈ ( M \ B ). Hence y ∈ ( M \ B ) ∪ ( B \ M ). If y ∈ B and y & M then y ∈ ( B \ M ). Hence y ∈ ( M \ B ) ∪ ( B \ M ). As any element y belonging to ( M ∪ B ) \ ( B ∩ M ) also belongs to ( M \ B ) ∪ ( B \ M ), we conclude that ( M ∪ B ) \ ( B ∩ M ) ⊆ ( M \ B ) ∪ ( B \ M ). As both subset relationships are true, the sets are equal.

E XAMPLE 1.1.6: Describe in words the set Y = ( M\B )U(B\M ).

One way to describe the set Y is as follows: "Y is the set of Laputans who either love music but not mathematics or love mathematics but not music". There is a second way to describe the set which takes advantage of the fact that ( M\B )U(B\M ) = ( MUB )\( BnM ). The set (MUB)\(B N M) can be described as, "The set of Laputans who either love music or mathematics but not both". Since these sets are identical, the latter sentence also describes the set Y and may in fact sound more elegant than the first!

Review Exercise 1.1.4 : Establish the relationship between (1)
( M \ B ) ∪ ( M \ A ) and M \ ( B ∩ A ) and (2) ( M \ B ) ∪ ( M \ A ) and M \ ( B U A ). You may use either Venn diagrams or statements.

## 1.1.3 The Set Of Real Numbers

The set of real numbers R, plays a most important role in mathematical economics and is a union of two disjoint sets: (1) the set of rational numbers and (2) the set of irrational numbers.

Rational numbers are those that can be expressed as ratios of two integers, such as the number 7 = 1 , the number 1 ⁄ 2 and the number 0.62 = 100. The number 0 can be expressed as such a ratio in infinitely many equivalent ways since 0 = f = f = f = ... = 100,000 = .... It is clear from the first example that the set of integers is a subset of the set of rationals.

Irrational numbers are those that cannot be expressed as ratios of two integers. Examples include the numbers √ 2, √ 3 and the natural constant π . The ratio f and the ratios f , where p is any real number, are not defined in mathematics.

When we try to convert a ratio of two integers into a decimal number, one of two things happen. Either, the series of digits after the decimal point terminates such as for the ratio 3 = 0.75. Or else, a subset of the digits are infinitely repeated, such as for the ratio 995 = 0.132132132 . . . Thus, rational numbers are often described as those that have a finite or recurring decimal expansion. By contrast, irrational numbers have decimal expansion that neither terminates, nor are recurring.

An interval is a subset of the set R, consisting of all numbers that lie within two numbers that are described as its bounds. The bounds themselves may or may not be members of the interval in question. The brackets, "[,]" and "(,)", indicate whether or not a bound is included in the set. For example, the interval [ a, b ) is the set of all numbers lying between a and b with the lower bound a included in the set but the upper bound b , not included.

## 1.2 Functions 1.2.1 Definitions

Consider two arbitrary sets, X and Y. A function, denoted by f, is a rule that assigns to each element of the set X, one and only one element of the set Y. A function is represented in notation as f : X −→ Y which reads as "f maps X to Y." There are several ways of describing or specifying such a rule.

E XAMPLE 1.2.1: If X and Y are specified by a list of their members, the function rule may be described by a series of sentences or by a table. Consider the sets X = {cat, mat, bat} and Y = {A, B, C}.

The following sentence in bold describes a function, f : X −→ Y :
f assigns B to "cat", A to "mat" and C to "bat".

Alternatively, f may be represented by the following table:
f(cat)
= B
f(mat) = A
f (bat)
= C
E XAMPLE 1.2.2: A function may be represented by an algebraic formula. Let X,Y C R. To each real number x E X, we assign another real number y E Y by using the rule f, where y = f(x) =
x 2 + 1. Thus, to x = 1, the rule f assigns the real number 2.

E XAMPLE 1.2.3: In many cases, a function may not admit a closed algebraic form. Assume, for example that y E Y denotes measured quarterly GDP in the US and x ∈ X denotes quarterly time points from 2005 to the 2013. Although a functional relationship between the elements of X and Y exists, it is too complex to have a closed algebraic form. The functional relationship in this case is represented by a 2-dimensional plot of the X-values and their corresponding Y- values as shown in Figure 1.2.1.

![22_image_0.png](22_image_0.png)

## 1.2.2 Vertical Line Test

Any rule that assigns elements of Y to elements of X must have the following property in order to qualify as a function. It can assign the same element y E Y to multiple elements x ′ , x ′′ E X . But it cannot assign multiple elements of Y to one element x ∈ X .

E XAMPLE 1.2.4: Let X = {cat, mat, bat} and Y = {A,B,C}.

The rule q below is a function although it assigns the same element

| g(cat)   | ll   | B   |
|----------|------|-----|
| g(mat)   | B    |     |
| ll       |      |     |
| g(bat)   | = C  |     |

B to both "cat" and "mat". But the rule h is not a function because it assigns two elements, A and B to one element, "cat".

$=\quad A,B$  $=\quad A$  $=\quad C$  . 
E XAMPLE 1.2.5: Let X, Y C R. The expression y = x 2 represents a function. To both x = 2 and x = − 2, the rule assigns the same real number 4. Indeed, the rule assigns the same y -value to any pair of x 's with the same magnitude but different signs. However, the algebraic

| h(cat)   | II A, B   |    |
|----------|-----------|----|
| h(mat)   | ll        | A  |
| h(bat)   | = C       |    |

expression y 2 = 4 x does not represent a function.

When X,Y C R and the rule f can be represented by a 2dimensional plot of the X-values and their corresponding Y-values, there is a simple geometric test, called the vertical-line test to verify if f is a function. We draw a vertical line through any point on the X-axis. If f is a function, the vertical line intersects the plot at one point at most. If the vertical line intersects the plot at two or more points, the plot does not represent a function.

The plot in Figure (1.2.2a) represents a function however much complicated it looks.  Any vertical line intersects the curve at one point only, as the dashed lines in the figure show. By contrast the simpler looking and familiar ellipse in Figure (1.2.2b) does not represent a function as the given vertical line intersects it at the two bulleted points.

![24_image_0.png](24_image_0.png)

## 1.2.3 Domain And Range

Consider the function, f : X - → Y . The set X is described as the domain of f and the set Y as the range of f . The element, y = f ( x ) ∈ Y corresponding to x E X , is described as the image of x under f or the value of the function at x E X . Alternatively, in the expression y = f(x), the variable x is often described as the argument of f or the independent variable, whereas y is often described as the dependent variable.

In many economic applications, the domain of a function is either explicitly specified or clearly understood because of the context.  If the domain is not explicitly specified or clearly understood and f is an algebraic expression, the default domain of f is defined as the largest set X for which the value f ( x ) is unique. Moreover, while functions in general can have range sets that contains imaginary values, the present text looks at only real valued functions as being the most useful in introductory economics applications. The default domain of a function is therefore, the largest set X for which the value f ( x ) is unique and real. The following examples illustrate.

E XAMPLE 1.2.6: Suppose f ( x ) = x . To each x value, the function f assigns the value y E Y = x . The default domain is the set of all real numbers as, for each real number, the value of the function is well defined and unique.  Geometrically, in a 2-dimensional x - y plane, the function can be represented by a straight line through the origin and a slope of 45 degrees. In notations, X = (-oo, oo). Similarly the default domain of f ( x ) = x 2 is X = (- ∞ , ∞ ).

E XAMPLE 1.2.7: Suppose f ( x ) = √ x . Then, the default domain of f is X = [0,00), as the square root of a negative number is not real.

E XAMPLE 1.2.8: Suppose f ( x ) = 
the set of all real numbers except the numbers 3 and - 3, since at x = 3 or -3, the value of the function is not defined. In notations, X = (−∞,∞) \ {−3,3}.

EXAMPLE 1.2.9: Suppose f(x) = √ 4 + 3x (the positive square root of (4 + 3 x )). The default domain is the set of all real numbers 14 greater than or equal to − 3 because for any x < − 4/3 the value of the expression within the root sign is negative and √ 4 + 3 x is not a real number. In notations, X = [-
Review Exercise 1.2.1 : Specify the default domains of the functions (1) f(x) = x² − 1 and (2) f(x) = √x² − 1.

## 1.2.4 Evaluating Functions

When f has a closed algebraic form, to evaluate f at any given point x = c E X, we replace the variable x by c in the expression for f(x) in all places where it appears.

E XAMPLE 1.2.10: Suppose f ( x ) = x 2 - 2 x - 3. Then,

$$\begin{array}{r l r l}{f(0)}&{{}=0^{2}-2.0-3}&{}&{{}=-3,}\\ {f({\frac{1}{\sqrt{2}}})}&{{}=({\frac{1}{\sqrt{2}}})^{2}-2{\frac{1}{\sqrt{2}}}-3}&{}&{{}=-{\frac{5}{2}}-{\sqrt{2}},}\\ {f(a)}&{{}=a^{2}-2a-3,}\\ {f(-x)}&{{}=(-x)^{2}-2(-x)-3}&{{}=x^{2}+2x-3.}\end{array}$$

Review Exercise 1.2.2 : Find the values of f(5) and f(-4) for the function f(x) = 2x 3 − 5x 2 + 8x − 20.

If the domain and range of f are sets of real numbers but f(x)
does not have a closed algebraic form (as in Example 1.2.1), to find the value of f at any point in the domain, we simply read the y -value off the graph of f .

## 1.2.5 Graph Of A Function

In the next several chapters we study functions whose domains are subsets of R. Thus, the independent variable is one-dimensional, like the real line.  We describe such functions as single variable functions.

Consider a single variable function, f : X −→ Y where X,Y ⊆ R.

The graph of f is the set of all ordered pairs (x, f(x)), where the first element of the pair is a point in the domain of the function and the second element is the corresponding value of the function at that point. It is important to note that the graph is not a set of all arbitrarily formed pairs of elements from the domain and the range sets. The choice of the first element in the pair, x , determines the choice of the second element, f ( x ), in the pair.  Geometrically, the pair ( x, f ( x )) is represented as a point in a 2-dimensional plane described as the Cartesian plane which in turn is represented by a pair of axes that are perpendicular to each other. The pair (x, f(x)) is at a distance of x units from the horizontal axis and f ( x ) units from the vertical axis. The graph of f is a line or a curve formed by joining all such points.

In many economic applications, the value of a function depends on the values of multiple independent variables. In such cases, the domain set X needs to be thought of as a set of points in a multidimensional space.  For instance, the value of the variable y may depend on the values of two independent variables. In this case, the domain is a set of points on a 2-dimensional Cartesian plane, where each axis can be used to represent a different independent variable. If three independent variables determine the value of y , the domain of the function is a set of points in a 3-dimensional cube. Such functions are described as multi-variate functions.  Some of the economic scenarios that are best captured by multi-variate functions are mentioned in Section 5. Study of such functions including their graphs is relegated to Chapters 7 and 8 in the text.

Function expressions often involve constants which are described as parameters. Parameters are really variables that are assumed to be constant within a specific given context. In many economic applications, the parameters are actually some independent variables of a multi-variate function that are temporarily held constant at specific levels while the analysis focuses on studying the influence of the others.

If a function expression involves a parameter, a change in the value of the parameter shifts the graph of the function on the 2-dimensional Cartesian plane.  Graph shifts are a useful way to capture the behavior of a multivariate function on a 2-dimensional plane.  By holding all but one independent variable constant, we plot the function on the Cartesian plane. The effects of the other variables are then studied by shifting this graph.

The following example illustrates how changes in some cost components may be captured by a shift of the total cost curve. Chapter 3 describes common types of graph shifts that are useful in economics.

E XAMPLE 1.2.11: The total cost of producing q units of a good is given by C (q) = F + 2q 2 where F represents a fixed cost that a firm must incur if it decides to produce. Assume that F depends on the size of the manufacturing facility the firm chooses, with a larger sized factory implying a higher F . Plot the cost curves for the values F = 200 and F = 250 on a 2-dimensional plane and discuss what happens to the cost per unit of producing 100 units when the fixed cost increases from 200 to 250.

![29_image_0.png](29_image_0.png)

The solid line in Figure 1.2.3 corresponds to F = 200 and the dashed one, to F = 250.  A higher fixed cost leads to a higher total cost C (q) for each value of q. In other words, a change in the parameter F
shifts the graph of the function C (q) vertically upwards. The cost of producing 100 units when F = 200 is C (100) = 200+2(100) 2 = 20200.

The cost per unit is C ( q = 20200 = 202. The cost of producing 100 units when F = 250 is 20250. The cost per unit is 202.50.

## 1.3 Function Composition

Suppose f : X −→ Y and g : Y −→ Z are two functions where X , Y
and Z are all subsets of R. The composition of g with f , denoted by g ø f , is a function that maps elements of X into elements of Z
in two steps. Under g ø f , we first take the image of x under f .