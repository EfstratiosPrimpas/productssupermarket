products = [("ΓΑΛΑ 1LT",1.5), ("ΓΙΑΟΥΡΤΙ ΣΤΡΑΓΓΙΣΤΟ 2%",2.0), ("ΠΑΓΩΤΟ", 2.5), ("ΝΕΣ ΚΑΦΕ", 7.5), ("ΜΠΙΣΚΟΤΑ ΓΕΜΙΣΤΑ", 1.0),
            ("ΣΑΛΑΤΑ ΣΕΦ", 1.0), ("ΤΥΡΙ ΤΟΣΤ", 6.0), ("ΕΞ. ΠΑΡΘΕΝΟ ΕΛΑΙΟΛΑΔΟ", 8.0), ("ΚΑΦΕΣ ΦΙΛΤΡΟΥ", 7.0), ("ΨΩΜΙ ΤΟΣΤ", 1.5)]

# καλαθι = λιστα με τα προιοντα του πελατη, η οποια περιεχει ζευγη στη
# μορφη (αριθμηση προιοντος στην products,ποσοτητα)
basket = list()

def add_products():
    """Προσθετει προιοντα στο καλαθι του χρηστη, εως οτου αυτος να σταματησει να
    εισαγει προιοντα."""
    # δημιουργειται μια απειρη επαναληψη-τερματιζει με break μονο
    # ετσι ωστε ο χρηστης να δωσει τα προιοντα που θελει να αγορασει
    while True:
        # για καθε θεση του προιοντος απο τη λιστα products
        for i in range(len(products)):
            # βαλε στην μεταβλητη products το ονομα του προιοντος
            product = products[i][0]
            # εμφανισε το ονομα του προιοντος
            print(f"Προϊόν #{i}: {product}")
        # απο τον χρηστη ζητειται η αριθμηση του προιοντος απο την λιστα products
        # που επιθυμει να προσθεσει στο καλαθι
        pos = input("Επέλεξε αριθμό προϊόντος: ")
        # οσο ο χρηστης δεν δινει μονο ψηφια η
        # το pos δεν ειναι μια αποδεκτη αριθμηση προιοντος, δηλαδη δεν υπαρχει
        while not(pos.isdigit() and int(pos) in range(len(products))):
            # ξαναζητειται η αριθμηση του προιοντος
            pos = input("Επέλεξε αριθμό προϊόντος: ")
        # σε αυτο το σημειο σιγουρα ο χρηστης εχει δωσει αποδεκτη αριθμηση
        # η οποια μετατρεπεται απο string σε ακεραιο
        pos = int(pos)
        # ο χρηστης ζητειται να εισαγει την ποσοτητα του προιοντος που επελεξε
        quantity = input("Εισάγετε την επιθυμητή ποσότητα: ")
        # οσο ο χρηστης δεν δινει μονο ψηφια η δεν δινει θετικη ποσοτητα
        while not(quantity.isdigit() and int(quantity) > 0):
            # ο χρηστης ζητεται να εισαγει ξανα την ποσοτητα του προιοντος
            quantity = input("Εισάγετε την επιθυμητή ποσότητα: ")
        # σε αυτο το σημειο ο χρηστης εχει δωσει αποδεκτη ποσοτητα προιοντος
        # η οποια μετατρεπεται απο string σε (θετικο) ακεραιο
        quantity = int(quantity)
        # τι γινεται αν προσθεσω προιον που εχω ηδη προσθεσει:
        # στην αρχη,δεν εχουν βρεθει διπλοτυπα προιοντα
        found = False
        # για καθε ζευγος (αριθμος προιοντος,ποσοτητα) στο καλαθι
        for (i, j) in basket:
            # αν η αριθμηση του τρεχοντος προιοντος με την αριθμηση που
            # εδωσε ο χρηστης ειναι ιδιες,τοτε εχουμε διπλοτυπο προιον
            if i == pos:
                # found = True σημαινει βρεθηκε διπλοτυπο προιον
                found = True
                # βρες τη θεση του ζευγους (i,j) στο καλαθι
                p = basket.index((i, j))
                # αφαιρεσε το
                basket.remove((i, j))
                # και στην ιδια θεση προσθεσε την αριθμηση του προιοντος
                # και ως ποσοτητα βαλε τη συνολικη ποσοτητα αυτου του προιοντος
                basket.insert(p, (i, j+quantity))
                # σταματα την απειρη επαναληψη του πιο πανω for, μιας και δεν
                # υπαρχουν αλλα διπλοτυπα προιοντα
                break
        # αν δεν βρεθηκε διπλοτυπο προιον, προσθεσε το ζευγος
        # (αριθμος προιοντος,ποσοσητα) στο καλαθι
        if not found:
            basket.append((pos, quantity))
        # ο χρηστης ζητειται αν θα εισαγει αλλο προιον
        reply = input("Επιθυμείτε να εισάγετε άλλο προϊόν (ν/ο): ")
        # αν δωσει 'ο', δηλαδη οχι, σταματα η αρχικη απειρη επαναληψη while True
        # ετσι ωστε ο χρηστης να μην προσθεσει αλλο προιον
        if reply == 'ο':
            break

