// SimpleList.h -- a minimal singly linked list with its own iterator, so it
// works with range-based for loops and with standard algorithms.
//
// The list itself is done. Complete the Iterator's five operators (TODOs).
#ifndef SIMPLE_LIST_H
#define SIMPLE_LIST_H

#include <cstddef>
#include <iterator>

template <typename T>
class SimpleList {
private:
    struct Node {
        T item;
        Node *next;
    };

public:
    class Iterator {
    public:
        // These five names let standard algorithms (std::find, std::count,
        // ...) work with this iterator. Given; do not change.
        using iterator_category = std::forward_iterator_tag;
        using value_type = T;
        using difference_type = std::ptrdiff_t;
        using pointer = T*;
        using reference = T&;

        explicit Iterator(Node *node = nullptr) : current_(node) {}

        // TODO 1: return a reference to the current node's item.
        T &operator*() const;

        // TODO 2: pre-increment (++it): move to the next node, return *this.
        Iterator &operator++();

        // TODO 3: post-increment (it++): remember a copy of *this, move to the
        //         next node, return the copy. (The int parameter is a dummy
        //         that tells the compiler this is the postfix version.)
        Iterator operator++(int);

        // TODO 4 and 5: two iterators are equal when they point to the same node.
        bool operator==(const Iterator &other) const;
        bool operator!=(const Iterator &other) const;

    private:
        Node *current_;
    };

    SimpleList() : head_(nullptr), tail_(nullptr), size_(0) {}
    ~SimpleList() {
        while (head_ != nullptr) {
            Node *next = head_->next;
            delete head_;
            head_ = next;
        }
    }
    SimpleList(const SimpleList &) = delete;              // copying not needed today
    SimpleList &operator=(const SimpleList &) = delete;

    void pushBack(const T &item) {
        Node *node = new Node{item, nullptr};
        if (tail_ == nullptr) {
            head_ = node;
        } else {
            tail_->next = node;
        }
        tail_ = node;
        size_++;
    }

    int size() const { return size_; }

    Iterator begin() { return Iterator(head_); }
    Iterator end() { return Iterator(nullptr); }    // one past the last node

private:
    Node *head_;
    Node *tail_;
    int size_;
};

// ------------------------------------------------- Iterator implementation
// Defined outside the class, so each needs the full template header.

template <typename T>
T &SimpleList<T>::Iterator::operator*() const {
    return current_->item;     // TODO 1 is done for you, as an example
}

// TODO 2: SimpleList<T>::Iterator::operator++()   (pre-increment)
//   Note the return type must be written as
//     typename SimpleList<T>::Iterator&
//   because Iterator is a type that depends on T.

// TODO 3: SimpleList<T>::Iterator::operator++(int)   (post-increment)

// TODO 4: operator==

// TODO 5: operator!=   (use ==)

#endif
