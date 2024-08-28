# Definitions of all Functions for Satisfiability

def invert(val):
  if (val == True):
    return False
  else:
    return True

class Satisfication:
  def __init__(self, number, variables, clauses):
    self.number = number
    for i in range(len(variables)):
      variables[i] = int(variables[i])
    self.clauses = clauses
    for i in range(len(self.clauses)):
      for j in range(len(self.clauses[i])):
        self.clauses[i][j] = int(self.clauses[i][j])
    # initialize everything as -1 which stands for unknown
    self.values = [-1] # index is equal to the variable
    self.currentVar = 0;
    for i in range(len(variables)):
      self.values.append(-1) # initialize everything to -1
    self.Vals = [-1] # keeps track of values left for each variable (index is variable)
    for i in range(len(variables)):
      self.Vals.append([True,False, -1]) # decision tree
    self.DoneClause = []
    self.Vars = [] # need a list to keep track of the order we assign variables in

  def backtracking(self, Vals, values, Vars): # tries backtracking
    if (len(Vars) > 0):
      v = Vars[-1] # try backtracking
      while v in Vars:
        Vars.remove(v)
      self.assignment(Vals, v, values, Vars)

  def assignment(self, Vals, var, values, Vars): # adds a variable and value to the decision tree
    if (Vals[abs(var)][0] != -1):
      values[abs(var)] = Vals[abs(var)][0]
      Vars.append(abs(var))
      Vals[abs(var)].remove(Vals[abs(var)][0])
      if(len(self.DoneClause) > 0 and self.isSatisfied(self.DoneClause, values) == False):
        self.assignment(Vals, var, values, Vars)

    else: # if it was a previously unit propagation and there are no values left to try
      Vals[abs(var)] = [True, False, -1]
      values[abs(var)] = -1
      try:
        self.backtracking(Vals, values, Vars)
      except:
        Unsatisfied = True # if there are no other options to try for any variable

  def isSatisfied(self, clauses, values):
    Satisfy = True
    for clause in clauses: # double checks if final assignment of values satisfies expression
      satisfied = False
      for literals in clause:
        val = values[abs(literals)]
        if (literals < 0):
          val = invert(val)
        satisfied |= val
      Satisfy &= satisfied
    return Satisfy

  def Check(self, ClauseVar, values, Vals, Vars, satisfied, clause):
    # check for unit propgation and get rid of alternative choices when assigning that variable
    blankvars = 0
    for v in clause: # looks at each variable in a clause
      if (values[abs(v)] == -1):
        blankvars += 1
    for var in clause: # looks at each variable in a clause
      if (blankvars == 1 and satisfied == False and values[abs(var)] == -1): # checks for a unit propagation
        if (var == abs(var)):
          values[abs(var)] = True # if value needes to be true
        else:
          values[abs(var)] = False # if value needs to be false
        Vars.append(abs(var))
        Vals[abs(var)] = [-1]
        blankvars -= 1
      if (values[abs(var)] == -1):
        self.assignment(Vals, var, values, Vars) # try assigning a value to a variable from the list of options
        blankvars -= 1
      val = values[abs(var)]
      if (var < 0):
        val = invert(val) # checks if value is negative
      satisfied |= val
    if (satisfied == False): # if conflict
      self.backtracking(Vals, values, Vars) # backtrack
    try:
      self.Check(ClauseVar, values, Vals, Vars, satisfied, clause) # check if new values work
    except:
      satisfied |= False
    return satisfied
  # repeats each time we focus on a new variable after finishing one variable
  def OneClauseVar(self, currentVar, values, clauses, Vals, Vars): # does not explicitly look for unit propagation
    variable = variables[currentVar] # find clauses with variable inside it
    ClauseVar = []
    for clause in clauses:
      for literal in clause:
        if (variable == abs(literal)):
          if ((clause not in ClauseVar) and (clause not in self.DoneClause)):
            ClauseVar.append(clause)
    # check for -1 for each value...
    satisfied = False
    if (len(ClauseVar) == 0):
      satisfied = True
    NoConflict = False
    back_num = 0
    UnSat = False
    while(NoConflict == False and UnSat == False):
      for clause in ClauseVar: # works for one ClauseVar (check clauses with that variable)
        satisfied = False
        satisfied = self.Check(ClauseVar, values, Vals, Vars, satisfied, clause)
        list1 = []
        list1.append(clause)
        self.DoneClause.append(clause)
      NoConflict = self.isSatisfied(ClauseVar, values)
      if (NoConflict == True):
        break
      back_num += 1
      for i in range(1, back_num):
        if (Vals[-1][0] == -1):
          try:
            v = Vars[-1]
            Vals[abs(v)] = [True, False, -1]
            values[abs(v)] = -1
            while v in Vars:
              Vars.remove(v)
          except:
            UnSat = True # Unsatisfied
        else:
          try:
            v = Vars[-1]
            Vals[abs(v)] = [True, False, -1]
            values[abs(v)] = -1
            while v in Vars:
              Vars.remove(v)
          except:
            UnSat = True
      self.backtracking(Vals, values, Vars)
      if (back_num > 10):
        break
    if (UnSat == True):
      satisfied = False
    return satisfied
  # increment currentVar, then repeat
  def Satisfaction(self, variables, currentVar, values, clauses, Vals, Vars):
    Satisfied = True
    Satisfy = False
    while (currentVar < len(variables)):
      Satisfied &= self.OneClauseVar(currentVar, values, clauses, Vals, Vars)
      if (Satisfied == False):
        break
      else:
        currentVar += 1
    if (Satisfied == True):
      Satisfy = self.isSatisfied(clauses, values)
      for val in values:
        if (val == -1 and values.index(val) != 0):
          Satisfy = False
    if (Satisfy == True):
      print("Satisfied:") # if satisfied
      print(values[1:])
    else:
      Satisfactory = self.isSatisfied(clauses, values)
      if (Satisfactory == True):
        for i in range(1,len(values)):
          if (values[i] == -1):
            Satisfactory = False
        if (Satisfactory == True):
          print("Satisfied:") # final check through to see if everything is accurate (ensures no conflicts)
          print(values[1:])
          Satisfy = True
      else:
        print("Unsatisfied")
    return Satisfy

# Main Program:

number = input("Enter the number of clauses you wish to input: ") # take in number of clauses
variables = input("List of variables: ").split(", ") # take in list of variables
clauses = []
for i in range(int(number)):
  clauses.append(input("Clause: ").split(" ")) # list of clauses

Expression = Satisfication(number, variables, clauses)

Satisfied = Expression.Satisfaction(variables, Expression.currentVar, Expression.values, Expression.clauses, Expression.Vals, Expression.Vars)
while (Satisfied): # will find all possible solutions
  new_clause = []
  for i in range(1,len(Expression.values)):
    if (Expression.values[i] == True):
      new_clause.append(0-i)
    else:
      new_clause.append(i)
  clauses.append(new_clause)
  Expression = Satisfication(number, variables, clauses)
  Satisfied = Expression.Satisfaction(variables, Expression.currentVar, Expression.values, Expression.clauses, Expression.Vals, Expression.Vars)