def display_basket():
    """Εμφανιζει τα προιοντα του καλαθιου του πελατη"""
    # αρχικοποιηση αθροισματος total με το συνολικο κοστος των προιοντων του καλαθιου
    total = 0
    # αριθμηση προιοντος (ξεκινα απο 1)
    i = 1
    # εμφανισε τις επικεφαλιδες της αποδειξης
    print("ΑΑ       ΕΙΔΟΣ             ΤΜΧ       ΤΙΜΗ ΤΜΧ     ΑΞΙΑ")
    # για καθε ζευγος (αριθμηση , ποσοτητα) στο καλαθι
    for (pos, quantity) in basket:
        # παρε το ονομα του προιοντος στην θεση pos στη λιστα με τα προιοντα products
        item = products[pos][0]
        # παρε την τιμη του προιοντος στην θεση pos στη λιστα με τα προιοντα products
        item_price = products[pos][1]
        # υπολογισε την τιμη ολων των τεμαχιων του προιοντος
        price = item_price * quantity
        # προσθεσε την στην total
        total += price
        # εμφανισε τα αποτελεσματα
        print(f"{i}. {item:12} {quantity:6} {item_price:10}€ {price:10}€")
        i += 1
    # εκτυπωνεται και επιστρεφεται το τελικο συνολικο ποσο πληρωμης
    print(f"\t\t\t\t\t\t\t\t\t\t\tΣΥΝΟΛΟ: {total} €")
    return total


def remove_product():
    """Αφαιρει ενα προιον απο το καλαθι του πελατη"""
    # εμφανιζει τα περιεχομενα του καλαθιου
    display_basket()
    # αν το καλαθι ειναι αδειο
    if not basket:
        # εμφανιζει αναλογο μηνυμα και εκτελει εξοδο απο τη συναρτηση
        print("Άδειο καλάθι")
        return
    # ο χρηστης ζητειται να δωσει την γραμμη του προιοντος που θελει να αφαιρεσει
    line = input("Επέλεξε γραμμή προϊόντος προς αφαίρεση: ")
    # οσο ο χρηστης δεν δινει μονο ψηφια η η γραμμη προιοντος δεν υπαρχει
    while not(line.isdigit() and int(line)-1 in range(len(basket))):
        # του ξαναζητειται η γραμμη προς αφαιρεση
        line = input("Επέλεξε γραμμή προϊόντος προς αφαίρεση: ")
    # η γραμμη μετατρεπεται σε ακεραιο
    line = int(line)
    # ο χρηστης ζητειται να επιβεβαιωσει την αφαιρεση του προιοντος στην γραμμη
    # που δοθηκε
    reply = input("Παρακαλώ επιβεβαιώστε την αφαίρεση (ν/ο): ")
    # αν απαντηση 'ν', δηλαδη ναι
    if reply == 'ν':
        # απο το καλαθι αφαιρειται το ζευγος (αριθμηση,ποσοτητα) στην γραμμη
        # line-1 (ο χρηστης δινει γραμμη 1,2,3,...) διοτι η αριθμηση στην python
        # ξεκινα απο 0
        basket.pop(line-1)
        print("Το προϊόν αφαιρέθηκε επιτυχώς από το καλάθι αγορών")

def buy_products():
    """Αγοραζει τα προιοντα στο καλαθι του πελατη"""
    # αν το καλαθι ειναι αδειο
    if not basket:
        # εμφανιζει σχετικο μηνυμα και εκτελει εξοδο απο την συναρτηση
        print("Άδειο καλάθι")
        return
    # στη μεταβλητη total εισαγουμε το αποτελεσμα της συναρτησης display_basket
    total = display_basket()
    # ο χρηστης ζητειται να επιβεβαιωσει την αγορα των προιοντων του
    reply = input("Παρακαλώ επιβεβαιώστε την αγορά (ν/ο): ")
    # αν η απαντηση ειναι 'ν', δηλαδη ναι
    if reply == 'ν':
        # ζητειται απο το χρηστη η καρτα μελους
        member = input("Έχετε κάρτα μέλους (ν/ο): ")
        # αν ο χρηστης εχει καρτα μελους
        if member == 'ν':
            # γινεται μια εκτωση 7% επι του τελικου ποσου
            discount = round(total*0.07, 2)
            print(f"Έκπτωση {discount}€")
            # αφαιρεται απο το τελικο ποσο
            total -= discount
        # εμφανιση τελικου ποσου
        print(f"Παρακαλούμε πληρώστε {total}€")
        print("Σας ευχαριστούμε για την αγορά σας!")


if __name__ == "__main__":
    while True:
        print("Επιλογές")
        print("========")
        print("1. Προσθήκη προϊόντων στο καλάθι, 2. Εμφάνιση περιεχομένου καλαθιού, 3. Αφαίρεση προϊόντος, 4. Πληρωμή")
        choice = input("Εισάγετε την επιλογή σας:")
        if choice == "1":
            add_products()
        elif choice == "2":
            display_basket()
        elif choice == "3":
             remove_product()
        elif choice == "4":
            buy_products()
            break
        else:
            print("Παρακαλώ εισάγετε έγκυρη επιλογή")
