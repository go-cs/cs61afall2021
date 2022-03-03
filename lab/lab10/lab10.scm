(define (over-or-under num1 num2) 
  'YOUR-CODE-HERE
  (if (> num1 num2) 1 
  (if (= num1 num2) 0 
  (if (< num1 num2) -1)))
  )

(define (make-adder num) 
  'YOUR-CODE-HERE
  (lambda (inc) (+ num inc))
  )

(define (composed f g) 
  'YOUR-CODE-HERE
  (lambda (x)(f (g x)))
  )

(define lst 
  ;((1) 2 (3 4) 5)
  ;(list (list 1) 2 (list 3 4) 5)
  '((1) 2 (3 4) 5)
  )

(define (remove item lst) 
  (filter (lambda (x) (not (= x item))) lst))
