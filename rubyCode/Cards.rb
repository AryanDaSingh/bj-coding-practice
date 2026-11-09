class Cards
  # Fields
  @@Deck = []
  @balance = 0 # To be implemented

  # Constructor
  def initialize
    new_deck
    @usr_hand = []
    @dealer_hand = []
  end

  #Methods
  
  public

  def self.get_deck # Remove this in production
    p @@Deck
  end

  def play_round
    new_deck
    shuffle_deck
    deal_hand("p"); deal_hand("d")
    print "Your hand: "; get_hand("p"); puts ""
    print "Dealer's hand: "; get_hand("d"); puts ""
  end

  private

  def new_deck
    ranks = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
    suits = ["S", "H", "C", "D"]
    ranks.each do |rank|
      suits.each do |suit|
        @@Deck.push([rank, suit])
      end
    end
  end

  def shuffle_deck
    @@Deck.shuffle!
  end

  def deal_hand(type)
    if type == "p"
      2.times do
        card = @@Deck.delete_at(rand(@@Deck.length))
        @usr_hand.push(card)
      end
    else
      card = @@Deck.delete_at(rand(@@Deck.length))
      @dealer_hand.push(card)
    end
  end

  def get_hand(type)
    if type == "p"
      @usr_hand.each do |r, s|
        print "#{r}#{s} "
      end
    else
      @dealer_hand.each do |r, s|
        print "#{r}#{s} "
      end
    end
  end
end