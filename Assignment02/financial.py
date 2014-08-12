import random

class Portfolio():
	def __init__(self):
		self.balance = 0.00
		self.hist = "Welcome! Empty portfolio \n"
		self.items = {"Stock" : {}, "Mutual_Fund" : {}}

	def addCash(self, amount_cash):
		if type(amount_cash) != "int" : 
			amount_cash = float(amount_cash)
		self.balance += amount_cash
		self.hist += "You added $ %0.2f in cash, your balance is $ %0.2f \n" % (amount_cash, self.balance)
		return self.balance

	def withdrawCash(self, amount_cash):
		if type(amount_cash) != "int" : 
			amount_cash = float(amount_cash)
		self.balance -= amount_cash
		self.hist += "You withdrew $ %0.2f in cash, your balance is $ %0.2f \n" % (amount_cash, self.balance)
		return self.balance
	
	def history(self):
		print "This is your financial history: \n"
		print self.hist
	
	def buyStock(self, number_shares, stock_name):
		if (number_shares % int(number_shares)) != 0:
			print "Stocks can only be sold or purchased as whole units. Check input."
			self.hist += "Unsuccessful attempt to sell mutual funds \n"
		else:
			stock_cost = stock_name.stock_price * number_shares
			if self.balance < stock_cost:
				print "Sorry, insufficient funds."
				self.hist += "Unsuccessful attempt to buy stocks"
			else:
				self.balance -= stock_cost
				if stock_name.stock_type in self.items["Stock"]:
					self.items["Stock"][stock_name.stock_type] += number_shares
				else:
					self.items["Stock"].update({stock_name.stock_type : number_shares})
				self.hist += "You bought %d stock(s) %s for $%0.2f. Your balance is %0.2f \n" % (number_shares, stock_name.stock_type, stock_cost, self.balance)
		return self.balance

	def buyMutualFund(self, number_shares_mf, mf_name):
		if (number_shares_mf % int(number_shares_mf)) == 0:
			print "Mutual funds can only be sold or purchased as fractional shares. Check input."
			self.hist += "Unsuccessful attempt to sell mutual funds \n"
		else:
			if type(number_shares_mf) == "int": 
				float(number_shares_mf)
			else: 
				pass
			if self.balance < number_shares_mf:
				print "Sorry, insufficient funds." 
				self.hist += "Unsuccessful attempt to buy mutual funds"
			else:
				self.balance -= number_shares_mf
				if mf_name.mf_type in self.items["Mutual_Fund"]:
					self.items["Mutual_Fund"][mf_name.mf_type] += number_shares_mf
				else:
					self.items["Mutual_Fund"].update({mf_name.mf_type : number_shares_mf})
				self.hist +=  "You bought %0.2f mutual fund(s) %s for $%0.2f. Your balance is %0.2f \n" % (number_shares_mf, mf_name.mf_type, number_shares_mf, self.balance)
		return self.balance

	def sellStock(self, stock_name, shares_stock_sell):
		if (shares_stock_sell % int(shares_stock_sell)) != 0:
			print "Stocks can only be sold or purchased as whole units. Check input."
			self.hist += "Unsuccessful attempt to sell stocks \n"
		else:
			self.balance += random.uniform(0.5, 1.5) * shares_stock_sell
			if stock_name in self.items["Stock"]:
				if shares_stock_sell > self.items["Stock"][stock_name]:
					print "Sorry, insufficient number of stocks to sell. Only %d available \n" %self.items["Stock"][stock_name]
					self.hist += "Unsuccessful attempt to sell stocks \n"
				else: 
					self.items["Stock"][stock_name] -= shares_stock_sell
					self.hist += "You sold %d stock(s) for $%0.4f. Your balance is $%0.2f \n" % (shares_stock_sell, (random.uniform(0.5, 1.5) * shares_stock_sell), self.balance)
			else:
				print "Stocks of type %s not found in your account. Cannot complete transaction \n" %stock_name
				self.hist += "Unsuccessful attempt to sell stocks\n"
		return self.balance

	def sellMutualFund(self, mf_name, shares_mf_sell):
		if (shares_mf_sell % int(shares_mf_sell)) == 0.00:
			print "Mutual funds can only be sold or purchased as fractional shares. Check input."
			self.hist += "Unsuccessful attempt to sell mutual funds \n"
		else:
			self.balance += random.uniform(0.9, 1.2) * shares_mf_sell
			if mf_name.mf_type in self.items["Mutual_Fund"]:
				if shares_mf_sell > self.items["Mutual_Fund"][mf_name.mf_type]:
					print "Sorry, insufficient number of mutual funds to sell. Only %d available \n" %self.items["Mutual_Fund"][mf_name.mf_type]
					self.hist += "Unsuccessful attempt to sell mutual funds \n"
				else: 
					self.items["Mutual_Fund"][mf_name.mf_type] -= shares_mf_sell
					self.hist += "You sold %0.2f mutual fund(s) for $%0.4f. Your balance is $%0.2f \n" % (shares_mf_sell, (random.uniform(0.5, 1.5) * shares_mf_sell), self.balance)
			else:
				print "Mutual funds of type %s not found in your account. Cannot complete transaction \n" % mf_name.mf_type
				self.hist += "Unsuccessful attempt to sell mutual funds\n"
		return self.balance

	def __str__(self):
		print "cash: $%0.2f" % self.balance
		print "stock: "
		for i in range(len(self.items["Stock"].values())):
			print "\t %d %s" % (self.items["Stock"].values()[i] , self.items["Stock"].keys()[i])
		print "mutual fund: "
		for j in range(len(self.items["Mutual_Fund"].values())):
			print "\t %d %s" % (self.items["Mutual_Fund"].values()[j] , self.items["Mutual_Fund"].keys()[j])
		return ""

		
		
class Stock():
	def __init__(self, stock_price, stock_type):
		self.stock_type = stock_type
		self.stock_price = stock_price

class MutualFund():
	def __init__(self, mf_type):
		self.mf_type = mf_type













		



